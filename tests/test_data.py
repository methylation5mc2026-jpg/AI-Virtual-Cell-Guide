from __future__ import annotations

import sys
import types

import numpy as np
import pytest
from scipy import sparse

from aivc_guide.data import (
    condition_split,
    load_dataset,
    load_norman,
    make_synthetic_adata,
    pseudobulk,
    pseudobulk_by_condition,
    validate_adata_contract,
)


def test_synthetic_contract_is_sparse_and_deterministic() -> None:
    first = make_synthetic_adata(seed=7)
    second = make_synthetic_adata(seed=7)
    validate_adata_contract(first)
    assert sparse.issparse(first.layers["counts"])
    assert sparse.issparse(first.layers["X_norm"])
    assert (first.layers["counts"] != second.layers["counts"]).nnz == 0


def test_contract_reports_missing_metadata_and_empty_groups() -> None:
    adata = make_synthetic_adata()
    del adata.obs["replicate"]
    with pytest.raises(ValueError, match="Missing obs fields"):
        validate_adata_contract(adata)

    adata = make_synthetic_adata()
    adata.obs.loc[adata.obs_names[0], "condition"] = ""
    with pytest.raises(ValueError, match="empty"):
        validate_adata_contract(adata)


def test_contract_reports_unknown_or_duplicate_gene_metadata() -> None:
    adata = make_synthetic_adata()
    adata.var.iloc[1, adata.var.columns.get_loc("gene_name")] = adata.var.iloc[0]["gene_name"]
    with pytest.raises(ValueError, match="unique"):
        validate_adata_contract(adata)

    adata = make_synthetic_adata()
    with pytest.raises(ValueError, match="Unknown"):
        validate_adata_contract(adata, expected_genes=["gene_000", "NOT_IN_DATA"])


def test_contract_reports_a_planned_but_empty_perturbation_group() -> None:
    adata = make_synthetic_adata()
    with pytest.raises(ValueError, match="no cells"):
        validate_adata_contract(
            adata,
            expected_conditions=["ctrl", "gene_000", "GENE_WITH_ZERO_CELLS"],
        )


def test_condition_split_prevents_perturbation_leakage() -> None:
    splits = condition_split(make_synthetic_adata(), seed=3)
    sets = {
        name: set(part.obs["condition"].astype(str)) - {"ctrl"}
        for name, part in splits.items()
    }
    assert sets["train"].isdisjoint(sets["val"])
    assert sets["train"].isdisjoint(sets["test"])
    assert sets["val"].isdisjoint(sets["test"])
    assert all("ctrl" in set(part.obs["condition"].astype(str)) for part in splits.values())
    control_ids = {
        name: set(part.obs_names[part.obs["condition"].astype(str) == "ctrl"])
        for name, part in splits.items()
    }
    assert control_ids["train"].isdisjoint(control_ids["val"])
    assert control_ids["train"].isdisjoint(control_ids["test"])
    assert control_ids["val"].isdisjoint(control_ids["test"])


def test_batch_imbalance_and_pseudobulk_are_supported() -> None:
    adata = make_synthetic_adata(
        n_per_condition={
            "ctrl": 80,
            "gene_000": 12,
            "gene_006": 25,
            "gene_012": 9,
            "gene_018": 31,
        }
    )
    means = pseudobulk_by_condition(adata)
    assert means.shape == (5, adata.n_vars)
    assert np.isfinite(means.to_numpy()).all()
    replicate_means = pseudobulk(
        adata, groupby=("condition", "cell_type", "replicate")
    )
    assert replicate_means.index.nlevels == 3


def test_counts_are_optional_but_cannot_be_processed_expression() -> None:
    adata = make_synthetic_adata()
    del adata.layers["counts"]
    validate_adata_contract(adata)
    with pytest.raises(ValueError, match="required"):
        validate_adata_contract(adata, require_counts=True)

    adata = make_synthetic_adata()
    adata.layers["counts"] = adata.layers["X_norm"].copy()
    with pytest.raises(ValueError, match="integer-like"):
        validate_adata_contract(adata)


def test_invalid_mode_and_download_failure_are_actionable(tmp_path, monkeypatch) -> None:
    with pytest.raises(ValueError, match="synthetic"):
        load_dataset("not-a-mode")

    fake_gears = types.ModuleType("gears")

    class BrokenPertData:
        def __init__(self, _: str) -> None:
            pass

        def load(self, *, data_name: str) -> None:
            raise OSError(f"cannot fetch {data_name}")

    fake_gears.PertData = BrokenPertData
    monkeypatch.setitem(sys.modules, "gears", fake_gears)
    with pytest.raises(RuntimeError, match="Unable to load"):
        load_norman(tmp_path)
