---
title: gears-norman-colab
hide:
  - toc
---

<div class="notebook-actions" markdown>
[查看源 Notebook](https://github.com/methylation5mc2026-jpg/AI-Virtual-Cell-Guide/blob/main/notebooks/perturbation-response/gears-norman-colab.ipynb){ .md-button }
[在 Colab 打开](https://colab.research.google.com/github/methylation5mc2026-jpg/AI-Virtual-Cell-Guide/blob/main/notebooks/perturbation-response/gears-norman-colab.ipynb){ .md-button .md-button--primary }
</div>

!!! note "在线渲染说明"
    本页由源 Notebook 自动生成。代码输出以实际运行为准；普通合并只执行离线六章，
    GEARS 页面需在 Colab GPU 中按运行清单复现。

# GEARS × Norman × Arc 官方指标（Colab GPU）

[在 Colab 打开](https://colab.research.google.com/github/methylation5mc2026-jpg/AI-Virtual-Cell-Guide/blob/main/notebooks/perturbation-response/gears-norman-colab.ipynb)

运行前选择 GPU。该流程固定 GEARS 0.1.2、Norman 的 simulation split
与 `cell-eval==0.8.1`；短跑用于验证复现链路，不等同论文完整复现。

```python
%%capture
!pip install "cell-gears==0.1.2" "cell-eval==0.8.1" \
    "anndata>=0.12.10,<0.13" "PyYAML>=6,<7"
!git clone -q https://github.com/methylation5mc2026-jpg/AI-Virtual-Cell-Guide.git
%cd AI-Virtual-Cell-Guide
!pip install -q -e .
```

```python
import torch
assert torch.cuda.is_available(), "请在 Colab 的运行时设置中启用 GPU。"
print(torch.cuda.get_device_name(0))
```

```python
!python scripts/run_gears_norman.py \
    --data-dir /content/aivc-data \
    --outdir /content/aivc-gears-run \
    --epochs 5 \
    --seed 1 \
    --device cuda:0 \
    --arc-metrics
```

```python
from pathlib import Path
print((Path("/content/aivc-gears-run") / "run-manifest.yml").read_text())
```

下载整个 `/content/aivc-gears-run` 目录作为运行证据。重点核对 manifest、
两个 H5AD、官方指标输出和模型目录是否同时存在。
