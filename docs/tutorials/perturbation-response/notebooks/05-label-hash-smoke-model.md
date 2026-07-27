---
title: 05-label-hash-smoke-model
hide:
  - toc
---

<div class="notebook-actions" markdown>
[查看源 Notebook](https://github.com/methylation5mc2026-jpg/AI-Virtual-Cell-Guide/blob/main/notebooks/perturbation-response/05-label-hash-smoke-model.ipynb){ .md-button }
[在 Colab 打开](https://colab.research.google.com/github/methylation5mc2026-jpg/AI-Virtual-Cell-Guide/blob/main/notebooks/perturbation-response/05-label-hash-smoke-model.ipynb){ .md-button .md-button--primary }
</div>

!!! note "在线渲染说明"
    本页由源 Notebook 自动生成。代码输出以实际运行为准；普通合并只执行离线六章，
    GEARS 页面需在 Colab GPU 中按运行清单复现。

# 05｜轻量 MLP：仅作接口冒烟测试

这个 MLP 使用确定性的标签哈希。哈希不包含基因功能、通路或序列信息，因此模型
正式命名为 `label_hash_smoke_model`，不能当作生物学基线，更不能冒充固定基因嵌入。

```python
from aivc_guide.workflow import run_experiment

experiment, predictions, metrics = run_experiment(seed=42)
for name in ("average_effect", "gene_identity_ridge", "label_hash_smoke_model"):
    print(name, metrics[name]["overall"])
```

若要形成可解释的进阶模型，应把输入替换为有出处并固定版本的基因表示，例如
序列、调控网络或经独立数据训练的嵌入，并继续与朴素基线同场比较。
