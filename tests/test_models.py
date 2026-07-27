from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from aivc_guide.baselines import GeneIdentityRidgeBaseline, LabelHashSmokeModel
from aivc_guide.outputs import (
    predictions_to_adata,
    save_metrics,
    validate_prediction_contract,
)
from aivc_guide.workflow import prepare_experiment, run_experiment

FIXTURE = Path(__file__).parent / "fixtures" / "expected_metrics.json"


def test_all_models_run_without_gpu_and_return_finite_metrics() -> None:
    experiment, predictions, metrics = run_experiment("synthetic", seed=42)
    assert set(predictions) == {
        "control_mean",
        "average_effect",
        "gene_identity_ridge",
        "label_hash_smoke_model",
    }
    for result in metrics.values():
        assert all(np.isfinite(value) for value in result["overall"].values())
        assert 0 <= result["overall"]["top_de_overlap"] <= 1
    assert predictions["control_mean"].shape == experiment.truth.shape


def test_seeded_metrics_remain_within_recorded_tolerance() -> None:
    expected = json.loads(FIXTURE.read_text(encoding="utf-8"))
    _, _, actual = run_experiment("synthetic", seed=expected["seed"])
    for model_name, model_expected in expected["models"].items():
        for metric_name, expected_value in model_expected.items():
            actual_value = actual[model_name]["overall"][metric_name]
            tolerance = expected["tolerance"][metric_name]
            assert abs(actual_value - expected_value) <= tolerance


def test_unseen_perturbation_name_has_a_prediction() -> None:
    experiment = prepare_experiment(seed=10)
    for model in (GeneIdentityRidgeBaseline(), LabelHashSmokeModel()):
        prediction = model.fit(experiment.train).predict(["UNKNOWN_GENE"])
        assert prediction.shape == (1, experiment.train.n_vars)
        assert np.isfinite(prediction.to_numpy()).all()


def test_prediction_artifacts_do_not_repeat_condition_means(tmp_path) -> None:
    experiment, predictions, metrics = run_experiment(seed=11)
    result = predictions_to_adata(
        predictions["control_mean"],
        cell_type="K562",
        model_name="control_mean",
    )
    validate_prediction_contract(result)
    assert result.n_obs == len(experiment.test_conditions)
    assert "counts" not in result.layers
    assert "X_norm" in result.layers
    assert "X_pred_norm" in result.layers
    assert result.uns["prediction_contract"]["repeated_over_observed_cells"] is False
    target = save_metrics(metrics, tmp_path / "metrics.json")
    payload = json.loads(target.read_text(encoding="utf-8"))
    assert "control_mean" in payload
