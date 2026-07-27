"""Thin, version-audited adapter for Arc's official cell-eval package."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import anndata as ad

CELL_EVAL_VERSION = "0.8.1"
VCC_PROFILE = "vcc"
VCC_METRICS = ("mae", "discrimination_score_l1", "overlap_at_N")


def _validate_cell_distribution(adata: ad.AnnData, *, role: str, pert_col: str) -> None:
    if pert_col not in adata.obs:
        raise ValueError(f"{role} AnnData is missing obs.{pert_col}.")
    if adata.n_obs <= adata.obs[pert_col].astype(str).nunique():
        raise ValueError(
            f"{role} must contain cell-level distributions, not one mean row "
            "per perturbation."
        )
    if role == "predicted":
        granularity = adata.uns.get("prediction_contract", {}).get("granularity")
        if granularity not in {"generated_cells", "cell_distribution"}:
            raise ValueError(
                "Official VCC metrics require generated cell distributions. "
                "Condition-mean artifacts are intentionally rejected because "
                "repeating means would fabricate sample size."
            )


def run_vcc_metrics(
    predicted_cells: ad.AnnData,
    observed_cells: ad.AnnData,
    *,
    outdir: str | Path,
    pert_col: str = "condition",
    control: str = "ctrl",
    num_threads: int = 4,
) -> tuple[Any, Any]:
    """Run Arc's official v0.8.1 VCC profile on cell-level predictions."""

    _validate_cell_distribution(predicted_cells, role="predicted", pert_col=pert_col)
    _validate_cell_distribution(observed_cells, role="observed", pert_col=pert_col)
    for role, adata in (("predicted", predicted_cells), ("observed", observed_cells)):
        conditions = set(adata.obs[pert_col].astype(str))
        if control not in conditions:
            raise ValueError(f"{role} AnnData is missing control {control!r}.")
    if set(predicted_cells.var_names) != set(observed_cells.var_names):
        raise ValueError("Predicted and observed AnnData must contain the same genes.")

    try:
        import cell_eval
        from cell_eval import MetricsEvaluator
    except ImportError as exc:
        raise RuntimeError(
            "Arc metrics require Python 3.11+ and `pip install -e '.[arc]'`."
        ) from exc
    installed = getattr(cell_eval, "__version__", None)
    if installed and installed != CELL_EVAL_VERSION:
        raise RuntimeError(
            f"Audited cell-eval version is {CELL_EVAL_VERSION}; found {installed}."
        )

    target = Path(outdir)
    target.mkdir(parents=True, exist_ok=True)
    evaluator = MetricsEvaluator(
        adata_pred=predicted_cells,
        adata_real=observed_cells,
        control_pert=control,
        pert_col=pert_col,
        num_threads=num_threads,
        outdir=str(target),
    )
    return evaluator.compute(profile=VCC_PROFILE)
