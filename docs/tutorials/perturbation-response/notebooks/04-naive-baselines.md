---
title: 04-naive-baselines
hide:
  - toc
---

<div class="notebook-actions" markdown>
[查看源 Notebook](https://github.com/methylation5mc2026-jpg/AI-Virtual-Cell-Guide/blob/main/notebooks/perturbation-response/04-naive-baselines.ipynb){ .md-button }
[在 Colab 打开](https://colab.research.google.com/github/methylation5mc2026-jpg/AI-Virtual-Cell-Guide/blob/main/notebooks/perturbation-response/04-naive-baselines.ipynb){ .md-button .md-button--primary }
</div>

!!! note "在线渲染说明"
    本页由源 Notebook 自动生成。代码输出以实际运行为准；普通合并只执行离线六章，
    GEARS 页面需在 Colab GPU 中按运行清单复现。

# 04｜三类 CPU 基线

依次比较控制均值、平均扰动效应、基因身份 Ridge。后者只使用扰动靶点与
`var.gene_name` 的显式对应；未知靶点回退到截距，不制造所谓“语义嵌入”。

```python
from aivc_guide.workflow import run_experiment

experiment, predictions, metrics = run_experiment(
    seed=42,
    include_smoke_model=False,
)
for name, result in metrics.items():
    print(name, result["overall"])
```

```python
assert set(predictions) == {
    "control_mean",
    "average_effect",
    "gene_identity_ridge",
}
predictions["gene_identity_ridge"].iloc[:, :8]
```
