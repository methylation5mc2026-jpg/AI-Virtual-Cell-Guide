---
title: 06-evaluation-and-arc-mapping
hide:
  - toc
---

<div class="notebook-actions" markdown>
[查看源 Notebook](https://github.com/methylation5mc2026-jpg/AI-Virtual-Cell-Guide/blob/main/notebooks/perturbation-response/06-evaluation-and-arc-mapping.ipynb){ .md-button }
[在 Colab 打开](https://colab.research.google.com/github/methylation5mc2026-jpg/AI-Virtual-Cell-Guide/blob/main/notebooks/perturbation-response/06-evaluation-and-arc-mapping.ipynb){ .md-button .md-button--primary }
</div>

!!! note "在线渲染说明"
    本页由源 Notebook 自动生成。代码输出以实际运行为准；普通合并只执行离线六章，
    GEARS 页面需在 Colab GPU 中按运行清单复现。

# 06｜误差分析、预测契约与 Arc 指标映射

本地 CPU 路径报告 MAE、扰动变化相关性和 Top-DE overlap。Arc 官方
`cell-eval==0.8.1` 的 `profile="vcc"` 另行用于**细胞级分布预测**；
条件均值不能复制成许多假细胞去计算分布指标。

```python
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
```

```python
mapping = {
    "local_mae": "Arc profile: mae",
    "local_delta_signal": "Arc profile: discrimination_score_l1 (PDS)",
    "local_top_de_overlap": "Arc profile: overlap_at_N (DES family)",
}
mapping
```

这里的映射用于理解，不声称本地三个简化指标与 Arc 聚合分数数值等价。
完整 GEARS Colab 会生成细胞级预测，再调用官方
`MetricsEvaluator.compute(profile="vcc")`。
