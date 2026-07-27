---
title: 环境与数据
summary: 安装实践依赖并在合成或 Norman 数据模式间切换。
level: intermediate
prerequisites:
  - Python 3.11（Arc 官方指标）或 Python 3.10+（离线六章）
estimated_time: 20–60 分钟
last_reviewed: 2026-07-28
---

# 环境与数据

## 安装

在仓库根目录创建独立 Python 环境后，安装 Notebook 依赖：

```bash
pip install -e ".[notebooks]"
```

需要 Norman 数据和 GEARS 时：

```bash
pip install -e ".[notebooks,gears]"
```

需要 Arc 官方 VCC 指标时使用 Python 3.11+：

```bash
pip install -e ".[arc]"
```

## 数据模式

Notebook 默认：

```python
DATA_MODE = "synthetic"
```

改为真实数据：

```python
DATA_MODE = "norman"
```

Norman 模式会通过 GEARS 的 `PertData` 加载器获取处理数据。下载位置为本地 `data/`，该目录不会提交到仓库。请同时检查原数据和 GEARS 的许可与引用要求。

## 标准数据契约

加载器输出必须包含：

```text
obs["condition"]
obs["cell_type"]
obs["batch"]
obs["replicate"]
var["gene_name"]
layers["X_norm"]
```

`layers["counts"]` 是可选字段；只有确有非负整数原始计数时才允许出现。验证器会对
缺失字段、空扰动组、重复基因、非有限数值以及伪装成 counts 的处理矩阵给出明确错误。

拆分时，扰动目标彼此不重叠，控制细胞也分配到互不重叠的集合。有足够重复时按
`batch × replicate` 拆分；上游没有重复信息时会发出警告并在 `uns["split_audit"]`
记录退化策略。

## 计算需求

合成模式仅需 CPU 和少量内存。Norman 全数据与 GEARS 训练建议使用 GPU；数据分析和朴素基线可以先用子集或 pseudobulk 在 CPU 上运行。
