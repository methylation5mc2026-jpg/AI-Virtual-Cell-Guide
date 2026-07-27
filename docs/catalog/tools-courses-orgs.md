---
title: 工具、课程与组织目录
summary: 由结构化 YAML 生成的可核验、可筛选资源目录。
level: reference
prerequisites: []
estimated_time: 按需查阅
last_reviewed: 2026-07-28
---

<!-- 此文件由 scripts/generate_catalog.py 自动生成，请勿手工编辑。 -->

# 工具、课程与组织目录

共 **18** 条。正文精选主线资源；本页提供完整元数据与限制。

<div class="catalog-controls" role="search" aria-label="筛选资源">
  <label>搜索<input class="catalog-search" type="search" placeholder="标题、任务、模态或背景" autocomplete="off"></label>
  <label>推荐等级<select class="catalog-filter" data-field="recommendation">
    <option value="">全部</option><option value="core">必读</option>
    <option value="recommended">推荐</option><option value="reference">参考</option>
  </select></label>
  <label>发表状态<select class="catalog-filter" data-field="status">
    <option value="">全部</option><option value="peer-reviewed">同行评审</option>
    <option value="preprint">预印本</option>
    <option value="technical-report">技术报告</option>
    <option value="product">产品/项目</option>
  </select></label>
  <label>模态<select class="catalog-filter" data-field="modalities">
    <option value="">全部</option>
    <option value="imaging">imaging</option>
    <option value="multiome">multiome</option>
    <option value="protein">protein</option>
    <option value="scATAC-seq">scATAC-seq</option>
    <option value="scRNA-seq">scRNA-seq</option>
    <option value="single-cell-general">single-cell-general</option>
    <option value="spatial-transcriptomics">spatial-transcriptomics</option>
  </select></label>
</div>
<p class="catalog-result-count" role="status" aria-live="polite">显示 18 / 18 条</p>
<div class="resource-grid">
<article class="resource-card" id="course-single-cell-best-practices" data-search="单细胞最佳实践 single-cell best practices 开放课程 education, quality control, analysis workflow scrna-seq, scatac-seq, spatial-transcriptomics, multiome none 单细胞分析入门与参考" data-recommendation="core" data-status="peer-reviewed" data-modalities="scRNA-seq|scATAC-seq|spatial-transcriptomics|multiome">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#course-single-cell-best-practices">单细胞最佳实践</a></h2>
      <p class="resource-card__english">Single-cell best practices · 2023 · 开放课程</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--core">必读</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">从实验设计、质控、整合到下游分析系统讲解单细胞最佳实践，适合作为 AI 学习者的生物数据分析教材。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>education, quality control, analysis workflow</dd>
    <dt>模态</dt><dd>scRNA-seq, scATAC-seq, spatial-transcriptomics, multiome</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>multi-species；单细胞分析入门与参考</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41576-023-00586-w" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/theislab/single-cell-best-practices" rel="noopener">代码</a> <a class="resource-link" href="https://www.sc-best-practices.org/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>阅读无需计算；练习可用标准 CPU 环境 (cpu)</li>
      <li><strong>证据阶段：</strong>not-applicable</li>
      <li><strong>许可证：</strong>CC-BY-4.0</li>
      <li><strong>已知限制：</strong>不同平台和实验类型的细节更新很快，应用时应同时查阅当前工具文档。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="tool-scvi-tools" data-search="scvi-tools scvi-tools 概率建模工具 representation learning, batch integration, differential expression scrna-seq, scatac-seq, spatial-transcriptomics, multiome none 概率单细胞建模" data-recommendation="core" data-status="peer-reviewed" data-modalities="scRNA-seq|scATAC-seq|spatial-transcriptomics|multiome">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#tool-scvi-tools">scvi-tools</a></h2>
      <p class="resource-card__english">scvi-tools · 2022 · 概率建模工具</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--core">必读</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-only">仅代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">为单细胞和空间组学提供概率生成模型、统一接口与教程，适合学习和比较 scVI 系列方法。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>representation learning, batch integration, differential expression</dd>
    <dt>模态</dt><dd>scRNA-seq, scATAC-seq, spatial-transcriptomics, multiome</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>multi-species；概率单细胞建模</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41587-021-01206-w" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/scverse/scvi-tools" rel="noopener">代码</a> <a class="resource-link" href="https://scvi-tools.org/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>小数据可用 CPU；训练通常推荐 GPU (single-gpu)</li>
      <li><strong>证据阶段：</strong>not-applicable</li>
      <li><strong>许可证：</strong>BSD-3-Clause</li>
      <li><strong>已知限制：</strong>模型假设、批次设置和潜变量解释需要通过下游任务与生物学对照独立验证。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="tool-scanpy" data-search="scanpy scanpy 分析工具 quality control, clustering, differential expression scrna-seq none python 单细胞分析工作流" data-recommendation="core" data-status="peer-reviewed" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#tool-scanpy">Scanpy</a></h2>
      <p class="resource-card__english">Scanpy · 2018 · 分析工具</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--core">必读</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-only">仅代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">基于 AnnData 的可扩展单细胞分析工具，覆盖质控、归一化、降维、聚类、差异表达和可视化。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>quality control, clustering, differential expression</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>multi-species；Python 单细胞分析工作流</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1186/s13059-017-1382-0" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/scverse/scanpy" rel="noopener">代码</a> <a class="resource-link" href="https://scanpy.readthedocs.io/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>CPU；大规模邻居图和降维需要较高内存 (cpu)</li>
      <li><strong>证据阶段：</strong>not-applicable</li>
      <li><strong>许可证：</strong>BSD-3-Clause</li>
      <li><strong>已知限制：</strong>默认参数不是通用最佳实践；统计检验与预处理必须匹配实验设计。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="tool-anndata" data-search="anndata anndata 数据结构 data management, interoperability single-cell-general, multiome none 单细胞与空间组学分析" data-recommendation="core" data-status="peer-reviewed" data-modalities="single-cell-general|multiome">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#tool-anndata">AnnData</a></h2>
      <p class="resource-card__english">AnnData · 2017 · 数据结构</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--core">必读</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-only">仅代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">面向带注释矩阵的数据结构，是 Python 单细胞生态中表达矩阵、细胞元数据、基因元数据和多层数据的共同契约。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>data management, interoperability</dd>
    <dt>模态</dt><dd>single-cell-general, multiome</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>multi-species；单细胞与空间组学分析</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1101/2021.12.16.473007" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/scverse/anndata" rel="noopener">代码</a> <a class="resource-link" href="https://anndata.readthedocs.io/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>CPU；内存需求取决于矩阵规模和稀疏表示 (cpu)</li>
      <li><strong>证据阶段：</strong>not-applicable</li>
      <li><strong>许可证：</strong>BSD-3-Clause</li>
      <li><strong>已知限制：</strong>数据层的语义并非由格式自动保证，必须额外记录归一化、批次与实验条件。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="standard-ome-zarr" data-search="ome-zarr / ome-ngff ome-zarr next-generation file format 成像数据标准 image storage, interoperability, cloud access imaging none 多维显微图像与标签" data-recommendation="recommended" data-status="product" data-modalities="imaging">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#standard-ome-zarr">OME-Zarr / OME-NGFF</a></h2>
      <p class="resource-card__english">OME-Zarr Next-Generation File Format · 2026 · 成像数据标准</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--product">产品/项目</span><span class="resource-badge resource-badge--documentation-only">仅文档</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">为多尺度图像、标签、坐标变换和高内涵筛选定义云原生元数据规范。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>image storage, interoperability, cloud access</dd>
    <dt>模态</dt><dd>imaging</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>not-applicable；多维显微图像与标签</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://github.com/ome/ngff" rel="noopener">代码</a> <a class="resource-link" href="https://ngff.openmicroscopy.org/specifications/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>与数据规模相关，支持分块和对象存储 (cpu)</li>
      <li><strong>证据阶段：</strong>deployed</li>
      <li><strong>许可证：</strong>Specification terms; implementations vary</li>
      <li><strong>已知限制：</strong>规范和实现版本仍在演进，交换数据时必须声明版本并做读回测试。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="platform-openproblems-bio" data-search="open problems in single cell analysis open problems in single cell analysis 开放基准平台 benchmarking, reproducible workflows scrna-seq, scatac-seq, multiome chemical, none 单细胞竞赛与社区基准" data-recommendation="recommended" data-status="product" data-modalities="scRNA-seq|scATAC-seq|multiome">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#platform-openproblems-bio">Open Problems in Single Cell Analysis</a></h2>
      <p class="resource-card__english">Open Problems in Single Cell Analysis · 2026 · 开放基准平台</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--product">产品/项目</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">以可复用任务、数据加载器和评测脚本组织单细胞与多组学开放问题。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>benchmarking, reproducible workflows</dd>
    <dt>模态</dt><dd>scRNA-seq, scATAC-seq, multiome</dd>
    <dt>扰动</dt><dd>chemical, none</dd>
    <dt>物种/背景</dt><dd>human, mouse；单细胞竞赛与社区基准</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://github.com/openproblems-bio/openproblems" rel="noopener">代码</a> <a class="resource-link" href="https://openproblems.bio/" rel="noopener">数据</a> <a class="resource-link" href="https://openproblems.bio/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>任务跨度从 CPU 到 GPU (single-gpu)</li>
      <li><strong>证据阶段：</strong>deployed</li>
      <li><strong>许可证：</strong>MIT; dataset-specific terms</li>
      <li><strong>已知限制：</strong>历史竞赛链接和运行环境会变化，复现时需固定任务及数据版本。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="tool-spatialdata" data-search="spatialdata spatialdata 空间数据框架 spatial data management, interoperability spatial-transcriptomics, imaging, protein none 多平台空间组学数据" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="spatial-transcriptomics|imaging|protein">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#tool-spatialdata">SpatialData</a></h2>
      <p class="resource-card__english">SpatialData · 2025 · 空间数据框架</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-only">仅代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">统一表示图像、点、形状、标签和表格，并维护坐标变换关系。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>spatial data management, interoperability</dd>
    <dt>模态</dt><dd>spatial-transcriptomics, imaging, protein</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>multi-species；多平台空间组学数据</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41592-024-02212-x" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/scverse/spatialdata" rel="noopener">代码</a> <a class="resource-link" href="https://spatialdata.scverse.org/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>CPU；大图像需要分块存储 (cpu)</li>
      <li><strong>证据阶段：</strong>deployed</li>
      <li><strong>许可证：</strong>BSD-3-Clause</li>
      <li><strong>已知限制：</strong>格式仍在演进，写出前需固定版本并验证坐标变换。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="tool-vitessce" data-search="vitessce vitessce 多模态可视化 multimodal visualization, spatial exploration single-cell-general, spatial-transcriptomics, imaging, multiome none 门户、浏览器与 notebook 可视化" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="single-cell-general|spatial-transcriptomics|imaging|multiome">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#tool-vitessce">Vitessce</a></h2>
      <p class="resource-card__english">Vitessce · 2025 · 多模态可视化</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-only">仅代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">在浏览器和 Notebook 中联动浏览空间、成像和单细胞多组学数据。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>multimodal visualization, spatial exploration</dd>
    <dt>模态</dt><dd>single-cell-general, spatial-transcriptomics, imaging, multiome</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>multi-species；门户、浏览器与 Notebook 可视化</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41592-024-02436-x" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/vitessce/vitessce" rel="noopener">代码</a> <a class="resource-link" href="https://vitessce.io/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>浏览器端；大数据建议分块和远程对象存储 (cpu)</li>
      <li><strong>证据阶段：</strong>deployed</li>
      <li><strong>许可证：</strong>MIT</li>
      <li><strong>已知限制：</strong>可视化不能替代统计验证，远程数据配置需考虑访问权限和版本。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="org-arc-virtual-cell" data-search="arc 虚拟细胞计划 arc virtual cell initiative 研究计划 perturbation prediction, benchmarking, dataset generation scrna-seq none 扰动预测与开放评测" data-recommendation="recommended" data-status="product" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#org-arc-virtual-cell">Arc 虚拟细胞计划</a></h2>
      <p class="resource-card__english">Arc Virtual Cell Initiative · 2024 · 研究计划</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--product">产品/项目</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">围绕大规模扰动数据、预测模型和标准化评测推进虚拟细胞研究，并组织公开挑战。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>perturbation prediction, benchmarking, dataset generation</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human；扰动预测与开放评测</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://github.com/ArcInstitute" rel="noopener">代码</a> <a class="resource-link" href="https://virtualcellchallenge.org/" rel="noopener">数据</a> <a class="resource-link" href="https://arcinstitute.org/virtual-cell-initiative" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>浏览资料无需计算；挑战模型通常需要 GPU 或集群 (single-gpu)</li>
      <li><strong>证据阶段：</strong>deployed</li>
      <li><strong>许可证：</strong>各数据集与代码仓库分别声明</li>
      <li><strong>已知限制：</strong>挑战任务只覆盖 AIVC 的部分能力，排行榜不能替代跨数据与湿实验验证。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="platform-czi-virtual-cells" data-search="czi 虚拟细胞平台 czi virtual cells platform 模型平台 model discovery, dataset discovery, tutorials single-cell-general, multiome none 虚拟细胞模型与资源发现" data-recommendation="recommended" data-status="product" data-modalities="single-cell-general|multiome">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#platform-czi-virtual-cells">CZI 虚拟细胞平台</a></h2>
      <p class="resource-card__english">CZI Virtual Cells Platform · 2024 · 模型平台</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--product">产品/项目</span><span class="resource-badge resource-badge--documentation-only">仅文档</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">集中展示单细胞模型、数据、任务与教程的开放平台，便于比较模型卡、输入输出和使用入口。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>model discovery, dataset discovery, tutorials</dd>
    <dt>模态</dt><dd>single-cell-general, multiome</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>multi-species；虚拟细胞模型与资源发现</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://virtualcellmodels.cziscience.com/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>浏览资料无需计算；运行需求取决于模型 (unknown)</li>
      <li><strong>证据阶段：</strong>deployed</li>
      <li><strong>许可证：</strong>各模型与数据分别声明</li>
      <li><strong>已知限制：</strong>平台元数据持续演化，收录不等于独立复现或生物学有效性认证。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="tool-pertpy" data-search="pertpy pertpy 扰动分析工具 perturbation analysis, differential expression, response comparison scrna-seq none 遗传与化学单细胞扰动实验" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#tool-pertpy">PertPy</a></h2>
      <p class="resource-card__english">PertPy · 2024 · 扰动分析工具</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-only">仅代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">面向单细胞扰动数据的 Python 工具箱，汇集距离、差异、混杂校正和响应分析方法。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>perturbation analysis, differential expression, response comparison</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>multi-species；遗传与化学单细胞扰动实验</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41592-025-02909-7" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/scverse/pertpy" rel="noopener">代码</a> <a class="resource-link" href="https://pertpy.readthedocs.io/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>CPU；部分方法随细胞数和基因数增加而显著变慢 (cpu)</li>
      <li><strong>证据阶段：</strong>not-applicable</li>
      <li><strong>许可证：</strong>Apache-2.0</li>
      <li><strong>已知限制：</strong>工具统一了接口，但不能替代对实验重复、批次和适用统计假设的审查。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="tool-squidpy" data-search="squidpy squidpy 空间组学分析 spatial analysis, image features, neighborhood analysis spatial-transcriptomics, imaging none 点位级、细胞级和亚细胞空间数据" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="spatial-transcriptomics|imaging">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#tool-squidpy">Squidpy</a></h2>
      <p class="resource-card__english">Squidpy · 2022 · 空间组学分析</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-only">仅代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">基于 AnnData/SpatialData 提供空间邻域、图像特征、空间统计和可视化。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>spatial analysis, image features, neighborhood analysis</dd>
    <dt>模态</dt><dd>spatial-transcriptomics, imaging</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>multi-species；点位级、细胞级和亚细胞空间数据</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41592-021-01358-2" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/scverse/squidpy" rel="noopener">代码</a> <a class="resource-link" href="https://squidpy.readthedocs.io/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>CPU 为主，图像任务可使用 GPU (cpu)</li>
      <li><strong>证据阶段：</strong>deployed</li>
      <li><strong>许可证：</strong>BSD-3-Clause</li>
      <li><strong>已知限制：</strong>部分分析依赖分割、邻域图和空间尺度选择。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="org-scverse" data-search="scverse scverse 开源生态 software ecosystem, community training single-cell-general, spatial-transcriptomics, multiome none 开源单细胞软件与社区" data-recommendation="recommended" data-status="product" data-modalities="single-cell-general|spatial-transcriptomics|multiome">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#org-scverse">scverse</a></h2>
      <p class="resource-card__english">scverse · 2021 · 开源生态</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--product">产品/项目</span><span class="resource-badge resource-badge--documentation-only">仅文档</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">维护 AnnData、Scanpy、scvi-tools 等核心 Python 单细胞工具，并推动兼容性、治理和教育资源。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>software ecosystem, community training</dd>
    <dt>模态</dt><dd>single-cell-general, spatial-transcriptomics, multiome</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>multi-species；开源单细胞软件与社区</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://github.com/scverse" rel="noopener">代码</a> <a class="resource-link" href="https://scverse.org/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>不适用；取决于所选工具 (unknown)</li>
      <li><strong>证据阶段：</strong>deployed</li>
      <li><strong>许可证：</strong>各项目许可证不同</li>
      <li><strong>已知限制：</strong>生态覆盖广但并非质量背书，具体方法仍需回到论文、版本和基准。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="tool-napari" data-search="napari napari 多维图像查看器 image visualization, annotation, quality control imaging none 二维至多维显微图像" data-recommendation="recommended" data-status="product" data-modalities="imaging">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#tool-napari">napari</a></h2>
      <p class="resource-card__english">napari · 2019 · 多维图像查看器</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--product">产品/项目</span><span class="resource-badge resource-badge--code-only">仅代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">面向科学 Python 的多维图像、标签、点和形状交互查看及插件平台。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>image visualization, annotation, quality control</dd>
    <dt>模态</dt><dd>imaging</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>not-applicable；二维至多维显微图像</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://github.com/napari/napari" rel="noopener">代码</a> <a class="resource-link" href="https://napari.org/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>桌面 CPU；大体积渲染受显存影响 (cpu)</li>
      <li><strong>证据阶段：</strong>deployed</li>
      <li><strong>许可证：</strong>BSD-3-Clause</li>
      <li><strong>已知限制：</strong>插件质量和格式兼容性不一，不适合作为无审计的批处理真值来源。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="tool-singlecellexperiment" data-search="singlecellexperiment singlecellexperiment 单细胞数据容器 data management, interoperability single-cell-general, scatac-seq, multiome none r/bioconductor 单细胞工作流" data-recommendation="recommended" data-status="product" data-modalities="single-cell-general|scATAC-seq|multiome">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#tool-singlecellexperiment">SingleCellExperiment</a></h2>
      <p class="resource-card__english">SingleCellExperiment · 2017 · 单细胞数据容器</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--product">产品/项目</span><span class="resource-badge resource-badge--code-only">仅代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">Bioconductor 中存储计数、样本元数据、特征元数据和降维结果的标准类。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>data management, interoperability</dd>
    <dt>模态</dt><dd>single-cell-general, scATAC-seq, multiome</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>multi-species；R/Bioconductor 单细胞工作流</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://github.com/drisso/SingleCellExperiment" rel="noopener">代码</a> <a class="resource-link" href="https://bioconductor.org/packages/SingleCellExperiment/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>CPU (cpu)</li>
      <li><strong>证据阶段：</strong>deployed</li>
      <li><strong>许可证：</strong>Artistic-2.0</li>
      <li><strong>已知限制：</strong>与 AnnData 互转时需要检查稀疏矩阵、因子、替代实验和元数据类型。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="org-human-cell-atlas" data-search="人类细胞图谱联盟 human cell atlas 国际联盟 reference atlas, data standards, community training single-cell-general, spatial-transcriptomics, multiome none 人体组织细胞图谱" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="single-cell-general|spatial-transcriptomics|multiome">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#org-human-cell-atlas">人类细胞图谱联盟</a></h2>
      <p class="resource-card__english">Human Cell Atlas · 2016 · 国际联盟</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--data-only">仅数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">通过开放数据、标准、器官网络和培训建设人类细胞参考图谱，是跨组织表征和数据治理的重要来源。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>reference atlas, data standards, community training</dd>
    <dt>模态</dt><dd>single-cell-general, spatial-transcriptomics, multiome</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human；人体组织细胞图谱</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.7554/eLife.27041" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/HumanCellAtlas" rel="noopener">代码</a> <a class="resource-link" href="https://data.humancellatlas.org/" rel="noopener">数据</a> <a class="resource-link" href="https://www.humancellatlas.org/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>浏览元数据无需计算；下载和分析图谱需要高内存或云资源 (unknown)</li>
      <li><strong>证据阶段：</strong>not-applicable</li>
      <li><strong>许可证：</strong>各项目和数据集分别声明</li>
      <li><strong>已知限制：</strong>图谱由不同实验和项目组成，跨研究比较仍需处理批次、同意范围与组织偏差。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="tool-seurat" data-search="seurat seurat 分析工具 quality control, integration, multimodal analysis scrna-seq, scatac-seq, spatial-transcriptomics, multiome none r 语言单细胞工作流" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq|scATAC-seq|spatial-transcriptomics|multiome">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#tool-seurat">Seurat</a></h2>
      <p class="resource-card__english">Seurat · 2015 · 分析工具</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-only">仅代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">R 语言单细胞分析生态，覆盖预处理、整合、多模态、空间分析和可视化，并拥有广泛教程。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>quality control, integration, multimodal analysis</dd>
    <dt>模态</dt><dd>scRNA-seq, scATAC-seq, spatial-transcriptomics, multiome</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>multi-species；R 语言单细胞工作流</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/nbt.3192" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/satijalab/seurat" rel="noopener">代码</a> <a class="resource-link" href="https://satijalab.org/seurat/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>CPU；大对象整合需要较高内存 (cpu)</li>
      <li><strong>证据阶段：</strong>not-applicable</li>
      <li><strong>许可证：</strong>MIT</li>
      <li><strong>已知限制：</strong>不同版本的数据层与接口存在变化，跨项目复现必须固定版本并记录参数。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="tool-cellprofiler" data-search="cellprofiler cellprofiler 图像分析工作流 image analysis, feature extraction, quality control imaging none 高内涵显微图像和 cell painting" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="imaging">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#tool-cellprofiler">CellProfiler</a></h2>
      <p class="resource-card__english">CellProfiler · 2006 · 图像分析工作流</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-only">仅代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">以可复用流水线执行细胞分割、特征提取和高通量图像质控。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>image analysis, feature extraction, quality control</dd>
    <dt>模态</dt><dd>imaging</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>multi-species；高内涵显微图像和 Cell Painting</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1186/gb-2006-7-10-r100" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/CellProfiler/CellProfiler" rel="noopener">代码</a> <a class="resource-link" href="https://cellprofiler.org/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>CPU；高通量任务可并行 (cpu)</li>
      <li><strong>证据阶段：</strong>deployed</li>
      <li><strong>许可证：</strong>BSD-3-Clause</li>
      <li><strong>已知限制：</strong>规则和参数需要按成像批次验证，错误分割会系统性污染形态特征。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
</div>
<p class="catalog-empty" hidden>没有匹配的资源，请调整筛选条件。</p>
