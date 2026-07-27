---
title: 结构化资源目录
summary: 100 条论文、模型、数据、基准、工具和组织的统一可筛选索引。
level: reference
prerequisites: []
estimated_time: 按需查阅
last_reviewed: 2026-07-28
---

# 结构化资源目录

资源目录的唯一数据源是仓库根目录下的 `catalog/*.yml`。论文、模型、数据集、基准以及工具/课程/组织分别生成对应页面；卡片可按关键词、推荐等级、发表状态和模态筛选。

## 如何筛选

1. 先看 `recommendation: core`，理解 AIVC 主线；
2. 根据 `tasks` 和 `modalities` 缩小范围；
3. 检查 `publication_status`，区分同行评审与预印本；
4. 检查 `reproducibility`、许可证和计算需求；
5. 阅读限制，不直接根据标题或参数量做选型。

## 字段说明

| 字段 | 含义 |
|---|---|
| `publication_status` | peer-reviewed、preprint、technical-report、product |
| `reproducibility` | 公开代码、数据、权重的组合状态 |
| `recommendation` | core、recommended、reference |
| `perturbation_types` | 遗传、化学、环境、疾病状态或无扰动 |
| `evidence_stage` | concept、in-silico、retrospective、prospective、deployed |
| `compute_tier` | CPU、单 GPU、多 GPU 或未知 |
| `last_verified` | 最后检查官方链接与状态的日期 |
| `verification_status` | 已核验、人工复核或暂不可达 |

## 贡献

新增资源请编辑 YAML 后运行：

```bash
python scripts/validate_catalog.py
python scripts/generate_catalog.py
```

生成的 Markdown 页面带有自动生成标记，请勿手工编辑。
