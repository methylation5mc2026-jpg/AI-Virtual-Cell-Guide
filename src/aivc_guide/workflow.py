"""End-to-end helpers shared by the six tutorial notebooks."""

from __future__ import annotations

from dataclasses import dataclass

import anndata as ad
import pandas as pd

from .baselines import (
    AverageEffectBaseline,
    ControlMeanBaseline,
    GeneIdentityRidgeBaseline,
    LabelHashSmokeModel,
)
from .data import condition_split, load_dataset, pseudobulk_by_condition
from .metrics import evaluate_predictions


@dataclass
class Experiment:
    train: ad.AnnData
    validation: ad.AnnData
    test: ad.AnnData
    test_conditions: list[str]
    truth: pd.DataFrame
    control_mean: pd.Series


def prepare_experiment(mode: str = "synthetic", *, seed: int = 42) -> Experiment:
    adata = load_dataset(mode=mode, seed=seed)
    splits = condition_split(adata, seed=seed)
    test_means = pseudobulk_by_condition(splits["test"])
    test_conditions = [name for name in test_means.index if name != "ctrl"]
    train_means = pseudobulk_by_condition(splits["train"])
    return Experiment(
        train=splits["train"],
        validation=splits["val"],
        test=splits["test"],
        test_conditions=test_conditions,
        truth=test_means.loc[test_conditions],
        control_mean=train_means.loc["ctrl"],
    )


def fitted_models(experiment: Experiment, *, include_smoke_model: bool = True) -> dict:
    models = [
        ControlMeanBaseline(),
        AverageEffectBaseline(),
        GeneIdentityRidgeBaseline(),
    ]
    if include_smoke_model:
        models.append(LabelHashSmokeModel())
    return {model.name: model.fit(experiment.train) for model in models}


def run_experiment(
    mode: str = "synthetic",
    *,
    seed: int = 42,
    include_smoke_model: bool = True,
) -> tuple[Experiment, dict[str, pd.DataFrame], dict[str, dict]]:
    experiment = prepare_experiment(mode=mode, seed=seed)
    models = fitted_models(experiment, include_smoke_model=include_smoke_model)
    predictions = {
        name: model.predict(experiment.test_conditions) for name, model in models.items()
    }
    metrics = {
        name: evaluate_predictions(
            prediction,
            experiment.truth,
            experiment.control_mean,
        )
        for name, prediction in predictions.items()
    }
    return experiment, predictions, metrics
