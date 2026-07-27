# AI Virtual Cell Guide

> 面向 AI 背景跨学科新人的人工智能虚拟细胞（AI Virtual Cell, AIVC）全景知识地图与可复现学习指南。

[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-526CFE)](https://methylation5mc2026-jpg.github.io/AI-Virtual-Cell-Guide/)
[![Quality](https://github.com/methylation5mc2026-jpg/AI-Virtual-Cell-Guide/actions/workflows/quality.yml/badge.svg)](https://github.com/methylation5mc2026-jpg/AI-Virtual-Cell-Guide/actions/workflows/quality.yml)
[![Content License](https://img.shields.io/badge/content-CC%20BY%204.0-lightgrey)](LICENSE-CONTENT.md)
[![Code License](https://img.shields.io/badge/code-Apache--2.0-blue)](LICENSE-CODE)

AIVC 的目标不是把细胞简化成一个“大模型”，而是构建能够跨尺度表示细胞状态、预测扰动后的变化，并支持可检验虚拟实验的计算系统。当前模型不能替代真实实验或临床判断。

![AIVC 三项能力](docs/assets/aivc-capability-map.svg)

## 快速入口

- 第一次接触 AIVC：[从这里开始](docs/00-start-here/index.md)
- AI/机器学习背景：[AI → 生物](docs/learning-paths/ai-to-biology.md)
- 生物或生信背景：[生物 → AI](docs/learning-paths/biology-to-ai.md)
- 准备做研究：[研究前沿](docs/learning-paths/research-frontiers.md)
- 想先动手：[扰动响应预测实践](docs/tutorials/perturbation-response/index.md)
- 查模型、论文与数据：[结构化资源目录](docs/catalog/index.md)

## v0.2.0 Beta

- 50+ 个知识页面、3 条学习路径和 5 张原创知识图；
- 100 条 Schema v2 结构化资源，支持搜索和筛选；
- 严格 AnnData 契约、重复级拆分、CPU 统计基线；
- Colab GPU GEARS 路线与 Arc 官方指标适配入口；
- MkDocs 文档站、自动测试、链接维护和 GitHub Pages。

## 单一数据源

正文维护在 `docs/`；资源目录维护在 `catalog/*.yml`，页面由脚本生成。Notebook 源文件维护在 `notebooks/`，在线阅读页同样自动生成，禁止手工维护第二份表格或 Notebook 正文。

## 本地检查

```bash
pip install -e ".[docs,notebooks,dev]"
python scripts/validate_catalog.py
python scripts/generate_catalog.py --check
python scripts/render_notebooks.py --check
pytest
mkdocs build --strict
```

## 贡献、引用与许可

请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。正文、原创图和目录采用 [CC BY 4.0](LICENSE-CONTENT.md)，代码、Notebook、测试和自动化采用 [Apache-2.0](LICENSE-CODE)。第三方数据与模型遵循各自许可证，本仓库不重新分发受限资源。

第二轮优先完成真实外部试读、GEARS GPU 运行证据和空间映射实践，详见
[ROADMAP.md](ROADMAP.md)。
