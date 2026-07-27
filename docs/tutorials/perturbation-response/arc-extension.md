---
title: Arc 挑战扩展
summary: 把入门实践迁移到 Arc Virtual Cell Challenge 数据与指标。
level: advanced
prerequisites:
  - 完成六个实践 Notebook
estimated_time: 1–3 天
last_reviewed: 2026-07-28
---

# Arc 挑战扩展

[Arc Virtual Cell Challenge 2025](https://github.com/ArcInstitute/arc-virtual-cell-atlas/tree/main/virtual-cell-challenge)提供 H1 人胚胎干细胞 CRISPRi 数据，包含训练、验证和测试扰动以及 Python/R 数据访问教程。

## 迁移步骤

1. 使用官方教程访问固定版本的 `h5ad`；
2. 将扰动字段映射到本项目 AnnData 契约；
3. 保留官方按扰动划分的训练、验证和测试集合；
4. 先复现控制均值和 pseudobulk 基线；
5. 再迁移岭回归、MLP 或状态转换模型；
6. 使用固定的官方 `cell-eval==0.8.1`，调用
   `MetricsEvaluator.compute(profile="vcc")`；
7. 同时报告 DES、PDS、MAE 和失败扰动。

## 三个指标的解释

- DES：恢复正确差异表达基因集合；
- PDS：预测是否最接近对应真实扰动，而不是其他扰动；
- MAE：全基因表达的绝对误差。

当前官方 `vcc` profile 对应 `mae`、`discrimination_score_l1` 和
`overlap_at_N`。本项目的简化 MAE、变化相关性和 Top-DE overlap 只用于 CPU 教学，
不冒充官方分数。

!!! warning "不要制造预测分布"
    Arc 路径要求细胞级预测。把一个条件均值重复成许多行会制造虚假样本量，并使
    分布型指标失真；本项目适配器会主动拒绝这种输入。

## 已审计运行入口

- [GEARS × Norman Colab](notebooks/gears-norman-colab.md)
- [`scripts/run_gears_norman.py`](https://github.com/methylation5mc2026-jpg/AI-Virtual-Cell-Guide/blob/main/scripts/run_gears_norman.py)
- [Arc cell-eval v0.8.1](https://github.com/ArcInstitute/cell-eval/releases/tag/v0.8.1)

## 不要直接照搬排行榜策略

2025 官方复盘显示，模型可通过缩放、pseudobulk 或针对权重优化改善某些指标，但这不一定提高跨指标和生物学泛化。扩展实验必须保留朴素基线，并增加表达变化相关、Top-DE 方向和跨数据背景分析。

## 建议研究问题

- 训练于 K562/A375 等背景的模型能否迁移到 H1？
- 蛋白或通路 embedding 的增益来自生物先验还是目标相似度？
- 平均状态预测与分布生成在不同指标上如何权衡？
- 不确定性是否能识别弱扰动和 OOD 目标？
