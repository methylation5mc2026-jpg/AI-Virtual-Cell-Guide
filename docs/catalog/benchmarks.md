---
title: 基准目录
summary: 由结构化 YAML 生成的可核验、可筛选资源目录。
level: reference
prerequisites: []
estimated_time: 按需查阅
last_reviewed: 2026-07-28
---

<!-- 此文件由 scripts/generate_catalog.py 自动生成，请勿手工编辑。 -->

# 基准目录

共 **14** 条。正文精选主线资源；本页提供完整元数据与限制。

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
    <option value="lineage">lineage</option>
    <option value="multiome">multiome</option>
    <option value="protein">protein</option>
    <option value="scATAC-seq">scATAC-seq</option>
    <option value="scRNA-seq">scRNA-seq</option>
    <option value="spatial-transcriptomics">spatial-transcriptomics</option>
  </select></label>
</div>
<p class="catalog-result-count" role="status" aria-live="polite">显示 14 / 14 条</p>
<div class="resource-grid">
<article class="resource-card" id="benchmark-cell-eval" data-search="cell-eval arc cell-eval 扰动预测评测库 perturbation evaluation, metric implementation scrna-seq none state与virtual cell challenge相关任务" data-recommendation="core" data-status="technical-report" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#benchmark-cell-eval">cell-eval</a></h2>
      <p class="resource-card__english">Arc cell-eval · 2025 · 扰动预测评测库</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--core">必读</span><span class="resource-badge resource-badge--technical-report">技术报告</span><span class="resource-badge resource-badge--code-only">仅代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">Arc为STATE与细胞状态转换任务维护的统一评测实现，包含多种表达和扰动指标。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>perturbation evaluation, metric implementation</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human；STATE与Virtual Cell Challenge相关任务</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://arcinstitute.org/tools/state" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/ArcInstitute/cell-eval" rel="noopener">代码</a> <a class="resource-link" href="https://github.com/ArcInstitute/cell-eval" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>CPU可运行多数指标；大数据需要批处理 (cpu)</li>
      <li><strong>证据阶段：</strong>concept</li>
      <li><strong>许可证：</strong>见官方仓库</li>
      <li><strong>已知限制：</strong>指标实现与模型/数据协议仍在演进，必须固定版本。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="benchmark-vcc-2025" data-search="arc virtual cell challenge 2025 virtual cell challenge 2025 未见扰动预测 held-out perturbation prediction, model comparison scrna-seq genetic-knockdown h1人胚胎干细胞、300个目标基因" data-recommendation="core" data-status="peer-reviewed" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#benchmark-vcc-2025">Arc Virtual Cell Challenge 2025</a></h2>
      <p class="resource-card__english">Virtual Cell Challenge 2025 · 2025 · 未见扰动预测</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--core">必读</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">以H1人胚胎干细胞CRISPRi数据评测未见基因扰动响应，采用DES、PDS和MAE。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>held-out perturbation prediction, model comparison</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>genetic-knockdown</dd>
    <dt>物种/背景</dt><dd>human；H1人胚胎干细胞、300个目标基因</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1016/j.cell.2025.05.045" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/ArcInstitute/arc-virtual-cell-atlas" rel="noopener">代码</a> <a class="resource-link" href="https://github.com/ArcInstitute/arc-virtual-cell-atlas/tree/main/virtual-cell-challenge" rel="noopener">数据</a> <a class="resource-link" href="https://virtualcellchallenge.org/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>完整数据分析需要较大内存；提交模型通常需要GPU (single-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>Arc挑战与数据条款</li>
      <li><strong>已知限制：</strong>单细胞背景；排行榜指标会影响建模策略，不能代表全部生物学用途。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="benchmark-multimodal-integration-2025" data-search="单细胞多模态整合多任务基准 multitask benchmarking of single-cell multimodal omics integration methods 多模态整合 multimodal integration, benchmarking scrna-seq, scatac-seq, protein, multiome none 多技术、多组织的单细胞多组学" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq|scATAC-seq|protein|multiome">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#benchmark-multimodal-integration-2025">单细胞多模态整合多任务基准</a></h2>
      <p class="resource-card__english">Multitask Benchmarking of Single-Cell Multimodal Omics Integration Methods · 2025 · 多模态整合</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--documentation-only">仅文档</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">从多类下游任务评估多模态整合，避免仅依赖可视化或单一邻域指标。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>multimodal integration, benchmarking</dd>
    <dt>模态</dt><dd>scRNA-seq, scATAC-seq, protein, multiome</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human, mouse；多技术、多组织的单细胞多组学</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41592-025-02856-3" rel="noopener">论文</a> <a class="resource-link" href="https://doi.org/10.1038/s41592-025-02856-3" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>方法跨度从 CPU 到多 GPU (multi-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>Article and source-dataset terms apply</li>
      <li><strong>已知限制：</strong>排名取决于任务权重、预处理和超参数预算，不能视为普遍优劣。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="benchmark-perturbench" data-search="perturbench perturbench 单细胞扰动模型基准 perturbation prediction, distribution evaluation, model comparison scrna-seq chemical scperturb及其他公开扰动数据" data-recommendation="recommended" data-status="preprint" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#benchmark-perturbench">PerturBench</a></h2>
      <p class="resource-card__english">PerturBench · 2025 · 单细胞扰动模型基准</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--preprint">预印本</span><span class="resource-badge resource-badge--code-only">仅代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">为单细胞扰动模型提供标准数据模块、预测接口、模型和评测流程，强调分布级比较。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>perturbation prediction, distribution evaluation, model comparison</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>chemical</dd>
    <dt>物种/背景</dt><dd>human, mouse；scPerturb及其他公开扰动数据</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://arxiv.org/abs/2408.10609" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/altoslabs/perturbench" rel="noopener">代码</a> <a class="resource-link" href="https://www.sanderlab.org/scPerturb/" rel="noopener">数据</a> <a class="resource-link" href="https://openreview.net/forum?id=PPPDuyiZaG" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>CPU可做基线；生成模型训练建议GPU (single-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>Apache-2.0</li>
      <li><strong>已知限制：</strong>预印本与活跃开发状态；不同数据集仍存在任务定义差异。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="benchmark-jump-cell-painting" data-search="jump cell painting 表型检索 jump cell painting benchmark 形态表征 phenotypic retrieval, batch generalization imaging genetic-knockout, chemical 多中心 cell painting 数据" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="imaging">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#benchmark-jump-cell-painting">JUMP Cell Painting 表型检索</a></h2>
      <p class="resource-card__english">JUMP Cell Painting Benchmark · 2024 · 形态表征</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">在跨批次遗传与化学扰动上评测形态特征的可重复性和生物关联检索。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>phenotypic retrieval, batch generalization</dd>
    <dt>模态</dt><dd>imaging</dd>
    <dt>扰动</dt><dd>genetic-knockout, chemical</dd>
    <dt>物种/背景</dt><dd>human；多中心 Cell Painting 数据</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41592-024-02528-8" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/jump-cellpainting/2024_Chandrasekaran_NatureMethods" rel="noopener">代码</a> <a class="resource-link" href="https://registry.opendata.aws/cellpainting-gallery/" rel="noopener">数据</a> <a class="resource-link" href="https://jump-cellpainting.broadinstitute.org/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>特征表可用 CPU，图像模型需要 GPU (single-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>CC0 and accession-specific terms</li>
      <li><strong>已知限制：</strong>批次校正可能同时移除真实信号，必须同时报告重复性与生物检索。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="benchmark-scperturb-estatistics" data-search="scperturb效应量与e-distance scperturb e-statistics benchmarking resources 扰动效应评测 perturbation effect quantification, distribution comparison scrna-seq none 多个遗传、药物和环境扰动数据" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#benchmark-scperturb-estatistics">scPerturb效应量与E-distance</a></h2>
      <p class="resource-card__english">scPerturb E-statistics Benchmarking Resources · 2024 · 扰动效应评测</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">在统一扰动数据上提供分布距离和效应显著性资源，可补充均值与Top-DE指标。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>perturbation effect quantification, distribution comparison</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human, mouse；多个遗传、药物和环境扰动数据</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41592-023-02144-y" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/theislab/sc-pert" rel="noopener">代码</a> <a class="resource-link" href="https://zenodo.org/doi/10.5281/zenodo.7041848" rel="noopener">数据</a> <a class="resource-link" href="https://www.sanderlab.org/scPerturb/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>CPU可运行；全量数据需批处理 (cpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>各原始数据许可证不同</li>
      <li><strong>已知限制：</strong>分布距离受样本量、批次和预处理影响，不能单独证明机制。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="benchmark-cytospace" data-search="单细胞到空间位置映射基准 cytospace spatial mapping benchmark 空间映射 spatial mapping, method comparison scrna-seq, spatial-transcriptomics none 单细胞参考与多平台空间转录组" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq|spatial-transcriptomics">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#benchmark-cytospace">单细胞到空间位置映射基准</a></h2>
      <p class="resource-card__english">CytoSPACE Spatial Mapping Benchmark · 2023 · 空间映射</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">比较专用空间映射、单细胞整合和朴素距离方法的细胞到位置对齐。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>spatial mapping, method comparison</dd>
    <dt>模态</dt><dd>scRNA-seq, spatial-transcriptomics</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human, mouse；单细胞参考与多平台空间转录组</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41587-023-01697-9" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/digitalcytometry/cytospace" rel="noopener">代码</a> <a class="resource-link" href="https://github.com/digitalcytometry/cytospace" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>CPU 可运行，大数据需高内存 (cpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>GPL-3.0</li>
      <li><strong>已知限制：</strong>不同空间技术的真值精度不一致，评测结论不能直接外推到新组织。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="benchmark-openproblems-perturbation" data-search="open problems单细胞扰动预测挑战 open problems single-cell perturbations 药物扰动预测 drug response, cross-cell-type prediction scrna-seq chemical pbmc细胞类型与小分子处理" data-recommendation="recommended" data-status="product" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#benchmark-openproblems-perturbation">Open Problems单细胞扰动预测挑战</a></h2>
      <p class="resource-card__english">Open Problems Single-Cell Perturbations · 2023 · 药物扰动预测</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--product">产品/项目</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">以外周血单核细胞药物处理数据评测跨细胞类型表达响应预测。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>drug response, cross-cell-type prediction</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>chemical</dd>
    <dt>物种/背景</dt><dd>human；PBMC细胞类型与小分子处理</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://github.com/openproblems-bio/openproblems" rel="noopener">代码</a> <a class="resource-link" href="https://www.kaggle.com/competitions/open-problems-single-cell-perturbations" rel="noopener">数据</a> <a class="resource-link" href="https://openproblems.bio/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>CPU可做pseudobulk基线；高排名方案常用GPU (single-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>Kaggle竞赛与数据条款</li>
      <li><strong>已知限制：</strong>主要评价pseudobulk差异表达，单一数据设计限制广泛外推。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="benchmark-openproblems-multiome" data-search="open problems多组学整合挑战 open problems multimodal single-cell integration 多组学整合 modality prediction, modality matching, joint embedding scrna-seq, scatac-seq, protein none pbmc和骨髓多组学数据" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq|scATAC-seq|protein">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#benchmark-openproblems-multiome">Open Problems多组学整合挑战</a></h2>
      <p class="resource-card__english">Open Problems Multimodal Single-Cell Integration · 2021 · 多组学整合</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">公开评测RNA、ATAC和蛋白等模态的匹配、预测与联合嵌入任务。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>modality prediction, modality matching, joint embedding</dd>
    <dt>模态</dt><dd>scRNA-seq, scATAC-seq, protein</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human；PBMC和骨髓多组学数据</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41587-023-01933-2" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/openproblems-bio/openproblems" rel="noopener">代码</a> <a class="resource-link" href="https://openproblems.bio/competitions/neurips_2021/" rel="noopener">数据</a> <a class="resource-link" href="https://openproblems.bio/events/2021-09_neurips" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>任务方案从CPU到多GPU不等 (multi-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>数据与竞赛条款；代码见仓库</li>
      <li><strong>已知限制：</strong>竞赛数据和指标不能覆盖所有组织、平台与缺失模态情况。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="benchmark-scib" data-search="scib整合基准 scib 单细胞数据整合 batch integration, representation evaluation scrna-seq none 多数据集、批次和细胞类型整合" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#benchmark-scib">scIB整合基准</a></h2>
      <p class="resource-card__english">scIB · 2020 · 单细胞数据整合</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-only">仅代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">用批次去除和生物结构保留等互补指标比较单细胞整合方法。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>batch integration, representation evaluation</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human, mouse；多数据集、批次和细胞类型整合</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41592-021-01336-8" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/theislab/scib" rel="noopener">代码</a> <a class="resource-link" href="https://scib.readthedocs.io/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>CPU；大数据图指标需要较大内存 (cpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>MIT</li>
      <li><strong>已知限制：</strong>整合指标不评价扰动预测或机制；聚合总分可能掩盖指标权衡。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="benchmark-cell-tracking-challenge" data-search="细胞追踪挑战 cell tracking challenge 时序成像 cell segmentation, cell tracking, lineage reconstruction imaging, lineage none 二维和三维活细胞显微序列" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="imaging|lineage">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#benchmark-cell-tracking-challenge">细胞追踪挑战</a></h2>
      <p class="resource-card__english">Cell Tracking Challenge · 2017 · 时序成像</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--data-only">仅数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">以多种显微时间序列和专家真值评测细胞分割、追踪与谱系恢复。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>cell segmentation, cell tracking, lineage reconstruction</dd>
    <dt>模态</dt><dd>imaging, lineage</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>multi-species；二维和三维活细胞显微序列</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/nmeth.4473" rel="noopener">论文</a> <a class="resource-link" href="https://celltrackingchallenge.net/datasets/" rel="noopener">数据</a> <a class="resource-link" href="https://celltrackingchallenge.net/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>从 CPU 到单 GPU，取决于方法 (single-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>Challenge dataset terms</li>
      <li><strong>已知限制：</strong>排行榜指标依赖特定真值和对象定义，跨成像平台需单独报告。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="benchmark-bbbc" data-search="bbbc 生物图像基准 broad bioimage benchmark collection 图像分析 segmentation, classification, morphological profiling imaging chemical, none 多种成像平台和生物样本" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="imaging">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#benchmark-bbbc">BBBC 生物图像基准</a></h2>
      <p class="resource-card__english">Broad Bioimage Benchmark Collection · 2012 · 图像分析</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--data-only">仅数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">提供覆盖分割、分类和形态画像任务的标准显微图像及真值。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>segmentation, classification, morphological profiling</dd>
    <dt>模态</dt><dd>imaging</dd>
    <dt>扰动</dt><dd>chemical, none</dd>
    <dt>物种/背景</dt><dd>multi-species；多种成像平台和生物样本</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/nmeth.2083" rel="noopener">论文</a> <a class="resource-link" href="https://bbbc.broadinstitute.org/image_sets" rel="noopener">数据</a> <a class="resource-link" href="https://bbbc.broadinstitute.org/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>按图像集从 CPU 到 GPU (single-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>Dataset-specific licenses</li>
      <li><strong>已知限制：</strong>图像集之间任务与真值不同，不应汇总成单一总分。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="benchmark-foundation-model-perturbation-600" data-search="600模型扰动响应基准 foundation models improve perturbation response prediction 基础模型与扰动预测 foundation model benchmarking, perturbation prediction scrna-seq, protein chemical 多个遗传与化学扰动数据集" data-recommendation="reference" data-status="preprint" data-modalities="scRNA-seq|protein">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#benchmark-foundation-model-perturbation-600">600模型扰动响应基准</a></h2>
      <p class="resource-card__english">Foundation Models Improve Perturbation Response Prediction · 2026 · 基础模型与扰动预测</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--reference">参考</span><span class="resource-badge resource-badge--preprint">预印本</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">比较数百种基础模型表示、生成模型与简单基线，覆盖遗传和化学扰动及跨背景设置。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>foundation model benchmarking, perturbation prediction</dd>
    <dt>模态</dt><dd>scRNA-seq, protein</dd>
    <dt>扰动</dt><dd>chemical</dd>
    <dt>物种/背景</dt><dd>human；多个遗传与化学扰动数据集</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://www.biorxiv.org/content/10.64898/2026.02.18.706454v1" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/genbio-ai/foundation-models-perturbation" rel="noopener">代码</a> <a class="resource-link" href="https://huggingface.co/genbio-ai" rel="noopener">数据</a> <a class="resource-link" href="https://github.com/genbio-ai/foundation-models-perturbation" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>完整复现需要多GPU和大量预计算embedding (multi-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>GenBio AI Community License</li>
      <li><strong>已知限制：</strong>预印本；模型与数据选择、任务公式和社区许可证需要独立审查。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="benchmark-rxrx3-core" data-search="rxrx3-core 药物—靶点基准 rxrx3-core 零样本形态检索 zero-shot retrieval, drug-target interaction imaging genetic-knockout, chemical 高内涵成像中的遗传与药物扰动" data-recommendation="reference" data-status="preprint" data-modalities="imaging">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#benchmark-rxrx3-core">RxRx3-core 药物—靶点基准</a></h2>
      <p class="resource-card__english">RxRx3-core · 2025 · 零样本形态检索</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--reference">参考</span><span class="resource-badge resource-badge--preprint">预印本</span><span class="resource-badge resource-badge--data-only">仅数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">从 RxRx3 提取较小的形态学子集，评测零样本药物—靶点相互作用预测。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>zero-shot retrieval, drug-target interaction</dd>
    <dt>模态</dt><dd>imaging</dd>
    <dt>扰动</dt><dd>genetic-knockout, chemical</dd>
    <dt>物种/背景</dt><dd>human；高内涵成像中的遗传与药物扰动</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://arxiv.org/abs/2503.20158" rel="noopener">论文</a> <a class="resource-link" href="https://www.rxrx.ai/rxrx3" rel="noopener">数据</a> <a class="resource-link" href="https://www.rxrx.ai/rxrx3" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>约 18 GB，单 GPU 推荐 (single-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>Recursion Non-Commercial EULA</li>
      <li><strong>已知限制：</strong>仍继承 RxRx3 的许可、实验背景和隐藏混杂限制。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
</div>
<p class="catalog-empty" hidden>没有匹配的资源，请调整筛选条件。</p>
