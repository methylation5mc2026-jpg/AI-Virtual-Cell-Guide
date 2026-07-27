---
title: 数据集目录
summary: 由结构化 YAML 生成的可核验、可筛选资源目录。
level: reference
prerequisites: []
estimated_time: 按需查阅
last_reviewed: 2026-07-28
---

<!-- 此文件由 scripts/generate_catalog.py 自动生成，请勿手工编辑。 -->

# 数据集目录

共 **20** 条。正文精选主线资源；本页提供完整元数据与限制。

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
<p class="catalog-result-count" role="status" aria-live="polite">显示 20 / 20 条</p>
<div class="resource-grid">
<article class="resource-card" id="dataset-arc-vcc-2025" data-search="arc virtual cell challenge 2025数据 arc virtual cell challenge 2025 dataset 评测扰动数据 held-out perturbation prediction, benchmarking scrna-seq genetic-knockdown h1人胚胎干细胞" data-recommendation="core" data-status="peer-reviewed" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#dataset-arc-vcc-2025">Arc Virtual Cell Challenge 2025数据</a></h2>
      <p class="resource-card__english">Arc Virtual Cell Challenge 2025 Dataset · 2025 · 评测扰动数据</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--core">必读</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">为未见基因扰动预测专门设计的H1人胚胎干细胞CRISPRi训练、验证和测试数据。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>held-out perturbation prediction, benchmarking</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>genetic-knockdown</dd>
    <dt>物种/背景</dt><dd>human；H1人胚胎干细胞</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1016/j.cell.2025.05.045" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/ArcInstitute/arc-virtual-cell-atlas" rel="noopener">代码</a> <a class="resource-link" href="https://github.com/ArcInstitute/arc-virtual-cell-atlas/tree/main/virtual-cell-challenge" rel="noopener">数据</a> <a class="resource-link" href="https://virtualcellchallenge.org/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>约30万高深度细胞；下载和分析需较大内存 (unknown)</li>
      <li><strong>证据阶段：</strong>not-applicable</li>
      <li><strong>许可证：</strong>Arc数据与挑战条款；使用前核查最新版本</li>
      <li><strong>已知限制：</strong>单一细胞背景；指标和测试设计不能代表所有AIVC用途。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="dataset-scperturb" data-search="scperturb统一扰动数据 scperturb harmonized single-cell perturbation data 扰动数据集合 perturbation prediction, perturbation effect analysis, benchmarking scrna-seq chemical 多实验、多细胞系与部分原代背景" data-recommendation="core" data-status="peer-reviewed" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#dataset-scperturb">scPerturb统一扰动数据</a></h2>
      <p class="resource-card__english">scPerturb Harmonized Single-Cell Perturbation Data · 2024 · 扰动数据集合</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--core">必读</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">统一整理基因、药物和其他单细胞扰动数据，提供标准化h5ad和数据元信息。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>perturbation prediction, perturbation effect analysis, benchmarking</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>chemical</dd>
    <dt>物种/背景</dt><dd>human, mouse；多实验、多细胞系与部分原代背景</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41592-023-02144-y" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/theislab/sc-pert" rel="noopener">代码</a> <a class="resource-link" href="https://zenodo.org/doi/10.5281/zenodo.7041848" rel="noopener">数据</a> <a class="resource-link" href="https://www.sanderlab.org/scPerturb/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>单个数据集可单机处理 (unknown)</li>
      <li><strong>证据阶段：</strong>not-applicable</li>
      <li><strong>许可证：</strong>原数据集许可证各异；Zenodo记录提供汇总信息</li>
      <li><strong>已知限制：</strong>跨研究预处理无法消除实验设计差异；统一格式不等于可直接合并训练。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="dataset-cellxgene-census" data-search="cellxgene census cz cellxgene discover census 单细胞图谱 pretraining, atlas mapping, reference annotation scrna-seq none 多组织、疾病和研究来源" data-recommendation="core" data-status="technical-report" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#dataset-cellxgene-census">CELLxGENE Census</a></h2>
      <p class="resource-card__english">CZ CELLxGENE Discover Census · 2023 · 单细胞图谱</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--core">必读</span><span class="resource-badge resource-badge--technical-report">技术报告</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">对CELLxGENE公开单细胞数据进行版本化、统一访问和基础标准化，是许多单细胞基础模型的预训练来源。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>pretraining, atlas mapping, reference annotation</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human, mouse；多组织、疾病和研究来源</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1101/2023.10.30.563174" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/chanzuckerberg/cellxgene-census" rel="noopener">代码</a> <a class="resource-link" href="https://registry.opendata.aws/cellxgene-census/" rel="noopener">数据</a> <a class="resource-link" href="https://chanzuckerberg.github.io/cellxgene-census/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>可按查询子集；全量使用需要云存储与大内存 (unknown)</li>
      <li><strong>证据阶段：</strong>not-applicable</li>
      <li><strong>许可证：</strong>各数据集许可证不同；使用前检查Census元数据</li>
      <li><strong>已知限制：</strong>聚合图谱存在研究选择、标签不一致、重复样本和平台偏差。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="dataset-norman" data-search="norman 2019 perturb-seq norman 2019 crispra perturb-seq 基因组合扰动 single perturbation prediction, combinatorial perturbation scrna-seq genetic-activation k562细胞系" data-recommendation="core" data-status="peer-reviewed" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#dataset-norman">Norman 2019 Perturb-seq</a></h2>
      <p class="resource-card__english">Norman 2019 CRISPRa Perturb-seq · 2019 · 基因组合扰动</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--core">必读</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">K562单基因和双基因CRISPRa数据，被GEARS等模型广泛使用，也是本项目真实数据实践入口。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>single perturbation prediction, combinatorial perturbation</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>genetic-activation</dd>
    <dt>物种/背景</dt><dd>human；K562细胞系</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1126/science.aax4438" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/snap-stanford/GEARS" rel="noopener">代码</a> <a class="resource-link" href="https://dataverse.harvard.edu/dataverse/gears" rel="noopener">数据</a> <a class="resource-link" href="https://github.com/snap-stanford/GEARS" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>CPU可完成基础分析；GEARS训练建议GPU (single-gpu)</li>
      <li><strong>证据阶段：</strong>not-applicable</li>
      <li><strong>许可证：</strong>见Harvard Dataverse和原论文</li>
      <li><strong>已知限制：</strong>单一癌细胞系和CRISPRa；常用处理版本可能与原始数据不同。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="dataset-human-cell-atlas" data-search="人类细胞图谱 human cell atlas data portal 国际细胞图谱 cell atlas, reference mapping, pretraining multiome, spatial-transcriptomics none 多组织、发育、健康与疾病" data-recommendation="core" data-status="peer-reviewed" data-modalities="multiome|spatial-transcriptomics">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#dataset-human-cell-atlas">人类细胞图谱</a></h2>
      <p class="resource-card__english">Human Cell Atlas Data Portal · 2017 · 国际细胞图谱</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--core">必读</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--data-only">仅数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">以开放标准构建人体细胞参考图谱，提供项目、数据和伦理治理框架。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>cell atlas, reference mapping, pretraining</dd>
    <dt>模态</dt><dd>multiome, spatial-transcriptomics</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human；多组织、发育、健康与疾病</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.7554/eLife.27041" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/HumanCellAtlas" rel="noopener">代码</a> <a class="resource-link" href="https://data.humancellatlas.org/" rel="noopener">数据</a> <a class="resource-link" href="https://www.humancellatlas.org/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>按项目下载；全量整合需要云计算 (unknown)</li>
      <li><strong>证据阶段：</strong>not-applicable</li>
      <li><strong>许可证：</strong>数据集级许可与访问条件</li>
      <li><strong>已知限制：</strong>图谱仍在建设；组织和人群覆盖不均，标签来自不同分析流程。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="dataset-allen-cell" data-search="allen integrated cell allen cell explorer data 三维细胞成像 cell morphology, organelle localization, image generation imaging chemical, none 人诱导多能干细胞三维荧光成像" data-recommendation="recommended" data-status="product" data-modalities="imaging">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#dataset-allen-cell">Allen Integrated Cell</a></h2>
      <p class="resource-card__english">Allen Cell Explorer Data · 2026 · 三维细胞成像</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--product">产品/项目</span><span class="resource-badge resource-badge--data-only">仅数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">提供人 iPSC 的三维细胞、细胞器、分割、特征和部分扰动成像数据。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>cell morphology, organelle localization, image generation</dd>
    <dt>模态</dt><dd>imaging</dd>
    <dt>扰动</dt><dd>chemical, none</dd>
    <dt>物种/背景</dt><dd>human；人诱导多能干细胞三维荧光成像</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://www.allencell.org/data-downloading.html" rel="noopener">数据</a> <a class="resource-link" href="https://www.allencell.org/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>单个数据集从 GB 到数百 GB (single-gpu)</li>
      <li><strong>证据阶段：</strong>not-applicable</li>
      <li><strong>许可证：</strong>Allen Institute data terms</li>
      <li><strong>已知限制：</strong>主要集中于特定 iPSC 系和标记结构，不能代表全部细胞背景。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="dataset-vizgen-merfish" data-search="vizgen merfish 公共数据 vizgen merfish data release program 亚细胞空间转录组 spatial analysis, cell segmentation, transcript localization spatial-transcriptomics, imaging none 脑、肿瘤及其他组织切片" data-recommendation="recommended" data-status="product" data-modalities="spatial-transcriptomics|imaging">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#dataset-vizgen-merfish">Vizgen MERFISH 公共数据</a></h2>
      <p class="resource-card__english">Vizgen MERFISH Data Release Program · 2026 · 亚细胞空间转录组</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--product">产品/项目</span><span class="resource-badge resource-badge--data-only">仅数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">提供 MERSCOPE 生成的 MERFISH 1.0/2.0 公共组织数据和示例分析文件。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>spatial analysis, cell segmentation, transcript localization</dd>
    <dt>模态</dt><dd>spatial-transcriptomics, imaging</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human, mouse；脑、肿瘤及其他组织切片</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://vizgen.com/data-release-program/" rel="noopener">数据</a> <a class="resource-link" href="https://vizgen.com/data-release-program/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>原始空间文件需要高内存与存储 (single-gpu)</li>
      <li><strong>证据阶段：</strong>not-applicable</li>
      <li><strong>许可证：</strong>Vizgen data release terms</li>
      <li><strong>已知限制：</strong>面板、软件版本和商业平台处理流程需随每个数据发布单独记录。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="dataset-scbasecount" data-search="arc scbasecount scbasecount 统一计数图谱 pretraining, atlas curation, cross-dataset analysis scrna-seq none 多研究和细胞背景的公开数据" data-recommendation="recommended" data-status="technical-report" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#dataset-scbasecount">Arc scBaseCount</a></h2>
      <p class="resource-card__english">scBaseCount · 2025 · 统一计数图谱</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--technical-report">技术报告</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">Arc用于收集、整理并重新处理公开单细胞原始计数的图谱基础。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>pretraining, atlas curation, cross-dataset analysis</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human；多研究和细胞背景的公开数据</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://github.com/ArcInstitute/arc-virtual-cell-atlas" rel="noopener">代码</a> <a class="resource-link" href="https://github.com/ArcInstitute/arc-virtual-cell-atlas" rel="noopener">数据</a> <a class="resource-link" href="https://arcinstitute.org/virtual-cell-initiative" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>全量规模面向云与分布式处理 (unknown)</li>
      <li><strong>证据阶段：</strong>not-applicable</li>
      <li><strong>许可证：</strong>数据集级许可证与Arc发布条款</li>
      <li><strong>已知限制：</strong>自动化收集与重处理仍受原始元数据、许可和质量差异影响。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="dataset-tahoe-100m" data-search="tahoe-100m tahoe-100m 超大规模化学扰动 drug response, cross-context prediction, pretraining scrna-seq chemical 50个癌细胞系" data-recommendation="recommended" data-status="preprint" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#dataset-tahoe-100m">Tahoe-100M</a></h2>
      <p class="resource-card__english">Tahoe-100M · 2025 · 超大规模化学扰动</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--preprint">预印本</span><span class="resource-badge resource-badge--data-only">仅数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">约一亿单细胞转录组，覆盖五十个癌细胞系与上千药物剂量条件。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>drug response, cross-context prediction, pretraining</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>chemical</dd>
    <dt>物种/背景</dt><dd>human；50个癌细胞系</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1101/2025.02.20.639398" rel="noopener">论文</a> <a class="resource-link" href="https://huggingface.co/datasets/tahoebio/Tahoe-100M" rel="noopener">数据</a> <a class="resource-link" href="https://huggingface.co/datasets/tahoebio/Tahoe-100M" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>全量需要流式或分布式处理 (unknown)</li>
      <li><strong>证据阶段：</strong>not-applicable</li>
      <li><strong>许可证：</strong>见Hugging Face数据卡</li>
      <li><strong>已知限制：</strong>癌细胞系、药物和固定读出时间不能覆盖复杂组织与患者反应。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="dataset-jump-cell-painting" data-search="jump cell painting jump cell painting consortium dataset 扰动形态组学 morphological profiling, mechanism retrieval imaging genetic-knockout, chemical 培养细胞高内涵显微成像" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="imaging">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#dataset-jump-cell-painting">JUMP Cell Painting</a></h2>
      <p class="resource-card__english">JUMP Cell Painting Consortium Dataset · 2024 · 扰动形态组学</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">大规模遗传和化学扰动 Cell Painting 图像与形态特征集合。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>morphological profiling, mechanism retrieval</dd>
    <dt>模态</dt><dd>imaging</dd>
    <dt>扰动</dt><dd>genetic-knockout, chemical</dd>
    <dt>物种/背景</dt><dd>human；培养细胞高内涵显微成像</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41592-024-02528-8" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/jump-cellpainting/datasets" rel="noopener">代码</a> <a class="resource-link" href="https://registry.opendata.aws/cellpainting-gallery/" rel="noopener">数据</a> <a class="resource-link" href="https://jump-cellpainting.broadinstitute.org/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>原始图像需要 TB 级存储；特征表可用 CPU (multi-gpu)</li>
      <li><strong>证据阶段：</strong>not-applicable</li>
      <li><strong>许可证：</strong>CC0 and accession-specific terms</li>
      <li><strong>已知限制：</strong>多批次、多中心和板位效应显著，必须按实验结构拆分。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="dataset-rxrx3" data-search="rxrx3 rxrx3: phenomics map of biology 扰动形态组学 representation learning, drug-target retrieval imaging genetic-knockout, chemical huvec 细胞与多通道显微图像" data-recommendation="recommended" data-status="preprint" data-modalities="imaging">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#dataset-rxrx3">RxRx3</a></h2>
      <p class="resource-card__english">RxRx3: Phenomics Map of Biology · 2023 · 扰动形态组学</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--preprint">预印本</span><span class="resource-badge resource-badge--data-only">仅数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">包含 CRISPR 基因敲除和化合物处理的数百万张高内涵细胞图像。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>representation learning, drug-target retrieval</dd>
    <dt>模态</dt><dd>imaging</dd>
    <dt>扰动</dt><dd>genetic-knockout, chemical</dd>
    <dt>物种/背景</dt><dd>human；HUVEC 细胞与多通道显微图像</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1101/2023.02.07.527350" rel="noopener">论文</a> <a class="resource-link" href="https://www.rxrx.ai/rxrx3" rel="noopener">数据</a> <a class="resource-link" href="https://www.rxrx.ai/rxrx3" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>完整数据约 83 TB，需分布式存储与 GPU (multi-gpu)</li>
      <li><strong>证据阶段：</strong>not-applicable</li>
      <li><strong>许可证：</strong>Recursion Non-Commercial EULA</li>
      <li><strong>已知限制：</strong>访问方式和非商业许可限制复现与再分发；批次结构需保留。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="dataset-replogle" data-search="replogle全基因组perturb-seq replogle genome-scale perturb-seq 全基因组crispri gene function, perturbation prediction, regulatory programs scrna-seq genetic-knockdown k562和rpe1等细胞系" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#dataset-replogle">Replogle全基因组Perturb-seq</a></h2>
      <p class="resource-card__english">Replogle Genome-Scale Perturb-seq · 2022 · 全基因组CRISPRi</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">大规模基因敲低单细胞数据，支持基因功能、细胞程序和未见扰动预测研究。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>gene function, perturbation prediction, regulatory programs</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>genetic-knockdown</dd>
    <dt>物种/背景</dt><dd>human；K562和RPE1等细胞系</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1016/j.cell.2022.05.013" rel="noopener">论文</a> <a class="resource-link" href="https://gwps.wi.mit.edu/" rel="noopener">代码</a> <a class="resource-link" href="https://gwps.wi.mit.edu/" rel="noopener">数据</a> <a class="resource-link" href="https://gwps.wi.mit.edu/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>全量分析需要较大内存和存储 (unknown)</li>
      <li><strong>证据阶段：</strong>not-applicable</li>
      <li><strong>许可证：</strong>见数据门户和原论文</li>
      <li><strong>已知限制：</strong>主要为体外细胞系和转录组终点；不同处理版本需固定。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="dataset-tabula-sapiens" data-search="tabula sapiens tabula sapiens 跨组织单细胞图谱 cell annotation, atlas mapping, pretraining scrna-seq none 多供体、多器官健康组织" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#dataset-tabula-sapiens">Tabula Sapiens</a></h2>
      <p class="resource-card__english">Tabula Sapiens · 2022 · 跨组织单细胞图谱</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">来自多名供体、覆盖多组织的人类单细胞转录组图谱，适合研究组织与供体上下文。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>cell annotation, atlas mapping, pretraining</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human；多供体、多器官健康组织</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1126/science.abl4896" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/czbiohub/tabula-sapiens" rel="noopener">代码</a> <a class="resource-link" href="https://cellxgene.cziscience.com/collections/e5f58829-1a66-40b5-a624-9046778e74f5" rel="noopener">数据</a> <a class="resource-link" href="https://tabula-sapiens-portal.ds.czbiohub.org/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>可按组织子集分析；全量需较大内存 (unknown)</li>
      <li><strong>证据阶段：</strong>not-applicable</li>
      <li><strong>许可证：</strong>见数据门户</li>
      <li><strong>已知限制：</strong>供体数量和健康组织采集流程限制人群与疾病泛化。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="dataset-human-cell-landscape" data-search="人类细胞景观 human cell landscape 跨组织图谱 cell annotation, cross-tissue integration scrna-seq none 胎儿与成人多组织" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#dataset-human-cell-landscape">人类细胞景观</a></h2>
      <p class="resource-card__english">Human Cell Landscape · 2020 · 跨组织图谱</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--data-only">仅数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">覆盖 50 余种人类组织的单细胞转录组资源，包含组织来源和细胞注释。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>cell annotation, cross-tissue integration</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human；胎儿与成人多组织</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41586-020-2157-4" rel="noopener">论文</a> <a class="resource-link" href="https://db.cngb.org/HCL/" rel="noopener">数据</a> <a class="resource-link" href="https://bis.zju.edu.cn/HCL/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>CPU 可查询，完整整合建议高内存 (cpu)</li>
      <li><strong>证据阶段：</strong>not-applicable</li>
      <li><strong>许可证：</strong>Portal and source-study terms</li>
      <li><strong>已知限制：</strong>Microwell-seq 平台和跨供体覆盖不均会影响与其他图谱比较。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="dataset-sciplex" data-search="sci-plex化学扰动图谱 sci-plex 化学扰动 drug response, dose response, chemical screening scrna-seq chemical a549、k562、mcf7等癌细胞系" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#dataset-sciplex">sci-Plex化学扰动图谱</a></h2>
      <p class="resource-card__english">sci-Plex · 2020 · 化学扰动</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">通过组合索引大规模测量多细胞系、药物和剂量下的单细胞转录响应。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>drug response, dose response, chemical screening</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>chemical</dd>
    <dt>物种/背景</dt><dd>human；A549、K562、MCF7等癌细胞系</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1126/science.aax6234" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/cole-trapnell-lab/sci-plex" rel="noopener">代码</a> <a class="resource-link" href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE139944" rel="noopener">数据</a> <a class="resource-link" href="https://github.com/cole-trapnell-lab/sci-plex" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>全量分析需要大内存；子集可单机 (unknown)</li>
      <li><strong>证据阶段：</strong>not-applicable</li>
      <li><strong>许可证：</strong>GEO与官方仓库条款</li>
      <li><strong>已知限制：</strong>癌细胞系、特定时间点与药物面板限制生理外推。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="dataset-shareseq" data-search="share-seq share-seq rna and chromatin accessibility data 配对多组学 multimodal integration, regulatory inference, trajectory scrna-seq, scatac-seq, multiome none 皮肤、脑和肺等组织" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq|scATAC-seq|multiome">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#dataset-shareseq">SHARE-seq</a></h2>
      <p class="resource-card__english">SHARE-seq RNA and Chromatin Accessibility Data · 2020 · 配对多组学</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--data-only">仅数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">在同一细胞中配对测量染色质可及性与 RNA，用于调控和轨迹建模。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>multimodal integration, regulatory inference, trajectory</dd>
    <dt>模态</dt><dd>scRNA-seq, scATAC-seq, multiome</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>mouse；皮肤、脑和肺等组织</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1016/j.cell.2020.09.056" rel="noopener">论文</a> <a class="resource-link" href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE140203" rel="noopener">数据</a> <a class="resource-link" href="https://pubmed.ncbi.nlm.nih.gov/33098772/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>完整矩阵需高内存，CPU 可处理子集 (cpu)</li>
      <li><strong>证据阶段：</strong>not-applicable</li>
      <li><strong>许可证：</strong>GEO terms</li>
      <li><strong>已知限制：</strong>稀疏性和配对测量误差会影响跨模态关联与伪时间推断。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="dataset-tabula-muris-senis" data-search="tabula muris senis tabula muris senis 小鼠衰老图谱 cell annotation, aging atlas, cross-tissue integration scrna-seq none 多组织衰老细胞图谱" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#dataset-tabula-muris-senis">Tabula Muris Senis</a></h2>
      <p class="resource-card__english">Tabula Muris Senis · 2020 · 小鼠衰老图谱</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">跨年龄、组织和性别的小鼠单细胞转录组，为年龄泛化提供参考。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>cell annotation, aging atlas, cross-tissue integration</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>mouse；多组织衰老细胞图谱</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41586-020-2496-1" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/czbiohub/tabula-muris-senis" rel="noopener">代码</a> <a class="resource-link" href="https://figshare.com/projects/Tabula_Muris_Senis/64982" rel="noopener">数据</a> <a class="resource-link" href="https://tabula-muris-senis.ds.czbiohub.org/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>CPU 可处理子集，完整整合建议高内存 (cpu)</li>
      <li><strong>证据阶段：</strong>not-applicable</li>
      <li><strong>许可证：</strong>CC BY 4.0</li>
      <li><strong>已知限制：</strong>小鼠品系、取样和平台结构限制跨物种及跨实验解释。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="dataset-hubmap" data-search="hubmap human biomolecular atlas program 空间多组学图谱 spatial atlas, multimodal integration, tissue mapping spatial-transcriptomics, imaging, protein, multiome none 多人体器官与组织" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="spatial-transcriptomics|imaging|protein|multiome">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#dataset-hubmap">HuBMAP</a></h2>
      <p class="resource-card__english">Human BioMolecular Atlas Program · 2019 · 空间多组学图谱</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--data-only">仅数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">提供人体组织的空间、多组学与成像数据，对AIVC跨尺度和组织上下文研究重要。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>spatial atlas, multimodal integration, tissue mapping</dd>
    <dt>模态</dt><dd>spatial-transcriptomics, imaging, protein, multiome</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human；多人体器官与组织</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41586-019-1629-x" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/hubmapconsortium" rel="noopener">代码</a> <a class="resource-link" href="https://portal.hubmapconsortium.org/" rel="noopener">数据</a> <a class="resource-link" href="https://hubmapconsortium.org/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>模态和切片数据可能非常大 (unknown)</li>
      <li><strong>证据阶段：</strong>not-applicable</li>
      <li><strong>许可证：</strong>数据集级许可；部分人类数据受控</li>
      <li><strong>已知限制：</strong>多中心、多平台异质性高；部分数据访问和再分发受限。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="dataset-human-protein-atlas-cell" data-search="人类蛋白质图谱细胞图谱 human protein atlas cell atlas 细胞成像与亚细胞定位 protein localization, cell imaging, multimodal representation imaging, protein none 多种人类细胞系与亚细胞结构" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="imaging|protein">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#dataset-human-protein-atlas-cell">人类蛋白质图谱细胞图谱</a></h2>
      <p class="resource-card__english">Human Protein Atlas Cell Atlas · 2017 · 细胞成像与亚细胞定位</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--data-only">仅数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">提供人类蛋白在细胞和亚细胞结构中的定位图像与注释，为成像型虚拟细胞提供参考。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>protein localization, cell imaging, multimodal representation</dd>
    <dt>模态</dt><dd>imaging, protein</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human；多种人类细胞系与亚细胞结构</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1126/science.aal3321" rel="noopener">论文</a> <a class="resource-link" href="https://www.proteinatlas.org/humanproteome/subcellular/data" rel="noopener">数据</a> <a class="resource-link" href="https://www.proteinatlas.org/humanproteome/subcellular" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>图像批量训练需要GPU和较大存储 (single-gpu)</li>
      <li><strong>证据阶段：</strong>not-applicable</li>
      <li><strong>许可证：</strong>Human Protein Atlas数据使用条款</li>
      <li><strong>已知限制：</strong>抗体特异性、细胞系覆盖和固定成像条件影响外推。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="dataset-bbbc" data-search="broad 生物图像基准集合 broad bioimage benchmark collection 生物图像基准数据 segmentation, classification, morphological profiling imaging chemical, none 多种显微技术、细胞和组织" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="imaging">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#dataset-bbbc">Broad 生物图像基准集合</a></h2>
      <p class="resource-card__english">Broad Bioimage Benchmark Collection · 2012 · 生物图像基准数据</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--data-only">仅数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">汇集带人工或合成真值的显微图像，用于分割、分类和形态分析验证。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>segmentation, classification, morphological profiling</dd>
    <dt>模态</dt><dd>imaging</dd>
    <dt>扰动</dt><dd>chemical, none</dd>
    <dt>物种/背景</dt><dd>multi-species；多种显微技术、细胞和组织</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/nmeth.2083" rel="noopener">论文</a> <a class="resource-link" href="https://bbbc.broadinstitute.org/image_sets" rel="noopener">数据</a> <a class="resource-link" href="https://bbbc.broadinstitute.org/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>从 MB 到 TB，按图像集选择 (cpu)</li>
      <li><strong>证据阶段：</strong>not-applicable</li>
      <li><strong>许可证：</strong>Dataset-specific licenses</li>
      <li><strong>已知限制：</strong>各图像集采集条件和真值定义不同，不能混合为单一排行榜。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
</div>
<p class="catalog-empty" hidden>没有匹配的资源，请调整筛选条件。</p>
