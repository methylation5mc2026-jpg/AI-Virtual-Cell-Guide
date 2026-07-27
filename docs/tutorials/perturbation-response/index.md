---
title: 扰动响应预测实践
summary: 从实验单位、数据契约和防泄漏拆分走到 CPU 基线、GEARS 与 Arc 官方指标。
level: intermediate
prerequisites:
  - Python
  - 单细胞数据基础
estimated_time: 4–6 小时
last_reviewed: 2026-07-28
---

# 扰动响应预测实践

这条实践线把“预测未见扰动后的细胞状态”拆成可以逐项审计的环节：

![扰动实践工作流](../../assets/experimental-units-and-leakage.svg)

## 两条运行路线

| 路线 | 数据与计算 | 用途 | 证据边界 |
|---|---|---|---|
| 离线六章 | 小型合成 AnnData、CPU | 理解契约、拆分、基线与指标 | 只验证代码和概念 |
| Colab 进阶 | Norman Perturb-seq、GEARS、GPU | 生成细胞级预测并调用 Arc 官方指标 | 短跑不等于论文级复现 |

## 统一契约

AnnData v2 要求：

- `obs.condition`、`obs.cell_type`、`obs.batch`、`obs.replicate`；
- `var.gene_name`；
- `layers.X_norm`；
- `layers.counts` 仅在真正的原始整数计数可用时存在。

条件均值预测输出为单独的 AnnData：每个“条件 × 细胞类型”只有一行，不复制到观测细胞。
Arc 的分布指标只接受真正的细胞级生成结果。

## 建议顺序

先完成左侧导航中的 Notebook 01–06；之后再打开
[GEARS × Norman Colab](notebooks/gears-norman-colab.md)。每一步都保留控制均值和平均效应，
防止复杂模型用规模掩盖没有超过朴素基线的事实。

医学、药物和疾病案例仅作为研究资料，不构成临床或治疗建议。
