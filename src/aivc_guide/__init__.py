"""Reusable utilities for the AI Virtual Cell Guide tutorials."""

from .data import (
    REQUIRED_LAYERS,
    REQUIRED_OBS,
    REQUIRED_VAR,
    condition_split,
    load_dataset,
    load_norman,
    make_synthetic_adata,
    pseudobulk,
    pseudobulk_by_condition,
    validate_adata_contract,
)
from .metrics import evaluate_predictions
from .outputs import predictions_to_adata, validate_prediction_contract

__all__ = [
    "REQUIRED_LAYERS",
    "REQUIRED_OBS",
    "REQUIRED_VAR",
    "condition_split",
    "evaluate_predictions",
    "load_dataset",
    "load_norman",
    "make_synthetic_adata",
    "predictions_to_adata",
    "pseudobulk",
    "pseudobulk_by_condition",
    "validate_adata_contract",
    "validate_prediction_contract",
]

__version__ = "0.2.0"
