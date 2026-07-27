"""Generate the six offline tutorials and the opt-in GEARS Colab notebook."""

from __future__ import annotations

from pathlib import Path
from textwrap import dedent

import nbformat as nbf

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "notebooks" / "perturbation-response"


def markdown(source: str):
    return nbf.v4.new_markdown_cell(dedent(source).strip())


def code(source: str):
    return nbf.v4.new_code_cell(dedent(source).strip())


def write_notebook(name: str, cells: list) -> None:
    notebook = nbf.v4.new_notebook(
        cells=cells,
        metadata={
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": "3"},
        },
    )
    nbf.write(notebook, TARGET / name)


def build_offline() -> None:
    write_notebook(
        "01-problem-formulation.ipynb",
        [
            markdown(
                """
                # 01｜把生物问题写成机器学习任务

                **目标：**区分观测状态、扰动、对照与反事实结果。这里先用小型合成
                AnnData 验证接口；它不是生物学结论。预测单位是“未见扰动下的细胞状态”，
                划分单位必须是扰动而不是随机细胞。
                """
            ),
            code(
                """
                from aivc_guide.data import make_synthetic_adata, validate_adata_contract

                adata = make_synthetic_adata(seed=42)
                validate_adata_contract(adata, require_counts=True)
                print(adata)
                print(adata.obs.groupby(["condition", "replicate"], observed=True).size())
                """
            ),
            markdown(
                """
                反事实问题是：给定控制状态、细胞背景和一个训练中未出现的扰动，
                预测干预后的表达分布。合成数据只有一个细胞系，不能支持跨细胞类型泛化结论。
                """
            ),
        ],
    )
    write_notebook(
        "02-anndata-qc-and-de.ipynb",
        [
            markdown(
                """
                # 02｜AnnData、QC 与实验单位

                契约 v2 要求 `obs.condition/cell_type/batch/replicate`、
                `var.gene_name` 与 `layers.X_norm`。`layers.counts` 只在确有原始整数计数时存在，
                绝不把处理后的矩阵伪装成 counts。
                """
            ),
            code(
                """
                import numpy as np
                from aivc_guide.data import make_synthetic_adata, pseudobulk

                adata = make_synthetic_adata(seed=42)
                qc = {
                    "cells": adata.n_obs,
                    "genes": adata.n_vars,
                    "counts_available": "counts" in adata.layers,
                    "zero_fraction": float(1 - adata.layers["counts"].nnz / np.prod(adata.shape)),
                }
                qc
                """
            ),
            code(
                """
                replicate_means = pseudobulk(
                    adata,
                    groupby=("condition", "cell_type", "replicate"),
                )
                replicate_means.iloc[:6, :6]
                """
            ),
            markdown(
                """
                差异表达的独立样本应尽量是生物学重复，而不是单个细胞。细胞数很大并不等于
                重复数很大；忽略这一点会产生伪重复（pseudoreplication）。
                """
            ),
        ],
    )
    write_notebook(
        "03-condition-split-and-leakage.ipynb",
        [
            markdown(
                """
                # 03｜按扰动拆分，并审计控制组泄漏

                同一扰动的细胞不能同时进入训练与测试。契约 v2 还把控制细胞分配为不相交集合；
                有足够重复时按 `batch × replicate` 分配，否则明确记录退化为细胞级分配。
                """
            ),
            code(
                """
                from aivc_guide.data import condition_split, make_synthetic_adata

                adata = make_synthetic_adata(seed=42)
                splits = condition_split(adata, seed=42)
                for name, part in splits.items():
                    print(name, part.n_obs, part.uns["split_audit"])
                """
            ),
            code(
                """
                pert_sets = {
                    name: set(part.obs["condition"].astype(str)) - {"ctrl"}
                    for name, part in splits.items()
                }
                ctrl_ids = {
                    name: set(part.obs_names[part.obs["condition"].astype(str) == "ctrl"])
                    for name, part in splits.items()
                }
                assert pert_sets["train"].isdisjoint(pert_sets["test"])
                assert ctrl_ids["train"].isdisjoint(ctrl_ids["test"])
                print("扰动与控制细胞均无跨集合重叠。")
                """
            ),
        ],
    )
    write_notebook(
        "04-naive-baselines.ipynb",
        [
            markdown(
                """
                # 04｜三类 CPU 基线

                依次比较控制均值、平均扰动效应、基因身份 Ridge。后者只使用扰动靶点与
                `var.gene_name` 的显式对应；未知靶点回退到截距，不制造所谓“语义嵌入”。
                """
            ),
            code(
                """
                from aivc_guide.workflow import run_experiment

                experiment, predictions, metrics = run_experiment(
                    seed=42,
                    include_smoke_model=False,
                )
                for name, result in metrics.items():
                    print(name, result["overall"])
                """
            ),
            code(
                """
                assert set(predictions) == {
                    "control_mean",
                    "average_effect",
                    "gene_identity_ridge",
                }
                predictions["gene_identity_ridge"].iloc[:, :8]
                """
            ),
        ],
    )
    write_notebook(
        "05-label-hash-smoke-model.ipynb",
        [
            markdown(
                """
                # 05｜轻量 MLP：仅作接口冒烟测试

                这个 MLP 使用确定性的标签哈希。哈希不包含基因功能、通路或序列信息，因此模型
                正式命名为 `label_hash_smoke_model`，不能当作生物学基线，更不能冒充固定基因嵌入。
                """
            ),
            code(
                """
                from aivc_guide.workflow import run_experiment

                experiment, predictions, metrics = run_experiment(seed=42)
                for name in ("average_effect", "gene_identity_ridge", "label_hash_smoke_model"):
                    print(name, metrics[name]["overall"])
                """
            ),
            markdown(
                """
                若要形成可解释的进阶模型，应把输入替换为有出处并固定版本的基因表示，例如
                序列、调控网络或经独立数据训练的嵌入，并继续与朴素基线同场比较。
                """
            ),
        ],
    )
    write_notebook(
        "06-evaluation-and-arc-mapping.ipynb",
        [
            markdown(
                """
                # 06｜误差分析、预测契约与 Arc 指标映射

                本地 CPU 路径报告 MAE、扰动变化相关性和 Top-DE overlap。Arc 官方
                `cell-eval==0.8.1` 的 `profile="vcc"` 另行用于**细胞级分布预测**；
                条件均值不能复制成许多假细胞去计算分布指标。
                """
            ),
            code(
                """
                from pathlib import Path
                from aivc_guide.outputs import predictions_to_adata, save_metrics
                from aivc_guide.workflow import run_experiment

                experiment, predictions, metrics = run_experiment(seed=42)
                artifact = predictions_to_adata(
                    predictions["gene_identity_ridge"],
                    cell_type="K562",
                    model_name="gene_identity_ridge",
                )
                outdir = Path("aivc-tutorial-output")
                outdir.mkdir(exist_ok=True)
                artifact.write_h5ad(outdir / "predictions.h5ad")
                save_metrics(metrics, outdir / "metrics.json")
                artifact.uns["prediction_contract"]
                """
            ),
            code(
                """
                mapping = {
                    "local_mae": "Arc profile: mae",
                    "local_delta_signal": "Arc profile: discrimination_score_l1 (PDS)",
                    "local_top_de_overlap": "Arc profile: overlap_at_N (DES family)",
                }
                mapping
                """
            ),
            markdown(
                """
                这里的映射用于理解，不声称本地三个简化指标与 Arc 聚合分数数值等价。
                完整 GEARS Colab 会生成细胞级预测，再调用官方
                `MetricsEvaluator.compute(profile="vcc")`。
                """
            ),
        ],
    )


def build_gears_colab() -> None:
    write_notebook(
        "gears-norman-colab.ipynb",
        [
            markdown(
                """
                # GEARS × Norman × Arc 官方指标（Colab GPU）

                [在 Colab 打开](https://colab.research.google.com/github/methylation5mc2026-jpg/AI-Virtual-Cell-Guide/blob/main/notebooks/perturbation-response/gears-norman-colab.ipynb)

                运行前选择 GPU。该流程固定 GEARS 0.1.2、Norman 的 simulation split
                与 `cell-eval==0.8.1`；短跑用于验证复现链路，不等同论文完整复现。
                """
            ),
            code(
                """
                %%capture
                !pip install "cell-gears==0.1.2" "cell-eval==0.8.1" \\
                    "anndata>=0.12.10,<0.13" "PyYAML>=6,<7"
                !git clone -q https://github.com/methylation5mc2026-jpg/AI-Virtual-Cell-Guide.git
                %cd AI-Virtual-Cell-Guide
                !pip install -q -e .
                """
            ),
            code(
                """
                import torch
                assert torch.cuda.is_available(), "请在 Colab 的运行时设置中启用 GPU。"
                print(torch.cuda.get_device_name(0))
                """
            ),
            code(
                """
                !python scripts/run_gears_norman.py \\
                    --data-dir /content/aivc-data \\
                    --outdir /content/aivc-gears-run \\
                    --epochs 5 \\
                    --seed 1 \\
                    --device cuda:0 \\
                    --arc-metrics
                """
            ),
            code(
                """
                from pathlib import Path
                print((Path("/content/aivc-gears-run") / "run-manifest.yml").read_text())
                """
            ),
            markdown(
                """
                下载整个 `/content/aivc-gears-run` 目录作为运行证据。重点核对 manifest、
                两个 H5AD、官方指标输出和模型目录是否同时存在。
                """
            ),
        ],
    )


if __name__ == "__main__":
    TARGET.mkdir(parents=True, exist_ok=True)
    build_offline()
    build_gears_colab()
