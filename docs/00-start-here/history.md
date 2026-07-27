---
title: 发展脉络
summary: 从机理 whole-cell modeling 到数据驱动 AIVC 的概念演进。
level: beginner
prerequisites: []
estimated_time: 15 分钟
last_reviewed: 2026-07-28
---

# 发展脉络

## 机理模型阶段

虚拟细胞并不是生成式 AI 时代才出现的概念。早期工作使用化学反应网络、常微分方程、随机模拟和代谢模型描述特定过程。2012 年 Karr 等人发表首个覆盖一个细菌细胞已知基因功能的 whole-cell model，展示了从基因型到表型的系统模拟可能性，但也暴露出参数获取和跨尺度整合的巨大成本。

## 单细胞图谱阶段

高通量单细胞测序使研究者能够在细胞分辨率观察 RNA、染色质和蛋白等模态。CELLxGENE、Human Cell Atlas、HuBMAP 等项目扩大了“观测状态”的覆盖面；Scanpy、Seurat、scVI 等工具形成较成熟的数据分析栈。

## 单细胞基础模型阶段

Geneformer、scGPT、scFoundation、UCE 等工作尝试从数千万到上亿细胞中预训练通用表征。它们推动了跨数据集迁移、细胞检索和基因网络任务，但也引发了关于预训练收益、简单基线和公平比较的争论。

## 从表征走向状态转换

扰动响应预测将问题从“这是什么细胞”推进到“改变一个基因或加入药物后，细胞会怎样变化”。scGen、CPA、GEARS、STATE 及后续生成模型分别探索条件生成、组合扰动、跨背景转移和分布级预测。

## AIVC 愿景

2024 年的 *Cell* 观点文章把分散的单细胞、成像、分子模型和扰动建模工作统一到 AIVC 愿景中。随后 Arc Virtual Cell Initiative、Virtual Cell Challenge 和 CZI Virtual Cells Platform进一步推动开放数据、模型分发和评测标准。

## 仍未完成的跃迁

今天的大多数系统只覆盖 AIVC 的局部：

- 表达组不是完整细胞；
- 单个时间点不是动态；
- 相关性表征不是机制；
- 同分布测试不是跨背景泛化；
- 排行榜提升不是实验可用性。

因此，本指南把“能否指导独立实验”视为最终判据，而不是把某个模型家族当作终点。

## 代表性来源

- Karr et al. [A whole-cell computational model predicts phenotype from genotype](https://doi.org/10.1016/j.cell.2012.05.044), *Cell*, 2012.
- Regev et al. [The Human Cell Atlas](https://doi.org/10.7554/eLife.27041), *eLife*, 2017.
- Bunne et al. [How to build the virtual cell with artificial intelligence](https://doi.org/10.1016/j.cell.2024.11.015), *Cell*, 2024.
