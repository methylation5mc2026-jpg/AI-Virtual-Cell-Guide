---
title: 复现审计
summary: 数据、代码、指标、运行证据和未完成项的公开记录。
last_reviewed: 2026-07-28
---

# 复现审计

## 审计结论

离线六章已纳入 CPU CI，覆盖 AnnData 契约、稀疏矩阵、缺失 counts、未知基因、
空扰动、批次不平衡、无 GPU 和下载失败。Norman × GEARS 的 GPU 路径已按官方 API
实现，并固定 Arc `cell-eval==0.8.1`；首个公开 Colab GPU 实跑仍需产生外部运行证据，
因此不把“代码已就绪”写成“结果已复现”。

## 可追溯链路

| 层 | 固定内容 | 验收证据 |
|---|---|---|
| 数据 | Norman，通过 `PertData.load(data_name="norman")` 获取 | 上游下载日志、数据对象摘要 |
| 拆分 | `simulation`，seed 1 | 运行清单 |
| 模型 | GEARS 0.1.2，hidden size 64 | 模型目录、版本记录 |
| 预测 | 细胞级 H5AD | `prediction_contract.granularity=generated_cells` |
| 指标 | cell-eval 0.8.1，`profile="vcc"` | `cell-eval/` 输出 |
| 环境 | Python 3.11、Colab GPU | 运行时与 GPU 名称 |

机器可读模板位于
[`reproducibility/gears-norman-colab.yml`](https://github.com/methylation5mc2026-jpg/AI-Virtual-Cell-Guide/blob/main/reproducibility/gears-norman-colab.yml)。

## 防止“伪复现”

- 合成数据只验证管线，绝不形成生物学结论；
- 条件均值只保存一行，不能重复成伪细胞；
- 缺失原始计数时不创建 `layers.counts`；
- 本地教学指标与 Arc 官方分数明确分开；
- 五轮短跑标记为 smoke run，不声称复现论文性能；
- 第三方数据和模型不再分发。

## 当前开放项

公开 Beta 后通过 GitHub Issue 收集至少两名 AI 新人、一名生信研究者和一名实验研究者
的真实试读反馈。收到反馈前，角色化内部审读只算发布前检查，不算外部验证。
