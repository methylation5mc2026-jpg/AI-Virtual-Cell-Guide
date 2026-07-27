---
title: 03-condition-split-and-leakage
hide:
  - toc
---

<div class="notebook-actions" markdown>
[查看源 Notebook](https://github.com/methylation5mc2026-jpg/AI-Virtual-Cell-Guide/blob/main/notebooks/perturbation-response/03-condition-split-and-leakage.ipynb){ .md-button }
[在 Colab 打开](https://colab.research.google.com/github/methylation5mc2026-jpg/AI-Virtual-Cell-Guide/blob/main/notebooks/perturbation-response/03-condition-split-and-leakage.ipynb){ .md-button .md-button--primary }
</div>

!!! note "在线渲染说明"
    本页由源 Notebook 自动生成。代码输出以实际运行为准；普通合并只执行离线六章，
    GEARS 页面需在 Colab GPU 中按运行清单复现。

# 03｜按扰动拆分，并审计控制组泄漏

同一扰动的细胞不能同时进入训练与测试。契约 v2 还把控制细胞分配为不相交集合；
有足够重复时按 `batch × replicate` 分配，否则明确记录退化为细胞级分配。

```python
from aivc_guide.data import condition_split, make_synthetic_adata

adata = make_synthetic_adata(seed=42)
splits = condition_split(adata, seed=42)
for name, part in splits.items():
    print(name, part.n_obs, part.uns["split_audit"])
```

```python
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
```
