"""Versioned prediction artifacts and metric serialization."""

from __future__ import annotations

import json
import warnings
from pathlib import Path

import anndata as ad
import numpy as np
import pandas as pd
from scipy import sparse

PREDICTION_CONTRACT_VERSION = 2


def predictions_to_adata(
    prediction: pd.DataFrame,
    *,
    cell_type: str,
    model_name: str,
) -> ad.AnnData:
    """Serialize one row per condition/cell-type aggregate.

    Contract v2 intentionally does not repeat a condition mean over observed
    cells. Such repetition creates fake sample size and invalid distributional
    metrics.
    """

    if prediction.empty:
        raise ValueError("Prediction table is empty.")
    if prediction.index.astype(str).duplicated().any():
        raise ValueError("Prediction conditions must be unique.")
    if prediction.columns.astype(str).duplicated().any():
        raise ValueError("Prediction genes must be unique.")
    values = prediction.to_numpy(dtype=np.float32)
    if not np.isfinite(values).all():
        raise ValueError("Prediction contains NaN or infinite values.")

    conditions = prediction.index.astype(str)
    genes = prediction.columns.astype(str)
    matrix = sparse.csr_matrix(values)
    obs = pd.DataFrame(
        {
            "condition": conditions.to_numpy(),
            "cell_type": str(cell_type),
            "batch": "prediction",
            "replicate": "aggregate",
        },
        index=pd.Index(
            [f"{model_name}::{condition}::{cell_type}" for condition in conditions],
            name="prediction_id",
        ),
    )
    result = ad.AnnData(
        X=matrix.copy(),
        obs=obs,
        var=pd.DataFrame({"gene_name": genes}, index=genes),
    )
    result.layers["X_norm"] = matrix.copy()
    result.layers["X_pred_norm"] = matrix.copy()
    result.uns["prediction_contract"] = {
        "version": PREDICTION_CONTRACT_VERSION,
        "model_name": model_name,
        "unit": "normalized_log_expression",
        "granularity": "condition_cell_type_mean",
        "raw_counts_predicted": False,
        "repeated_over_observed_cells": False,
    }
    validate_prediction_contract(result)
    return result


def validate_prediction_contract(adata: ad.AnnData) -> None:
    metadata = adata.uns.get("prediction_contract", {})
    if metadata.get("version") != PREDICTION_CONTRACT_VERSION:
        raise ValueError("Prediction artifact is not contract v2.")
    if metadata.get("granularity") != "condition_cell_type_mean":
        raise ValueError("Expected condition/cell-type mean predictions.")
    for field in ("condition", "cell_type"):
        if field not in adata.obs:
            raise ValueError(f"Prediction artifact is missing obs.{field}.")
    if "gene_name" not in adata.var or "X_pred_norm" not in adata.layers:
        raise ValueError("Prediction artifact is missing gene names or X_pred_norm.")
    if "counts" in adata.layers:
        raise ValueError("Mean normalized predictions must not be labelled as raw counts.")
    if adata.obs[["condition", "cell_type"]].duplicated().any():
        raise ValueError("Each condition/cell-type prediction must have one aggregate row.")


def attach_predictions(
    observed: ad.AnnData,
    prediction: pd.DataFrame,
    *,
    layer: str = "X_pred_norm",
) -> ad.AnnData:
    """Compatibility wrapper returning a non-replicated aggregate artifact."""

    warnings.warn(
        "attach_predictions no longer copies means across observed cells; "
        "use predictions_to_adata directly.",
        DeprecationWarning,
        stacklevel=2,
    )
    genes = observed.var["gene_name"].astype(str)
    missing_genes = sorted(set(genes) - set(prediction.columns.astype(str)))
    if missing_genes:
        raise ValueError(f"Prediction is missing genes: {missing_genes[:5]}")
    cell_types = observed.obs["cell_type"].astype(str).unique()
    if len(cell_types) != 1:
        raise ValueError("Compatibility wrapper requires exactly one cell type.")
    result = predictions_to_adata(
        prediction.loc[:, genes],
        cell_type=cell_types[0],
        model_name="unspecified",
    )
    if layer != "X_pred_norm":
        result.layers[layer] = result.layers["X_pred_norm"].copy()
        result.uns["prediction_contract"]["prediction_layer"] = layer
    return result


def save_metrics(metrics: dict, path: str | Path) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(metrics, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return target
