"""Run the official GEARS Norman pipeline and write auditable cell artifacts."""

from __future__ import annotations

import argparse
import json
import platform
from datetime import UTC, datetime
from pathlib import Path

import anndata as ad
import numpy as np
import pandas as pd
import yaml
from scipy import sparse

from aivc_guide.arc_metrics import CELL_EVAL_VERSION, run_vcc_metrics


def _dense(matrix) -> np.ndarray:
    return matrix.toarray() if sparse.issparse(matrix) else np.asarray(matrix)


def _cell_adata(
    matrix: np.ndarray,
    conditions: np.ndarray,
    genes: np.ndarray,
    *,
    predicted: bool,
) -> ad.AnnData:
    obs = pd.DataFrame(
        {
            "condition": conditions.astype(str),
            "cell_type": "K562",
            "batch": "GEARS_Norman",
            "replicate": "unreported",
        },
        index=[f"{'pred' if predicted else 'real'}_{index:07d}" for index in range(len(matrix))],
    )
    result = ad.AnnData(
        X=sparse.csr_matrix(matrix.astype(np.float32)),
        obs=obs,
        var=pd.DataFrame({"gene_name": genes.astype(str)}, index=genes.astype(str)),
    )
    result.layers["X_norm"] = result.X.copy()
    if predicted:
        result.uns["prediction_contract"] = {
            "version": 2,
            "model_name": "GEARS",
            "granularity": "generated_cells",
            "unit": "GEARS_processed_expression",
            "raw_counts_predicted": False,
        }
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", default="data/gears")
    parser.add_argument("--outdir", default="runs/gears-norman")
    parser.add_argument("--epochs", type=int, default=5)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--device", default=None)
    parser.add_argument("--arc-metrics", action="store_true")
    args = parser.parse_args()

    import torch
    from gears import GEARS, PertData
    from gears.inference import evaluate

    device = args.device or ("cuda:0" if torch.cuda.is_available() else "cpu")
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(args.seed)

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    pert_data = PertData(args.data_dir)
    pert_data.load(data_name="norman")
    pert_data.prepare_split(split="simulation", seed=args.seed)
    pert_data.get_dataloader(batch_size=32, test_batch_size=128)

    model = GEARS(pert_data, device=device)
    model.model_initialize(hidden_size=64)
    model.train(epochs=args.epochs)
    model.save_model(str(outdir / "model"))

    test_res = evaluate(
        pert_data.dataloader["test_loader"],
        model.best_model,
        model.config["uncertainty"],
        model.device,
    )
    genes = pert_data.adata.var["gene_name"].astype(str).to_numpy()
    conditions = np.asarray(test_res["pert_cat"]).astype(str)

    # cell-eval's control-relative metrics need controls in both objects.
    ctrl = pert_data.adata[pert_data.adata.obs["condition"].astype(str) == "ctrl"]
    ctrl_matrix = _dense(ctrl.X)[: min(512, ctrl.n_obs)]
    ctrl_conditions = np.repeat("ctrl", len(ctrl_matrix))
    pred_matrix = np.vstack([ctrl_matrix, np.asarray(test_res["pred"])])
    real_matrix = np.vstack([ctrl_matrix, np.asarray(test_res["truth"])])
    all_conditions = np.concatenate([ctrl_conditions, conditions])

    predicted = _cell_adata(pred_matrix, all_conditions, genes, predicted=True)
    observed = _cell_adata(real_matrix, all_conditions, genes, predicted=False)
    predicted.write_h5ad(outdir / "gears_predicted_cells.h5ad")
    observed.write_h5ad(outdir / "gears_observed_cells.h5ad")

    arc_status: dict[str, object] = {"requested": args.arc_metrics}
    if args.arc_metrics:
        results, aggregate = run_vcc_metrics(
            predicted,
            observed,
            outdir=outdir / "cell-eval",
        )
        arc_status.update(
            {
                "completed": True,
                "cell_eval_version": CELL_EVAL_VERSION,
                "aggregate": json.loads(aggregate.to_json())
                if hasattr(aggregate, "to_json")
                else str(aggregate),
            }
        )

    manifest = {
        "schema_version": 1,
        "run_status": "completed",
        "created_at": datetime.now(UTC).isoformat(),
        "dataset": "Norman Perturb-seq via GEARS",
        "split": "simulation",
        "seed": args.seed,
        "epochs": args.epochs,
        "device": device,
        "python": platform.python_version(),
        "torch": torch.__version__,
        "cell_gears": "0.1.2",
        "arc": arc_status,
        "artifacts": [
            "gears_predicted_cells.h5ad",
            "gears_observed_cells.h5ad",
            "model/",
        ],
        "limitations": [
            "GEARS is a single-cell-type perturbation model.",
            "Norman does not report independent biological replicates in this adapter.",
            "A short smoke run is not a paper-level reproduction.",
        ],
    }
    (outdir / "run-manifest.yml").write_text(
        yaml.safe_dump(manifest, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )
    print(f"Artifacts written to {outdir}")


if __name__ == "__main__":
    main()
