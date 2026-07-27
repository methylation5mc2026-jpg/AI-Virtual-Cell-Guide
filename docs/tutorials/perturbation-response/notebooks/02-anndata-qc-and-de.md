---
title: 02-anndata-qc-and-de
hide:
  - toc
---

<div class="notebook-actions" markdown>
[查看源 Notebook](https://github.com/methylation5mc2026-jpg/AI-Virtual-Cell-Guide/blob/main/notebooks/perturbation-response/02-anndata-qc-and-de.ipynb){ .md-button }
[在 Colab 打开](https://colab.research.google.com/github/methylation5mc2026-jpg/AI-Virtual-Cell-Guide/blob/main/notebooks/perturbation-response/02-anndata-qc-and-de.ipynb){ .md-button .md-button--primary }
</div>

!!! note "在线渲染说明"
    本页由源 Notebook 自动生成。代码输出以实际运行为准；普通合并只执行离线六章，
    GEARS 页面需在 Colab GPU 中按运行清单复现。

# 02｜AnnData、QC 与实验单位

契约 v2 要求 `obs.condition/cell_type/batch/replicate`、
`var.gene_name` 与 `layers.X_norm`。`layers.counts` 只在确有原始整数计数时存在，
绝不把处理后的矩阵伪装成 counts。

```python
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
```

```python
replicate_means = pseudobulk(
    adata,
    groupby=("condition", "cell_type", "replicate"),
)
replicate_means.iloc[:6, :6]
```

差异表达的独立样本应尽量是生物学重复，而不是单个细胞。细胞数很大并不等于
重复数很大；忽略这一点会产生伪重复（pseudoreplication）。
