---
title: 模型目录
summary: 由结构化 YAML 生成的可核验、可筛选资源目录。
level: reference
prerequisites: []
estimated_time: 按需查阅
last_reviewed: 2026-07-28
---

<!-- 此文件由 scripts/generate_catalog.py 自动生成，请勿手工编辑。 -->

# 模型目录

共 **23** 条。正文精选主线资源；本页提供完整元数据与限制。

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
    <option value="spatial-transcriptomics">spatial-transcriptomics</option>
  </select></label>
</div>
<p class="catalog-result-count" role="status" aria-live="polite">显示 23 / 23 条</p>
<div class="resource-grid">
<article class="resource-card" id="model-state" data-search="state state embedding and state transition aivc状态转换 state embedding, perturbation prediction, cross-context transfer scrna-seq chemical 多细胞背景的大规模观测与扰动数据" data-recommendation="core" data-status="technical-report" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#model-state">STATE</a></h2>
      <p class="resource-card__english">State Embedding and State Transition · 2025 · AIVC状态转换</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--core">必读</span><span class="resource-badge resource-badge--technical-report">技术报告</span><span class="resource-badge resource-badge--weights-and-code">权重＋代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">Arc的第一代虚拟细胞模型，将状态表征和扰动状态转换模块分开，覆盖遗传、化学和细胞因子响应。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>state embedding, perturbation prediction, cross-context transfer</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>chemical</dd>
    <dt>物种/背景</dt><dd>human；多细胞背景的大规模观测与扰动数据</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://arcinstitute.org/tools/state" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/ArcInstitute/state" rel="noopener">代码</a> <a class="resource-link" href="https://arcinstitute.org/tools/state" rel="noopener">权重</a> <a class="resource-link" href="https://github.com/ArcInstitute/arc-virtual-cell-atlas" rel="noopener">数据</a> <a class="resource-link" href="https://arcinstitute.org/virtual-cell-initiative" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>预训练模型推理与训练通常需要GPU (single-gpu)</li>
      <li><strong>证据阶段：</strong>concept</li>
      <li><strong>许可证：</strong>Arc Research/Public/Commercial model licenses；代码另见仓库</li>
      <li><strong>已知限制：</strong>模型与权重使用受特定许可证约束；当前主要预测转录组响应。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="model-scgpt" data-search="scgpt scgpt 单细胞基础模型 cell annotation, integration, gene network, perturbation prediction scrna-seq, multiome none 人类单细胞与多组学数据" data-recommendation="core" data-status="peer-reviewed" data-modalities="scRNA-seq|multiome">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#model-scgpt">scGPT</a></h2>
      <p class="resource-card__english">scGPT · 2024 · 单细胞基础模型</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--core">必读</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--weights-and-code">权重＋代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">面向单细胞多任务和多组学数据的生成式Transformer，提供预训练权重与下游任务代码。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>cell annotation, integration, gene network, perturbation prediction</dd>
    <dt>模态</dt><dd>scRNA-seq, multiome</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human；人类单细胞与多组学数据</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41592-024-02201-0" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/bowang-lab/scGPT" rel="noopener">代码</a> <a class="resource-link" href="https://huggingface.co/bowanglab/scGPT" rel="noopener">权重</a> <a class="resource-link" href="https://scgpt.readthedocs.io/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>单GPU下游任务；预训练需要多GPU (multi-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>MIT；权重另见模型卡</li>
      <li><strong>已知限制：</strong>不同任务代码路径和预处理并不完全统一，复现需固定版本。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="model-gears" data-search="gears graph-enhanced gene activation and repression simulator 图扰动模型 single perturbation prediction, combinatorial perturbation scrna-seq genetic-knockout 细胞系crispr扰动" data-recommendation="core" data-status="peer-reviewed" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#model-gears">GEARS</a></h2>
      <p class="resource-card__english">Graph-Enhanced Gene Activation and Repression Simulator · 2023 · 图扰动模型</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--core">必读</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">结合基因知识图和共表达图预测单基因与多基因干预后的转录响应。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>single perturbation prediction, combinatorial perturbation</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>genetic-knockout</dd>
    <dt>物种/背景</dt><dd>human；细胞系CRISPR扰动</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41587-023-01905-6" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/snap-stanford/GEARS" rel="noopener">代码</a> <a class="resource-link" href="https://dataverse.harvard.edu/dataverse/gears" rel="noopener">数据</a> <a class="resource-link" href="https://github.com/snap-stanford/GEARS" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>GPU推荐 (single-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>MIT</li>
      <li><strong>已知限制：</strong>跨细胞类型能力有限；组合预测需要组合训练信号。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="model-scvi" data-search="scvi single-cell variational inference 概率生成模型 representation learning, batch integration, differential expression scrna-seq none 通用单细胞rna测序" data-recommendation="core" data-status="peer-reviewed" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#model-scvi">scVI</a></h2>
      <p class="resource-card__english">single-cell Variational Inference · 2018 · 概率生成模型</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--core">必读</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-only">仅代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">以负二项等计数分布建模单细胞表达，是批次整合、潜在表示和下游生成模型的重要基线。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>representation learning, batch integration, differential expression</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>multi-species；通用单细胞RNA测序</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41592-018-0229-2" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/scverse/scvi-tools" rel="noopener">代码</a> <a class="resource-link" href="https://scvi-tools.org/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>CPU可用于小数据；GPU推荐 (single-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>BSD-3-Clause</li>
      <li><strong>已知限制：</strong>主要是观测数据的概率表征与整合，不是完整扰动状态转换模型。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="model-uce" data-search="uce universal cell embeddings 跨物种基础模型 cell embedding, cross-species integration, cell annotation scrna-seq, protein none 多物种单细胞数据" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq|protein">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#model-uce">UCE</a></h2>
      <p class="resource-card__english">Universal Cell Embeddings · 2026 · 跨物种基础模型</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--weights-and-code">权重＋代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">用蛋白序列表示提供统一基因空间，生成可跨物种使用的细胞嵌入。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>cell embedding, cross-species integration, cell annotation</dd>
    <dt>模态</dt><dd>scRNA-seq, protein</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>multi-species；多物种单细胞数据</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41586-026-10689-z" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/snap-stanford/UCE" rel="noopener">代码</a> <a class="resource-link" href="https://figshare.com/articles/dataset/Universal_Cell_Embeddings_Model_Files/24320806" rel="noopener">权重</a> <a class="resource-link" href="https://github.com/snap-stanford/UCE" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>GPU和较大内存推荐 (single-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>见官方仓库与Figshare</li>
      <li><strong>已知限制：</strong>主要提供表征；不直接预测干预后的细胞状态。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="model-scimilarity" data-search="scimilarity scimilarity 图谱检索模型 cell retrieval, cell annotation, atlas mapping scrna-seq none 23.4m细胞的人体图谱" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#model-scimilarity">SCimilarity</a></h2>
      <p class="resource-card__english">SCimilarity · 2025 · 图谱检索模型</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--weights-and-code">权重＋代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">通过度量学习建立可扩展细胞相似度，用于跨研究检索、注释和置信度判断。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>cell retrieval, cell annotation, atlas mapping</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human；23.4M细胞的人体图谱</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41586-024-08411-y" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/Genentech/scimilarity" rel="noopener">代码</a> <a class="resource-link" href="https://zenodo.org/records/10685499" rel="noopener">权重</a> <a class="resource-link" href="https://github.com/Genentech/scimilarity" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>CPU检索可行；图谱构建需要大内存 (cpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>Apache-2.0；权重和图谱另见发布页</li>
      <li><strong>已知限制：</strong>用于状态检索而非状态转换；低训练覆盖会降低表示置信度。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="model-scprint" data-search="scprint scprint 基因网络基础模型 gene network inference, cell labeling, imputation scrna-seq none 多组织人类单细胞数据" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#model-scprint">scPRINT</a></h2>
      <p class="resource-card__english">scPRINT · 2025 · 基因网络基础模型</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--weights-and-code">权重＋代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">在数千万细胞上预训练，重点支持基因网络推断、标签和表达相关任务。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>gene network inference, cell labeling, imputation</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human；多组织人类单细胞数据</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41467-025-58699-1" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/cantinilab/scPRINT" rel="noopener">代码</a> <a class="resource-link" href="https://huggingface.co/jkobject/scPRINT" rel="noopener">权重</a> <a class="resource-link" href="https://github.com/cantinilab/scPRINT" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>GPU推荐 (single-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>见官方仓库与模型卡</li>
      <li><strong>已知限制：</strong>网络推断结果不是直接因果证据；依赖预训练图谱覆盖。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="model-aido-cell" data-search="aido.cell aido.cell 单细胞基础模型 cell clustering, cell classification, perturbation modeling scrna-seq none cellxgene census等大规模人类细胞" data-recommendation="recommended" data-status="preprint" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#model-aido-cell">AIDO.Cell</a></h2>
      <p class="resource-card__english">AIDO.Cell · 2024 · 单细胞基础模型</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--preprint">预印本</span><span class="resource-badge resource-badge--weights-and-code">权重＋代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">采用全转录组连续值离散化与双向Transformer，在大规模人类细胞上预训练。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>cell clustering, cell classification, perturbation modeling</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human；CELLxGENE Census等大规模人类细胞</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1101/2024.11.28.625303" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/genbio-ai/AIDO" rel="noopener">代码</a> <a class="resource-link" href="https://huggingface.co/genbio-ai/AIDO.Cell-100M" rel="noopener">权重</a> <a class="resource-link" href="https://cellxgene.cziscience.com/census" rel="noopener">数据</a> <a class="resource-link" href="https://virtualcellmodels.cziscience.com/model/aido-cell" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>单GPU推理；预训练需要多GPU (multi-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>GenBio AI Community License</li>
      <li><strong>已知限制：</strong>社区许可证并非标准开源许可证；论文仍为预印本。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="model-genecompass" data-search="genecompass genecompass 知识与跨物种基础模型 gene representation, cell annotation, gene regulatory inference scrna-seq none 人和小鼠大规模单细胞图谱" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#model-genecompass">GeneCompass</a></h2>
      <p class="resource-card__english">GeneCompass · 2024 · 知识与跨物种基础模型</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--weights-and-code">权重＋代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">将基因调控、家族与共表达先验引入跨物种预训练，面向基因机制和细胞任务。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>gene representation, cell annotation, gene regulatory inference</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human, mouse；人和小鼠大规模单细胞图谱</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1093/nsr/nwae114" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/xCompass-AI/GeneCompass" rel="noopener">代码</a> <a class="resource-link" href="https://github.com/xCompass-AI/GeneCompass" rel="noopener">权重</a> <a class="resource-link" href="https://github.com/xCompass-AI/GeneCompass" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>GPU推荐 (single-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>见官方仓库</li>
      <li><strong>已知限制：</strong>先验知识可能带来物种和注释偏差；机制解释仍需实验验证。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="model-scfoundation" data-search="scfoundation scfoundation 单细胞基础模型 cell representation, cell annotation, perturbation prediction scrna-seq none 超过五千万细胞的人类转录组" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#model-scfoundation">scFoundation</a></h2>
      <p class="resource-card__english">scFoundation · 2024 · 单细胞基础模型</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--weights-and-code">权重＋代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">覆盖约两万基因的预训练模型，强调大规模人类单细胞转录组表示与多类下游任务。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>cell representation, cell annotation, perturbation prediction</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human；超过五千万细胞的人类转录组</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41592-024-02305-7" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/biomap-research/scFoundation" rel="noopener">代码</a> <a class="resource-link" href="https://github.com/biomap-research/scFoundation" rel="noopener">权重</a> <a class="resource-link" href="https://github.com/biomap-research/scFoundation" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>GPU推荐；模型与输入维度带来较高显存需求 (single-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>见官方仓库</li>
      <li><strong>已知限制：</strong>复杂度高，需与PCA、scVI和任务专用模型公平比较。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="model-cellot" data-search="cellot cellot 分布扰动模型 perturbation prediction, distribution modeling scrna-seq, imaging chemical 药物与细胞因子扰动" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq|imaging">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#model-cellot">CellOT</a></h2>
      <p class="resource-card__english">CellOT · 2023 · 分布扰动模型</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">用输入凸神经网络参数化最优传输，预测扰动后的单细胞分布。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>perturbation prediction, distribution modeling</dd>
    <dt>模态</dt><dd>scRNA-seq, imaging</dd>
    <dt>扰动</dt><dd>chemical</dd>
    <dt>物种/背景</dt><dd>human, mouse；药物与细胞因子扰动</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41592-023-01969-x" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/bunnech/cellot" rel="noopener">代码</a> <a class="resource-link" href="https://github.com/bunnech/cellot" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>单 GPU 推荐 (single-gpu)</li>
      <li><strong>证据阶段：</strong>retrospective</li>
      <li><strong>许可证：</strong>MIT</li>
      <li><strong>已知限制：</strong>逐扰动学习限制了对全新扰动的组合泛化。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="model-geneformer" data-search="geneformer geneformer 单细胞基础模型 cell classification, gene network, perturbation prioritization scrna-seq none 大规模人类单细胞图谱" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#model-geneformer">Geneformer</a></h2>
      <p class="resource-card__english">Geneformer · 2023 · 单细胞基础模型</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--weights-and-code">权重＋代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">以细胞内基因表达排序序列进行Transformer预训练，支持分类、网络和候选基因优先级等迁移任务。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>cell classification, gene network, perturbation prioritization</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human；大规模人类单细胞图谱</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41586-023-06139-9" rel="noopener">论文</a> <a class="resource-link" href="https://huggingface.co/ctheodoris/Geneformer" rel="noopener">代码</a> <a class="resource-link" href="https://huggingface.co/ctheodoris/Geneformer" rel="noopener">权重</a> <a class="resource-link" href="https://huggingface.co/ctheodoris/Geneformer" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>单GPU推理/微调；按模型版本调整显存 (single-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>见官方模型卡</li>
      <li><strong>已知限制：</strong>排序表示忽略绝对表达与部分技术过程；任务解释性需独立验证。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="model-multivi" data-search="multivi multivi rna-atac联合模型 multimodal integration, imputation scrna-seq, scatac-seq, protein, multiome none 单细胞多组学" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq|scATAC-seq|protein|multiome">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#model-multivi">MultiVI</a></h2>
      <p class="resource-card__english">MultiVI · 2023 · RNA-ATAC联合模型</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">联合分析单模态、配对和马赛克式 RNA、ATAC、蛋白数据。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>multimodal integration, imputation</dd>
    <dt>模态</dt><dd>scRNA-seq, scATAC-seq, protein, multiome</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human；单细胞多组学</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41592-023-01909-9" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/scverse/scvi-tools" rel="noopener">代码</a> <a class="resource-link" href="https://docs.scvi-tools.org/en/stable/user_guide/models/multivi.html" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>单 GPU 推荐 (single-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>BSD-3-Clause</li>
      <li><strong>已知限制：</strong>未测模态的预测必须与真实配对数据分开评测。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="model-destvi" data-search="destvi deconvolution of spatial transcriptomics profiles using variational inference 空间反卷积 spatial deconvolution, continuous state inference scrna-seq, spatial-transcriptomics none visium 等点位级空间转录组" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq|spatial-transcriptomics">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#model-destvi">DestVI</a></h2>
      <p class="resource-card__english">Deconvolution of Spatial Transcriptomics Profiles Using Variational Inference · 2022 · 空间反卷积</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">联合单细胞参考和空间观测，估计空间位置的细胞类型比例与连续状态。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>spatial deconvolution, continuous state inference</dd>
    <dt>模态</dt><dd>scRNA-seq, spatial-transcriptomics</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human, mouse；Visium 等点位级空间转录组</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41587-022-01272-8" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/scverse/scvi-tools" rel="noopener">代码</a> <a class="resource-link" href="https://docs.scvi-tools.org/en/stable/user_guide/models/destvi.html" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>单 GPU 推荐 (single-gpu)</li>
      <li><strong>证据阶段：</strong>retrospective</li>
      <li><strong>许可证：</strong>BSD-3-Clause</li>
      <li><strong>已知限制：</strong>依赖匹配的单细胞参考，稀有或缺失细胞类型难以可靠恢复。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="model-scglue" data-search="scglue graph-linked unified embedding 图多组学 multimodal integration, regulatory inference scrna-seq, scatac-seq, multiome none 非配对 rna 与染色质数据" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq|scATAC-seq|multiome">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#model-scglue">scGLUE</a></h2>
      <p class="resource-card__english">Graph-Linked Unified Embedding · 2022 · 图多组学</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">以调控图连接非配对组学的潜空间，兼顾整合和调控关系推断。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>multimodal integration, regulatory inference</dd>
    <dt>模态</dt><dd>scRNA-seq, scATAC-seq, multiome</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human, mouse；非配对 RNA 与染色质数据</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41587-022-01284-4" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/gao-lab/GLUE" rel="noopener">代码</a> <a class="resource-link" href="https://scglue.readthedocs.io/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>单 GPU 推荐 (single-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>MIT</li>
      <li><strong>已知限制：</strong>整合质量对先验图、特征过滤和对抗训练敏感。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="model-cellpose" data-search="cellpose cellpose 通用细胞分割 cell segmentation, image analysis imaging none 荧光与明场显微图像" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="imaging">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#model-cellpose">Cellpose</a></h2>
      <p class="resource-card__english">Cellpose · 2021 · 通用细胞分割</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--weights-and-code">权重＋代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">使用流场表示进行二维和三维细胞分割，并提供预训练模型和交互工具。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>cell segmentation, image analysis</dd>
    <dt>模态</dt><dd>imaging</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>multi-species；荧光与明场显微图像</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41592-020-01018-x" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/MouseLand/cellpose" rel="noopener">代码</a> <a class="resource-link" href="https://www.cellpose.org/" rel="noopener">权重</a> <a class="resource-link" href="https://www.cellpose.org/dataset" rel="noopener">数据</a> <a class="resource-link" href="https://www.cellpose.org/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>CPU 可运行，GPU 显著加速 (single-gpu)</li>
      <li><strong>证据阶段：</strong>retrospective</li>
      <li><strong>许可证：</strong>BSD-3-Clause</li>
      <li><strong>已知限制：</strong>跨成像协议需抽样人工检查，分割误差会传播到所有下游特征。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="model-cpa" data-search="cpa compositional perturbation autoencoder 条件生成 drug response, dose response, combinatorial perturbation scrna-seq chemical 遗传与化学扰动数据" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#model-cpa">CPA</a></h2>
      <p class="resource-card__english">Compositional Perturbation Autoencoder · 2021 · 条件生成</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-only">仅代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">将基础细胞状态、扰动、剂量和协变量表示组合，用于未见条件的反事实响应预测。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>drug response, dose response, combinatorial perturbation</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>chemical</dd>
    <dt>物种/背景</dt><dd>human；遗传与化学扰动数据</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.15252/msb.202211517" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/theislab/cpa" rel="noopener">代码</a> <a class="resource-link" href="https://cpa-tools.readthedocs.io/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>单GPU推荐 (single-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>BSD-3-Clause</li>
      <li><strong>已知限制：</strong>表示解耦和组合假设需通过未见背景与强基线验证。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="model-tangram" data-search="tangram tangram 空间映射 spatial mapping, deconvolution scrna-seq, spatial-transcriptomics none 单细胞参考和空间组织切片" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq|spatial-transcriptomics">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#model-tangram">Tangram</a></h2>
      <p class="resource-card__english">Tangram · 2021 · 空间映射</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">学习单细胞参考与空间表达之间的概率匹配。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>spatial mapping, deconvolution</dd>
    <dt>模态</dt><dd>scRNA-seq, spatial-transcriptomics</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human, mouse；单细胞参考和空间组织切片</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41592-021-01264-7" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/broadinstitute/Tangram" rel="noopener">代码</a> <a class="resource-link" href="https://tangram-sc.readthedocs.io/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>单 GPU 推荐 (single-gpu)</li>
      <li><strong>证据阶段：</strong>retrospective</li>
      <li><strong>许可证：</strong>BSD-3-Clause</li>
      <li><strong>已知限制：</strong>空间映射受参考覆盖和共享基因限制。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="model-totalvi" data-search="totalvi total variational inference rna-蛋白联合模型 multimodal integration, denoising, differential expression scrna-seq, protein none cite-seq 配对多组学" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq|protein">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#model-totalvi">totalVI</a></h2>
      <p class="resource-card__english">total Variational Inference · 2021 · RNA-蛋白联合模型</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">面向 CITE-seq 的生成模型，联合估计 RNA、蛋白背景、批次和潜在细胞状态。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>multimodal integration, denoising, differential expression</dd>
    <dt>模态</dt><dd>scRNA-seq, protein</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human, mouse；CITE-seq 配对多组学</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41592-020-01050-x" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/scverse/scvi-tools" rel="noopener">代码</a> <a class="resource-link" href="https://docs.scvi-tools.org/en/stable/user_guide/models/totalvi.html" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>单 GPU 推荐 (single-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>BSD-3-Clause</li>
      <li><strong>已知限制：</strong>依赖明确的批次和蛋白背景建模，潜变量不等于机制状态。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="model-scgen" data-search="scgen scgen 状态转换 perturbation prediction, cross-cell-type transfer scrna-seq none 刺激与疾病相关单细胞数据" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#model-scgen">scGen</a></h2>
      <p class="resource-card__english">scGen · 2019 · 状态转换</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-only">仅代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">在VAE潜在空间应用扰动差向量，提供直观、轻量的跨细胞背景响应预测基线。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>perturbation prediction, cross-cell-type transfer</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human, mouse；刺激与疾病相关单细胞数据</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41592-019-0494-8" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/theislab/scgen" rel="noopener">代码</a> <a class="resource-link" href="https://scgen.readthedocs.io/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>CPU小数据或单GPU (single-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>Apache-2.0</li>
      <li><strong>已知限制：</strong>差向量可加性无法覆盖复杂、异质或强非线性响应。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="model-stardist" data-search="stardist stardist 实例分割 nucleus segmentation, instance segmentation imaging none 二维和三维显微图像" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="imaging">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#model-stardist">StarDist</a></h2>
      <p class="resource-card__english">StarDist · 2018 · 实例分割</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--weights-and-code">权重＋代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">用星形凸多边形或多面体表示细胞核，适合拥挤荧光图像实例分割。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>nucleus segmentation, instance segmentation</dd>
    <dt>模态</dt><dd>imaging</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>multi-species；二维和三维显微图像</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1007/978-3-030-00934-2_30" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/stardist/stardist" rel="noopener">代码</a> <a class="resource-link" href="https://bioimage.io/" rel="noopener">权重</a> <a class="resource-link" href="https://stardist.net/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>CPU 可推理，训练推荐单 GPU (single-gpu)</li>
      <li><strong>证据阶段：</strong>retrospective</li>
      <li><strong>许可证：</strong>BSD-3-Clause</li>
      <li><strong>已知限制：</strong>星形凸假设不适合所有细胞形状，模型迁移需匹配像素尺度。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="model-tahoe-x1" data-search="tahoe-x1 tahoe-x1 扰动基础模型 cell representation, perturbation prediction scrna-seq chemical tahoe-100m癌细胞系药物扰动" data-recommendation="reference" data-status="preprint" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#model-tahoe-x1">Tahoe-x1</a></h2>
      <p class="resource-card__english">Tahoe-x1 · 2025 · 扰动基础模型</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--reference">参考</span><span class="resource-badge resource-badge--preprint">预印本</span><span class="resource-badge resource-badge--weights-and-code">权重＋代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">面向十亿级扰动数据训练的单细胞基础模型，强调在Tahoe-100M上的规模化训练。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>cell representation, perturbation prediction</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>chemical</dd>
    <dt>物种/背景</dt><dd>human；Tahoe-100M癌细胞系药物扰动</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1101/2025.10.23.683759" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/tahoebio/tahoe-x1" rel="noopener">代码</a> <a class="resource-link" href="https://huggingface.co/tahoebio" rel="noopener">权重</a> <a class="resource-link" href="https://huggingface.co/datasets/tahoebio/Tahoe-100M" rel="noopener">数据</a> <a class="resource-link" href="https://github.com/tahoebio/tahoe-x1" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>多GPU训练；推理需求按模型规模变化 (multi-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>见官方仓库、模型卡和数据卡</li>
      <li><strong>已知限制：</strong>预印本；以癌细胞系化学扰动训练，跨原代组织结论需验证。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="model-cellplm" data-search="cellplm cellplm 细胞与空间基础模型 cell representation, spatial analysis, cell annotation scrna-seq, spatial-transcriptomics none 单细胞与空间数据" data-recommendation="reference" data-status="preprint" data-modalities="scRNA-seq|spatial-transcriptomics">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#model-cellplm">CellPLM</a></h2>
      <p class="resource-card__english">CellPLM · 2024 · 细胞与空间基础模型</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--reference">参考</span><span class="resource-badge resource-badge--preprint">预印本</span><span class="resource-badge resource-badge--weights-and-code">权重＋代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">使用细胞邻域和关系信息进行预训练，支持单细胞与空间转录组下游任务。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>cell representation, spatial analysis, cell annotation</dd>
    <dt>模态</dt><dd>scRNA-seq, spatial-transcriptomics</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human, mouse；单细胞与空间数据</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1101/2023.10.03.560734" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/OmicsML/CellPLM" rel="noopener">代码</a> <a class="resource-link" href="https://github.com/OmicsML/CellPLM" rel="noopener">权重</a> <a class="resource-link" href="https://github.com/OmicsML/CellPLM" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>GPU推荐 (single-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>见官方仓库</li>
      <li><strong>已知限制：</strong>预印本状态；跨平台和空间邻域定义影响迁移结果。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
</div>
<p class="catalog-empty" hidden>没有匹配的资源，请调整筛选条件。</p>
