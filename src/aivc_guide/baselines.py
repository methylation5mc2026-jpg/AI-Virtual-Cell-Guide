"""Transparent perturbation baselines plus one explicitly labelled smoke model."""

from __future__ import annotations

import hashlib
from collections.abc import Iterable
from dataclasses import dataclass

import anndata as ad
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.neural_network import MLPRegressor

from .data import CONTROL_CONDITION, pseudobulk_by_condition, validate_adata_contract


def _condition_embedding(condition: str, dimension: int = 32) -> np.ndarray:
    """Hash a label for interface testing, not for biological representation."""

    tokens = [
        token.strip()
        for token in condition.replace(",", "+").split("+")
        if token.strip() and token.strip().lower() not in {"ctrl", "control"}
    ]
    vector = np.zeros(dimension, dtype=np.float64)
    for token in tokens or [condition]:
        digest = hashlib.sha256(token.encode("utf-8")).digest()
        raw = np.frombuffer(digest, dtype=np.uint8).astype(np.float64)
        raw = np.resize(raw, dimension)
        vector += (raw - 127.5) / 127.5
    norm = np.linalg.norm(vector)
    return vector / norm if norm else vector


@dataclass
class _FittedState:
    control: pd.Series
    genes: pd.Index


class ControlMeanBaseline:
    """Predict the mean expression of control cells for every perturbation."""

    name = "control_mean"

    def fit(self, adata: ad.AnnData) -> ControlMeanBaseline:
        validate_adata_contract(adata)
        means = pseudobulk_by_condition(adata)
        self.state_ = _FittedState(means.loc[CONTROL_CONDITION], means.columns)
        return self

    def predict(self, conditions: Iterable[str]) -> pd.DataFrame:
        state = self._check_fitted()
        names = list(conditions)
        matrix = np.repeat(state.control.to_numpy()[None, :], len(names), axis=0)
        return pd.DataFrame(matrix, index=names, columns=state.genes)

    def _check_fitted(self) -> _FittedState:
        if not hasattr(self, "state_"):
            raise RuntimeError("Fit the baseline before prediction.")
        return self.state_


class AverageEffectBaseline(ControlMeanBaseline):
    """Add the average training-set perturbation delta to the control mean."""

    name = "average_effect"

    def fit(self, adata: ad.AnnData) -> AverageEffectBaseline:
        super().fit(adata)
        means = pseudobulk_by_condition(adata)
        perturbations = means.drop(index=CONTROL_CONDITION, errors="ignore")
        if perturbations.empty:
            raise ValueError("AverageEffectBaseline requires a training perturbation.")
        self.average_delta_ = perturbations.sub(self.state_.control, axis=1).mean(axis=0)
        return self

    def predict(self, conditions: Iterable[str]) -> pd.DataFrame:
        state = self._check_fitted()
        names = list(conditions)
        prediction = np.clip(state.control.to_numpy() + self.average_delta_.to_numpy(), 0, None)
        matrix = np.repeat(prediction[None, :], len(names), axis=0)
        return pd.DataFrame(matrix, index=names, columns=state.genes)


class RidgeResidualBaseline(ControlMeanBaseline):
    """Deprecated alias retained for notebooks created before contract v2."""

    name = "gene_identity_ridge"

    def __init__(self, *, alpha: float = 10.0) -> None:
        self.alpha = alpha

    def fit(self, adata: ad.AnnData) -> RidgeResidualBaseline:
        super().fit(adata)
        means = pseudobulk_by_condition(adata)
        perturbations = means.drop(index=CONTROL_CONDITION, errors="ignore")
        if perturbations.empty:
            raise ValueError("RidgeResidualBaseline requires a training perturbation.")
        self.gene_lookup_ = {
            gene.casefold(): index
            for index, gene in enumerate(self.state_.genes.astype(str))
        }
        x_train = np.vstack([self._encode(name) for name in perturbations.index])
        y_train = perturbations.sub(self.state_.control, axis=1).to_numpy()
        self.regressor_ = Ridge(alpha=self.alpha).fit(x_train, y_train)
        return self

    def _encode(self, condition: str) -> np.ndarray:
        vector = np.zeros(len(self.state_.genes), dtype=np.float64)
        tokens = condition.replace(",", "+").split("+")
        for token in tokens:
            index = self.gene_lookup_.get(token.strip().casefold())
            if index is not None:
                vector[index] = 1.0
        return vector

    def predict(self, conditions: Iterable[str]) -> pd.DataFrame:
        state = self._check_fitted()
        names = list(conditions)
        x_test = np.vstack([self._encode(name) for name in names])
        delta = self.regressor_.predict(x_test)
        prediction = np.clip(state.control.to_numpy()[None, :] + delta, 0, None)
        return pd.DataFrame(prediction, index=names, columns=state.genes)


class GeneIdentityRidgeBaseline(RidgeResidualBaseline):
    """Map observed perturbation target identities to expression residuals.

    Target genes are encoded as explicit one-hot vectors against
    ``var.gene_name``. An unseen or unknown target therefore falls back to the
    learned intercept instead of receiving a fabricated semantic embedding.
    """

    name = "gene_identity_ridge"


class LabelHashSmokeModel(ControlMeanBaseline):
    """CPU interface smoke test over deterministic label hashes.

    The representation contains no biological knowledge and this model must
    not be presented as a scientific baseline or foundation-model surrogate.
    """

    name = "label_hash_smoke_model"

    def __init__(
        self,
        *,
        embedding_dim: int = 32,
        hidden_units: int = 32,
        alpha: float = 10.0,
        random_state: int = 42,
    ) -> None:
        self.embedding_dim = embedding_dim
        self.hidden_units = hidden_units
        self.alpha = alpha
        self.random_state = random_state

    def fit(self, adata: ad.AnnData) -> LabelHashSmokeModel:
        super().fit(adata)
        means = pseudobulk_by_condition(adata)
        perturbations = means.drop(index=CONTROL_CONDITION, errors="ignore")
        if perturbations.empty:
            raise ValueError("LabelHashSmokeModel requires a training perturbation.")
        x_train = np.vstack(
            [_condition_embedding(name, self.embedding_dim) for name in perturbations.index]
        )
        y_train = perturbations.sub(self.state_.control, axis=1).to_numpy()
        self.regressor_ = MLPRegressor(
            hidden_layer_sizes=(self.hidden_units,),
            activation="tanh",
            solver="lbfgs",
            alpha=self.alpha,
            max_iter=2_000,
            max_fun=50_000,
            tol=1e-3,
            random_state=self.random_state,
        ).fit(x_train, y_train)
        return self

    def predict(self, conditions: Iterable[str]) -> pd.DataFrame:
        state = self._check_fitted()
        names = list(conditions)
        x_test = np.vstack([_condition_embedding(name, self.embedding_dim) for name in names])
        delta = self.regressor_.predict(x_test)
        prediction = np.clip(state.control.to_numpy()[None, :] + delta, 0, None)
        return pd.DataFrame(prediction, index=names, columns=state.genes)


# Backward-compatible import name; public documentation uses the honest name.
MLPResidualModel = LabelHashSmokeModel
