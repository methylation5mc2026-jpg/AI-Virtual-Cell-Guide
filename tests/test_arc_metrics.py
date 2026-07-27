from __future__ import annotations

import sys
import types

import pytest

from aivc_guide.arc_metrics import run_vcc_metrics
from aivc_guide.data import make_synthetic_adata
from aivc_guide.outputs import predictions_to_adata
from aivc_guide.workflow import run_experiment


def test_arc_adapter_rejects_condition_means(tmp_path) -> None:
    experiment, predictions, _ = run_experiment(seed=3)
    aggregate = predictions_to_adata(
        predictions["control_mean"],
        cell_type="K562",
        model_name="control_mean",
    )
    with pytest.raises(ValueError, match="cell-level distributions"):
        run_vcc_metrics(aggregate, experiment.test, outdir=tmp_path)


def test_arc_adapter_calls_audited_vcc_profile(tmp_path, monkeypatch) -> None:
    observed = make_synthetic_adata(seed=4)
    predicted = observed.copy()
    predicted.uns["prediction_contract"] = {
        "version": 2,
        "granularity": "generated_cells",
    }
    calls: dict[str, object] = {}

    class FakeEvaluator:
        def __init__(self, **kwargs) -> None:
            calls["init"] = kwargs

        def compute(self, *, profile: str):
            calls["profile"] = profile
            return {"metric": 1.0}, {"aggregate": 1.0}

    fake = types.ModuleType("cell_eval")
    fake.__version__ = "0.8.1"
    fake.MetricsEvaluator = FakeEvaluator
    monkeypatch.setitem(sys.modules, "cell_eval", fake)
    results, aggregate = run_vcc_metrics(predicted, observed, outdir=tmp_path)
    assert calls["profile"] == "vcc"
    assert calls["init"]["control_pert"] == "ctrl"
    assert results["metric"] == 1.0
    assert aggregate["aggregate"] == 1.0
