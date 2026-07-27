---
title: AI → 生物学习路线
summary: 面向机器学习背景读者的六周主学习路径。
level: beginner
prerequisites:
  - Python
  - 基础机器学习
estimated_time: 6 周，每周 5–7 小时
last_reviewed: 2026-07-28
---

# AI → 生物学习路线

目标不是把生物学快速翻译成“token 和 Transformer”，而是学会识别实验单位、测量过程、混杂因素和可验证结论。

## 第 1 周：细胞状态是什么

- 阅读[生物学基础](../01-foundations/index.md)。
- 掌握 DNA、RNA、蛋白、调控、细胞类型、状态和背景。
- 产出：用自己的话解释“RNA 表达不是完整细胞状态”。

## 第 2 周：数据如何产生

- 阅读[单细胞数据基础](../01-foundations/single-cell-basics.md)和[数据版图](../02-data-and-experiments/index.md)。
- 用 Scanpy 打开一个 AnnData，检查 `X`、`obs`、`var` 和 `layers`。
- 产出：为一个数据集画出实验单位、处理、测量和元数据关系。

## 第 3 周：从观测到干预

- 阅读[扰动实验](../02-data-and-experiments/perturbation-experiments.md)。
- 区分 knockout、knockdown、activation、药物、剂量和时间。
- 产出：写出控制组、干预组、目标读数和潜在混杂因素。

## 第 4 周：先做基线

- 阅读[从基线到基础模型](../03-models/baselines-to-foundation-models.md)。
- 完成实践 Notebook 1–4。
- 产出：比较控制均值、平均扰动效应和线性残差模型。

## 第 5 周：模型与泛化

- 阅读[任务版图](../04-tasks/index.md)和[扰动响应预测](../04-tasks/perturbation-prediction.md)。
- 完成轻量 MLP；可选运行 GEARS。
- 产出：明确测试的是新细胞、新扰动还是新背景。

## 第 6 周：评测与研究问题

- 阅读[评测原则](../05-evaluation/index.md)和[数据拆分](../05-evaluation/splits-and-leakage.md)。
- 完成误差分析 Notebook。
- 产出：提出一个可能推翻模型结论的独立验证实验。

## 完成标准

你应能阅读一个 AIVC 项目 README 后，独立找出训练数据、任务定义、数据拆分、基线、指标、实验验证和最危险的外推。
