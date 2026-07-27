---
title: 01-problem-formulation
hide:
  - toc
---

<div class="notebook-actions" markdown>
[查看源 Notebook](https://github.com/methylation5mc2026-jpg/AI-Virtual-Cell-Guide/blob/main/notebooks/perturbation-response/01-problem-formulation.ipynb){ .md-button }
[在 Colab 打开](https://colab.research.google.com/github/methylation5mc2026-jpg/AI-Virtual-Cell-Guide/blob/main/notebooks/perturbation-response/01-problem-formulation.ipynb){ .md-button .md-button--primary }
</div>

!!! note "在线渲染说明"
    本页由源 Notebook 自动生成。代码输出以实际运行为准；普通合并只执行离线六章，
    GEARS 页面需在 Colab GPU 中按运行清单复现。

# 01｜把生物问题写成机器学习任务

**目标：**区分观测状态、扰动、对照与反事实结果。这里先用小型合成
AnnData 验证接口；它不是生物学结论。预测单位是“未见扰动下的细胞状态”，
划分单位必须是扰动而不是随机细胞。

```python
from aivc_guide.data import make_synthetic_adata, validate_adata_contract

adata = make_synthetic_adata(seed=42)
validate_adata_contract(adata, require_counts=True)
print(adata)
print(adata.obs.groupby(["condition", "replicate"], observed=True).size())
```

反事实问题是：给定控制状态、细胞背景和一个训练中未出现的扰动，
预测干预后的表达分布。合成数据只有一个细胞系，不能支持跨细胞类型泛化结论。
