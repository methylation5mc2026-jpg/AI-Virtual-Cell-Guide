"""Evaluation metrics for perturbation-response predictions."""

from __future__ import annotations

import numpy as np
import pandas as pd


def _aligned(
    prediction: pd.DataFrame,
    truth: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    missing_conditions = sorted(set(truth.index) - set(prediction.index))
    missing_genes = sorted(set(truth.columns) - set(prediction.columns))
    if missing_conditions:
        raise ValueError(f"Missing predicted conditions: {missing_conditions}")
    if missing_genes:
        raise ValueError(f"Missing predicted genes: {missing_genes[:5]}")
    return prediction.loc[truth.index, truth.columns], truth


def _safe_pearson(left: np.ndarray, right: np.ndarray) -> float:
    if left.size < 2 or np.std(left) == 0 or np.std(right) == 0:
        return 0.0
    value = float(np.corrcoef(left, right)[0, 1])
    return value if np.isfinite(value) else 0.0


def top_de_overlap(
    prediction_delta: np.ndarray,
    truth_delta: np.ndarray,
    *,
    k: int = 20,
) -> float:
    top_k = min(k, prediction_delta.size)
    pred_top = set(np.argsort(np.abs(prediction_delta))[-top_k:])
    true_top = set(np.argsort(np.abs(truth_delta))[-top_k:])
    return len(pred_top & true_top) / top_k if top_k else 0.0


def evaluate_predictions(
    prediction: pd.DataFrame,
    truth: pd.DataFrame,
    control_mean: pd.Series,
    *,
    top_k: int = 20,
) -> dict:
    """Evaluate absolute expression and perturbation-induced changes."""

    prediction, truth = _aligned(prediction, truth)
    control = control_mean.loc[truth.columns].to_numpy()
    per_condition: dict[str, dict[str, float]] = {}
    for condition in truth.index:
        pred_values = prediction.loc[condition].to_numpy(dtype=float)
        true_values = truth.loc[condition].to_numpy(dtype=float)
        pred_delta = pred_values - control
        true_delta = true_values - control
        per_condition[str(condition)] = {
            "mae": float(np.mean(np.abs(pred_values - true_values))),
            "delta_pearson": _safe_pearson(pred_delta, true_delta),
            "top_de_overlap": top_de_overlap(pred_delta, true_delta, k=top_k),
        }
    keys = ("mae", "delta_pearson", "top_de_overlap")
    overall = {
        key: float(np.mean([metrics[key] for metrics in per_condition.values()]))
        for key in keys
    }
    return {
        "overall": overall,
        "per_condition": per_condition,
        "metric_notes": {
            "mae": "Mean absolute error on normalized expression.",
            "delta_pearson": "Pearson correlation after subtracting the control mean.",
            "top_de_overlap": f"Overlap fraction among the top {top_k} absolute changes.",
        },
    }
