"""AnnData contracts, loaders and leakage-aware splits for the tutorials."""

from __future__ import annotations

import warnings
from collections.abc import Iterable, Sequence
from pathlib import Path
from typing import Any

import anndata as ad
import numpy as np
import pandas as pd
from scipy import sparse

REQUIRED_OBS = ("condition", "cell_type", "batch", "replicate")
REQUIRED_VAR = ("gene_name",)
REQUIRED_LAYERS = ("X_norm",)
CONTROL_CONDITION = "ctrl"
CONTRACT_VERSION = 2


def _matrix_values(matrix: Any) -> np.ndarray:
    if sparse.issparse(matrix):
        return np.asarray(matrix.data)
    return np.asarray(matrix)


def _is_count_matrix(matrix: Any) -> bool:
    values = _matrix_values(matrix)
    return bool(
        (values.size == 0)
        or (
            np.isfinite(values).all()
            and (values >= 0).all()
            and np.allclose(values, np.round(values), atol=1e-6)
        )
    )


def validate_adata_contract(
    adata: ad.AnnData,
    *,
    control: str = CONTROL_CONDITION,
    expected_conditions: Iterable[str] | None = None,
    expected_genes: Iterable[str] | None = None,
    require_counts: bool = False,
) -> None:
    """Validate AnnData contract v2 without silently inventing missing fields.

    ``layers.counts`` is optional because several public perturbation datasets
    only distribute processed expression. When it is present, this validator
    requires it to look like raw, non-negative integer counts.
    """

    if adata.n_obs == 0 or adata.n_vars == 0:
        raise ValueError("AnnData must contain at least one cell and one gene.")

    missing_obs = [name for name in REQUIRED_OBS if name not in adata.obs]
    missing_var = [name for name in REQUIRED_VAR if name not in adata.var]
    missing_layers = [name for name in REQUIRED_LAYERS if name not in adata.layers]
    if missing_obs:
        raise ValueError(f"Missing obs fields: {', '.join(missing_obs)}")
    if missing_var:
        raise ValueError(f"Missing var fields: {', '.join(missing_var)}")
    if missing_layers:
        raise ValueError(f"Missing layers: {', '.join(missing_layers)}")
    if require_counts and "counts" not in adata.layers:
        raise ValueError("layers.counts is required for this operation but is unavailable.")

    for field in REQUIRED_OBS:
        values = adata.obs[field]
        if values.isna().any() or values.astype(str).str.strip().eq("").any():
            raise ValueError(f"obs.{field} contains empty values.")

    conditions = adata.obs["condition"].astype(str)
    if control not in set(conditions):
        raise ValueError(f"Control condition {control!r} is absent.")
    if len(set(conditions) - {control}) == 0:
        raise ValueError("At least one non-control perturbation is required.")
    if expected_conditions is not None:
        missing_conditions = sorted(set(expected_conditions) - set(conditions))
        if missing_conditions:
            raise ValueError(
                "Expected perturbation groups have no cells: "
                f"{', '.join(missing_conditions)}"
            )

    gene_names = adata.var["gene_name"]
    if gene_names.isna().any() or gene_names.astype(str).str.strip().eq("").any():
        raise ValueError("var.gene_name contains empty values.")
    gene_names = gene_names.astype(str)
    if gene_names.duplicated().any():
        duplicated = gene_names[gene_names.duplicated()].iloc[0]
        raise ValueError(f"var.gene_name must be unique; duplicate: {duplicated}")
    if expected_genes is not None:
        missing_genes = sorted(set(expected_genes) - set(gene_names))
        if missing_genes:
            raise ValueError(f"Unknown or missing genes: {', '.join(missing_genes[:5])}")

    for name in REQUIRED_LAYERS:
        values = _matrix_values(adata.layers[name])
        if values.size and not np.isfinite(values).all():
            raise ValueError(f"layers.{name} contains NaN or infinite values.")
    if "counts" in adata.layers and not _is_count_matrix(adata.layers["counts"]):
        raise ValueError(
            "layers.counts must contain non-negative integer-like raw counts; "
            "processed expression must only be stored in layers.X_norm."
        )


def make_synthetic_adata(
    *,
    seed: int = 42,
    n_per_condition: int | dict[str, int] = 48,
    n_genes: int = 48,
) -> ad.AnnData:
    """Create deterministic sparse data with three independent replicates."""

    if n_genes < 24:
        raise ValueError("n_genes must be at least 24 for the synthetic effects.")
    rng = np.random.default_rng(seed)
    conditions = ["ctrl", "gene_000", "gene_006", "gene_012", "gene_018"]
    if isinstance(n_per_condition, int):
        sizes = {condition: n_per_condition for condition in conditions}
    else:
        sizes = {condition: int(n_per_condition.get(condition, 0)) for condition in conditions}
    if any(size <= 0 for size in sizes.values()):
        raise ValueError("Every synthetic condition must contain at least one cell.")
    if sizes["ctrl"] < 3:
        raise ValueError("Synthetic controls require at least three cells.")

    base_rate = rng.gamma(shape=2.5, scale=1.4, size=n_genes) + 0.3
    effects: dict[str, np.ndarray] = {}
    for index, condition in enumerate(conditions[1:]):
        effect = np.zeros(n_genes)
        start = index * 6
        effect[start : start + 4] = np.array([0.9, 0.7, 0.5, 0.35])
        effect[start + 4 : start + 6] = np.array([-0.6, -0.4])
        effect[-4:] += np.array([0.3, 0.2, -0.15, 0.1])
        effects[condition] = effect

    matrices: list[np.ndarray] = []
    obs_rows: list[dict[str, str]] = []
    for condition in conditions:
        effect = effects.get(condition, np.zeros(n_genes))
        rates = base_rate * np.exp(effect)
        size_factors = rng.lognormal(mean=0.0, sigma=0.18, size=sizes[condition])
        rate_matrix = size_factors[:, None] * rates[None, :]
        counts = rng.poisson(rate_matrix).astype(np.float32)
        matrices.append(counts)
        for cell_index in range(sizes[condition]):
            replicate_index = cell_index % 3 + 1
            obs_rows.append(
                {
                    "condition": condition,
                    "cell_type": "K562",
                    "batch": f"batch_{replicate_index}",
                    "replicate": f"replicate_{replicate_index}",
                }
            )

    counts_dense = np.vstack(matrices)
    library_size = counts_dense.sum(axis=1, keepdims=True)
    library_size[library_size == 0] = 1
    x_norm = np.log1p(counts_dense / library_size * 10_000).astype(np.float32)
    counts_sparse = sparse.csr_matrix(counts_dense)
    norm_sparse = sparse.csr_matrix(x_norm)
    gene_names = [f"gene_{index:03d}" for index in range(n_genes)]

    obs_index = [f"cell_{index:04d}" for index in range(len(obs_rows))]
    adata = ad.AnnData(
        X=norm_sparse.copy(),
        obs=pd.DataFrame(obs_rows, index=obs_index),
        var=pd.DataFrame({"gene_name": gene_names}, index=gene_names),
    )
    adata.layers["counts"] = counts_sparse
    adata.layers["X_norm"] = norm_sparse.copy()
    adata.uns["aivc_contract"] = {
        "version": CONTRACT_VERSION,
        "counts_available": True,
        "counts_provenance": "synthetic_raw_counts",
    }
    adata.uns["dataset"] = {
        "name": "synthetic-perturbation-smoke-test",
        "seed": seed,
        "is_biological_data": False,
    }
    validate_adata_contract(adata, require_counts=True)
    return adata


def _first_present(frame: pd.DataFrame, candidates: Sequence[str]) -> str | None:
    return next((name for name in candidates if name in frame), None)


def _standardize_norman(adata: ad.AnnData) -> ad.AnnData:
    """Normalize metadata while preserving uncertainty about raw counts."""

    result = adata.copy()
    condition_source = _first_present(
        result.obs, ("condition", "perturbation", "condition_name")
    )
    if condition_source is None:
        raise ValueError("Norman data has no recognizable perturbation column.")
    result.obs["condition"] = result.obs[condition_source].astype(str)
    if "cell_type" not in result.obs:
        result.obs["cell_type"] = "K562"

    batch_source = _first_present(result.obs, ("batch", "batch_id", "library", "sample"))
    replicate_source = _first_present(
        result.obs, ("replicate", "replicate_id", "donor", "sample")
    )
    result.obs["batch"] = (
        result.obs[batch_source].astype(str) if batch_source else "unreported"
    )
    result.obs["replicate"] = (
        result.obs[replicate_source].astype(str) if replicate_source else "unreported"
    )
    if "gene_name" not in result.var:
        result.var["gene_name"] = result.var_names.astype(str)
    if "X_norm" not in result.layers:
        result.layers["X_norm"] = result.X.copy()

    counts_source = None
    if "counts" in result.layers and _is_count_matrix(result.layers["counts"]):
        counts_source = "upstream_counts_layer"
    elif result.raw is not None and set(result.var_names).issubset(set(result.raw.var_names)):
        raw_counts = result.raw[:, result.var_names].X
        if _is_count_matrix(raw_counts):
            result.layers["counts"] = raw_counts.copy()
            counts_source = "upstream_raw"
    if counts_source is None:
        result.layers.pop("counts", None)

    result.uns["aivc_contract"] = {
        "version": CONTRACT_VERSION,
        "counts_available": counts_source is not None,
        "counts_provenance": counts_source or "not_distributed",
        "batch_reported": batch_source is not None,
        "replicate_reported": replicate_source is not None,
    }
    validate_adata_contract(result)
    return result


def load_norman(data_dir: str | Path = "data") -> ad.AnnData:
    """Load the GEARS-supported Norman dataset through the official API."""

    try:
        from gears import PertData
    except ImportError as exc:
        raise RuntimeError(
            "Norman mode requires GEARS. Install `pip install -e '.[gears]'`, "
            "or keep using mode='synthetic'."
        ) from exc

    target = Path(data_dir)
    target.mkdir(parents=True, exist_ok=True)
    try:
        perturbation_data = PertData(str(target))
        perturbation_data.load(data_name="norman")
    except Exception as exc:
        raise RuntimeError(
            "Unable to load Norman through GEARS. Check storage, network and "
            "the upstream host; synthetic mode remains available offline."
        ) from exc
    return _standardize_norman(perturbation_data.adata)


def load_dataset(
    mode: str = "synthetic",
    *,
    data_dir: str | Path = "data",
    seed: int = 42,
) -> ad.AnnData:
    if mode == "synthetic":
        return make_synthetic_adata(seed=seed)
    if mode == "norman":
        return load_norman(data_dir=data_dir)
    raise ValueError("mode must be either 'synthetic' or 'norman'.")


def _partition(items: Sequence[str], *, seed: int) -> dict[str, list[str]]:
    if len(items) < 3:
        raise ValueError("At least three units are required for train/val/test splits.")
    rng = np.random.default_rng(seed)
    shuffled = list(rng.permutation(list(items)))
    n_total = len(shuffled)
    n_train = max(1, int(np.floor(n_total * 0.6)))
    n_val = max(1, int(np.floor(n_total * 0.2)))
    if n_train + n_val >= n_total:
        n_train, n_val = n_total - 2, 1
    return {
        "train": shuffled[:n_train],
        "val": shuffled[n_train : n_train + n_val],
        "test": shuffled[n_train + n_val :],
    }


def condition_split(
    adata: ad.AnnData,
    *,
    seed: int = 42,
    control: str = CONTROL_CONDITION,
) -> dict[str, ad.AnnData]:
    """Hold out entire perturbations and allocate disjoint control cells.

    Controls are split by ``batch × replicate`` when at least three such units
    exist. If upstream replicate metadata is unavailable, controls are split at
    cell level and the fallback is recorded in ``uns['split_audit']``.
    """

    validate_adata_contract(adata, control=control)
    conditions = adata.obs["condition"].astype(str)
    perturbations = sorted(set(conditions) - {control})
    condition_units = _partition(perturbations, seed=seed)

    control_obs = adata.obs.loc[conditions == control].copy()
    control_groups = (
        control_obs["batch"].astype(str) + "::" + control_obs["replicate"].astype(str)
    )
    unique_groups = sorted(control_groups.unique())
    control_indices: dict[str, list[str]]
    split_basis: str
    if len(unique_groups) >= 3:
        group_split = _partition(unique_groups, seed=seed + 1)
        control_indices = {
            name: control_obs.index[control_groups.isin(groups)].astype(str).tolist()
            for name, groups in group_split.items()
        }
        split_basis = "batch_x_replicate"
    else:
        warnings.warn(
            "Fewer than three independent control groups were reported; "
            "falling back to disjoint control-cell partitions.",
            RuntimeWarning,
            stacklevel=2,
        )
        control_indices = _partition(control_obs.index.astype(str).tolist(), seed=seed + 1)
        split_basis = "cell_fallback_no_reported_replicates"

    splits: dict[str, ad.AnnData] = {}
    for name in ("train", "val", "test"):
        perturbation_mask = conditions.isin(condition_units[name])
        control_mask = adata.obs_names.astype(str).isin(control_indices[name])
        subset = adata[np.asarray(perturbation_mask | control_mask)].copy()
        subset.uns["split_audit"] = {
            "seed": seed,
            "held_out_unit": "condition",
            "control_split_basis": split_basis,
            "conditions": sorted(condition_units[name]),
            "control_cell_count": len(control_indices[name]),
        }
        splits[name] = subset
    return splits


def pseudobulk(
    adata: ad.AnnData,
    *,
    groupby: Sequence[str] = ("condition",),
    layer: str = "X_norm",
) -> pd.DataFrame:
    """Average expression over explicit experimental units."""

    if layer not in adata.layers:
        raise ValueError(f"Layer {layer!r} is missing.")
    missing = [field for field in groupby if field not in adata.obs]
    if missing:
        raise ValueError(f"Missing pseudobulk fields: {', '.join(missing)}")
    frame = adata.obs.loc[:, list(groupby)].astype(str)
    labels = pd.MultiIndex.from_frame(frame) if len(groupby) > 1 else frame.iloc[:, 0]
    matrix = adata.layers[layer]
    rows: list[np.ndarray] = []
    names: list[Any] = []
    for label in labels.drop_duplicates():
        mask = np.asarray(labels == label)
        rows.append(np.asarray(matrix[mask].mean(axis=0)).reshape(-1))
        names.append(label)
    index: pd.Index
    if len(groupby) > 1:
        index = pd.MultiIndex.from_tuples(names, names=list(groupby))
    else:
        index = pd.Index(names, name=groupby[0])
    return pd.DataFrame(
        np.vstack(rows),
        index=index,
        columns=adata.var["gene_name"].astype(str),
    )


def pseudobulk_by_condition(
    adata: ad.AnnData,
    *,
    layer: str = "X_norm",
) -> pd.DataFrame:
    """Compatibility wrapper for condition-level tutorial baselines."""

    return pseudobulk(adata, groupby=("condition",), layer=layer)
