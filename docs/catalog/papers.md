---
title: 论文目录
summary: 由结构化 YAML 生成的可核验、可筛选资源目录。
level: reference
prerequisites: []
estimated_time: 按需查阅
last_reviewed: 2026-07-28
---

<!-- 此文件由 scripts/generate_catalog.py 自动生成，请勿手工编辑。 -->

# 论文目录

共 **25** 条。正文精选主线资源；本页提供完整元数据与限制。

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
    <option value="bulk-omics">bulk-omics</option>
    <option value="imaging">imaging</option>
    <option value="lineage">lineage</option>
    <option value="multiome">multiome</option>
    <option value="protein">protein</option>
    <option value="scATAC-seq">scATAC-seq</option>
    <option value="scRNA-seq">scRNA-seq</option>
    <option value="spatial-transcriptomics">spatial-transcriptomics</option>
  </select></label>
</div>
<p class="catalog-result-count" role="status" aria-live="polite">显示 25 / 25 条</p>
<div class="resource-grid">
<article class="resource-card" id="simple-controls-2025" data-search="简单对照超过复杂扰动模型 simple controls exceed best deep learning algorithms and reveal foundation model effectiveness for predicting genetic perturbations 扰动评测 perturbation prediction, benchmarking scrna-seq none adamson、norman、replogle等遗传扰动数据" data-recommendation="core" data-status="peer-reviewed" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#simple-controls-2025">简单对照超过复杂扰动模型</a></h2>
      <p class="resource-card__english">Simple Controls Exceed Best Deep Learning Algorithms and Reveal Foundation Model Effectiveness for Predicting Genetic Perturbations · 2025 · 扰动评测</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--core">必读</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">系统展示简单均值和线性对照在多个基因扰动数据上可超过复杂方法，强调拆分、指标和基础模型公平比较。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>perturbation prediction, benchmarking</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human；Adamson、Norman、Replogle等遗传扰动数据</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12202205/" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/pfizer-opensource/perturb_seq" rel="noopener">代码</a> <a class="resource-link" href="https://github.com/pfizer-opensource/perturb_seq/tree/main/splits" rel="noopener">数据</a> <a class="resource-link" href="https://github.com/pfizer-opensource/perturb_seq" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>CPU可运行主要基线；基础模型比较需GPU (single-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>见论文与官方仓库</li>
      <li><strong>已知限制：</strong>结论依赖所选数据、任务和指标，不代表所有基础模型或扰动类型均无效。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="aivc-vision-2024" data-search="如何用人工智能构建虚拟细胞 how to build the virtual cell with artificial intelligence: priorities and opportunities aivc愿景 universal representation, state prediction, virtual experiments multiome, imaging, bulk-omics none 跨分子、细胞与组织尺度的开放科学愿景" data-recommendation="core" data-status="peer-reviewed" data-modalities="multiome|imaging|bulk-omics">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#aivc-vision-2024">如何用人工智能构建虚拟细胞</a></h2>
      <p class="resource-card__english">How to Build the Virtual Cell with Artificial Intelligence: Priorities and Opportunities · 2024 · AIVC愿景</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--core">必读</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--documentation-only">仅文档</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">定义AIVC的统一表征、预测模拟和虚拟实验三项核心能力，是本指南信息架构的主要依据。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>universal representation, state prediction, virtual experiments</dd>
    <dt>模态</dt><dd>multiome, imaging, bulk-omics</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>multi-species；跨分子、细胞与组织尺度的开放科学愿景</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1016/j.cell.2024.11.015" rel="noopener">论文</a> <a class="resource-link" href="https://pubmed.ncbi.nlm.nih.gov/39672099/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>不适用 (unknown)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>CC BY (article)</li>
      <li><strong>已知限制：</strong>观点与路线图，不是已经实现或经过统一评测的完整模型。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="replogle-2022" data-search="全基因组perturb-seq mapping information-rich genotype-phenotype landscapes with genome-scale perturb-seq 扰动图谱 gene function, perturbation prediction, regulatory programs scrna-seq genetic-knockdown k562、rpe1等细胞系的大规模基因敲低" data-recommendation="core" data-status="peer-reviewed" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#replogle-2022">全基因组Perturb-seq</a></h2>
      <p class="resource-card__english">Mapping Information-Rich Genotype-Phenotype Landscapes with Genome-Scale Perturb-seq · 2022 · 扰动图谱</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--core">必读</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">构建大规模CRISPRi单细胞扰动图谱，推动基因功能、细胞程序和状态预测研究。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>gene function, perturbation prediction, regulatory programs</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>genetic-knockdown</dd>
    <dt>物种/背景</dt><dd>human；K562、RPE1等细胞系的大规模基因敲低</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1016/j.cell.2022.05.013" rel="noopener">论文</a> <a class="resource-link" href="https://gwps.wi.mit.edu/" rel="noopener">数据</a> <a class="resource-link" href="https://pubmed.ncbi.nlm.nih.gov/35688146/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>大内存单细胞工作站；模型训练建议GPU (single-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>见论文、数据门户及仓库</li>
      <li><strong>已知限制：</strong>以细胞系和转录组读数为主，不能代表完整生理背景。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="norman-2019" data-search="组合crispr扰动中的基因程序 exploring genetic interaction manifolds constructed from rich single-cell phenotypes 组合扰动 single perturbation prediction, combinatorial perturbation scrna-seq genetic-activation k562细胞中的单基因与双基因激活" data-recommendation="core" data-status="peer-reviewed" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#norman-2019">组合CRISPR扰动中的基因程序</a></h2>
      <p class="resource-card__english">Exploring Genetic Interaction Manifolds Constructed from Rich Single-Cell Phenotypes · 2019 · 组合扰动</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--core">必读</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--data-only">仅数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">提供广泛使用的Norman单基因和双基因Perturb-seq数据，是本项目入门实践的真实数据来源。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>single perturbation prediction, combinatorial perturbation</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>genetic-activation</dd>
    <dt>物种/背景</dt><dd>human；K562细胞中的单基因与双基因激活</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1126/science.aax4438" rel="noopener">论文</a> <a class="resource-link" href="https://dataverse.harvard.edu/dataverse/gears" rel="noopener">数据</a> <a class="resource-link" href="https://github.com/snap-stanford/GEARS" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>CPU可分析；深度模型训练建议GPU (single-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>见Harvard Dataverse数据条款</li>
      <li><strong>已知限制：</strong>单一细胞系，组合结构与CRISPRa背景限制外推。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="perturb-seq-dixit-2016" data-search="perturb-seq perturb-seq dissecting molecular circuits with scalable single-cell rna profiling of pooled genetic screens 扰动实验 perturbation profiling, regulatory circuit discovery scrna-seq genetic-knockout k562与免疫相关细胞系统" data-recommendation="core" data-status="peer-reviewed" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#perturb-seq-dixit-2016">Perturb-seq</a></h2>
      <p class="resource-card__english">Perturb-Seq Dissecting Molecular Circuits with Scalable Single-Cell RNA Profiling of Pooled Genetic Screens · 2016 · 扰动实验</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--core">必读</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--data-only">仅数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">将pooled CRISPR筛选和单细胞RNA测序结合，为状态转换与因果响应建模提供实验基础。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>perturbation profiling, regulatory circuit discovery</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>genetic-knockout</dd>
    <dt>物种/背景</dt><dd>human, mouse；K562与免疫相关细胞系统</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1016/j.cell.2016.11.038" rel="noopener">论文</a> <a class="resource-link" href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE90063" rel="noopener">数据</a> <a class="resource-link" href="https://pubmed.ncbi.nlm.nih.gov/27984732/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>单细胞分析工作站 (unknown)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>GEO数据使用条款</li>
      <li><strong>已知限制：</strong>早期数据规模和实验背景有限；guide赋值与技术噪声需单独处理。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="uce-2026" data-search="通用细胞嵌入uce universal cell embedding provides a foundation model for cell biology 跨物种表征 cell embedding, cross-species integration, cell annotation scrna-seq, protein none 跨物种单细胞转录组" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq|protein">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#uce-2026">通用细胞嵌入UCE</a></h2>
      <p class="resource-card__english">Universal Cell Embedding Provides a Foundation Model for Cell Biology · 2026 · 跨物种表征</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--weights-and-code">权重＋代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">利用蛋白语言模型表示基因并学习跨物种细胞嵌入，重点展示零样本与新物种泛化。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>cell embedding, cross-species integration, cell annotation</dd>
    <dt>模态</dt><dd>scRNA-seq, protein</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>multi-species；跨物种单细胞转录组</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41586-026-10689-z" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/snap-stanford/UCE" rel="noopener">代码</a> <a class="resource-link" href="https://figshare.com/articles/dataset/Universal_Cell_Embeddings_Model_Files/24320806" rel="noopener">权重</a> <a class="resource-link" href="https://github.com/snap-stanford/UCE" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>大内存与GPU推荐 (single-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>见官方仓库与模型文件</li>
      <li><strong>已知限制：</strong>通用嵌入不等于状态转换模型；不同物种基因注释质量影响结果。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="scimilarity-2025" data-search="scimilarity细胞图谱检索 a cell atlas foundation model for scalable search of similar human cells 细胞检索 cell retrieval, cell annotation, atlas mapping scrna-seq none 多组织人类细胞图谱与独立研究" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#scimilarity-2025">SCimilarity细胞图谱检索</a></h2>
      <p class="resource-card__english">A Cell Atlas Foundation Model for Scalable Search of Similar Human Cells · 2025 · 细胞检索</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--weights-and-code">权重＋代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">通过度量学习在数千万细胞图谱中检索相似状态，并提供表示置信度和可追溯参考。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>cell retrieval, cell annotation, atlas mapping</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human；多组织人类细胞图谱与独立研究</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41586-024-08411-y" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/Genentech/scimilarity" rel="noopener">代码</a> <a class="resource-link" href="https://zenodo.org/records/10685499" rel="noopener">权重</a> <a class="resource-link" href="https://github.com/Genentech/scimilarity" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>CPU可检索；大图谱构建需要较大内存 (cpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>Apache-2.0；数据和权重另见发布页</li>
      <li><strong>已知限制：</strong>表征和检索不是因果扰动模拟；训练图谱覆盖决定置信度。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="tahoe-100m-2025" data-search="tahoe-100m扰动图谱 tahoe-100m a giga-scale single-cell perturbation atlas for context-dependent gene function and cellular modeling 化学扰动图谱 drug response, cross-context prediction, representation learning scrna-seq chemical 50个癌细胞系和多剂量小分子处理" data-recommendation="recommended" data-status="preprint" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#tahoe-100m-2025">Tahoe-100M扰动图谱</a></h2>
      <p class="resource-card__english">Tahoe-100M A Giga-Scale Single-Cell Perturbation Atlas for Context-Dependent Gene Function and Cellular Modeling · 2025 · 化学扰动图谱</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--preprint">预印本</span><span class="resource-badge resource-badge--data-only">仅数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">约一亿细胞、上千药物剂量条件和五十个癌细胞系，为跨背景化学扰动建模提供大规模训练数据。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>drug response, cross-context prediction, representation learning</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>chemical</dd>
    <dt>物种/背景</dt><dd>human；50个癌细胞系和多剂量小分子处理</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1101/2025.02.20.639398" rel="noopener">论文</a> <a class="resource-link" href="https://huggingface.co/datasets/tahoebio/Tahoe-100M" rel="noopener">数据</a> <a class="resource-link" href="https://www.biorxiv.org/content/10.1101/2025.02.20.639398v3" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>全量使用需要分布式存储与计算；子集可单机处理 (unknown)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>见Hugging Face数据卡</li>
      <li><strong>已知限制：</strong>癌细胞系和24小时转录响应不能覆盖原代组织、长期功能或临床反应。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="scfoundation-2024" data-search="scfoundation large-scale foundation model on single-cell transcriptomics 单细胞基础模型 cell representation, cell annotation, perturbation prediction scrna-seq none 大规模人类转录组图谱" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#scfoundation-2024">scFoundation</a></h2>
      <p class="resource-card__english">Large-Scale Foundation Model on Single-Cell Transcriptomics · 2024 · 单细胞基础模型</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--weights-and-code">权重＋代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">覆盖全转录组维度并在超过五千万细胞上预训练，用于细胞和基因层下游任务。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>cell representation, cell annotation, perturbation prediction</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human；大规模人类转录组图谱</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41592-024-02305-7" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/biomap-research/scFoundation" rel="noopener">代码</a> <a class="resource-link" href="https://github.com/biomap-research/scFoundation" rel="noopener">权重</a> <a class="resource-link" href="https://github.com/biomap-research/scFoundation" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>大模型推理/微调建议GPU (single-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>见官方仓库与模型说明</li>
      <li><strong>已知限制：</strong>计算和输入预处理较重；对任务专用基线的增益需独立验证。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="scgpt-2024" data-search="scgpt scgpt toward building a foundation model for single-cell multi-omics using generative ai 单细胞基础模型 cell annotation, integration, gene network, perturbation prediction scrna-seq, multiome none 大规模人类单细胞与多组学数据" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq|multiome">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#scgpt-2024">scGPT</a></h2>
      <p class="resource-card__english">scGPT Toward Building a Foundation Model for Single-Cell Multi-omics Using Generative AI · 2024 · 单细胞基础模型</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--weights-and-code">权重＋代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">用生成式Transformer统一多个单细胞任务，是单细胞基础模型路线的代表工作。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>cell annotation, integration, gene network, perturbation prediction</dd>
    <dt>模态</dt><dd>scRNA-seq, multiome</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human；大规模人类单细胞与多组学数据</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41592-024-02201-0" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/bowang-lab/scGPT" rel="noopener">代码</a> <a class="resource-link" href="https://huggingface.co/bowanglab/scGPT" rel="noopener">权重</a> <a class="resource-link" href="https://scgpt.readthedocs.io/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>单GPU推理与微调；预训练需要多GPU (multi-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>MIT；模型与数据另见模型卡</li>
      <li><strong>已知限制：</strong>多任务结果依赖不同微调设置；预训练重叠、基线和扰动代码需逐任务核查。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="cellot-2023" data-search="cellot：神经最优传输预测扰动分布 learning single-cell perturbation responses using neural optimal transport 分布状态转换 perturbation prediction, distribution modeling scrna-seq, imaging chemical 药物、细胞因子和成像扰动数据" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq|imaging">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#cellot-2023">CellOT：神经最优传输预测扰动分布</a></h2>
      <p class="resource-card__english">Learning Single-Cell Perturbation Responses Using Neural Optimal Transport · 2023 · 分布状态转换</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">学习控制细胞分布到扰动后分布的最优传输映射，而非只预测平均表达。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>perturbation prediction, distribution modeling</dd>
    <dt>模态</dt><dd>scRNA-seq, imaging</dd>
    <dt>扰动</dt><dd>chemical</dd>
    <dt>物种/背景</dt><dd>human, mouse；药物、细胞因子和成像扰动数据</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41592-023-01969-x" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/bunnech/cellot" rel="noopener">代码</a> <a class="resource-link" href="https://github.com/bunnech/cellot" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>单 GPU 推荐 (single-gpu)</li>
      <li><strong>证据阶段：</strong>retrospective</li>
      <li><strong>许可证：</strong>MIT</li>
      <li><strong>已知限制：</strong>最优传输的最小代价假设并不保证真实细胞配对或分子机制正确。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="multivi-2023" data-search="multivi：rna、染色质与蛋白的联合表示 multivi: deep generative model for the integration of multimodal data 多模态概率模型 multimodal integration, missing modality imputation scrna-seq, scatac-seq, protein, multiome none pbmc 等配对或马赛克式多组学数据" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq|scATAC-seq|protein|multiome">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#multivi-2023">MultiVI：RNA、染色质与蛋白的联合表示</a></h2>
      <p class="resource-card__english">MultiVI: Deep Generative Model for the Integration of Multimodal Data · 2023 · 多模态概率模型</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">联合建模配对和非配对的 RNA、ATAC 与蛋白数据，并补全缺失模态。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>multimodal integration, missing modality imputation</dd>
    <dt>模态</dt><dd>scRNA-seq, scATAC-seq, protein, multiome</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human；PBMC 等配对或马赛克式多组学数据</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41592-023-01909-9" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/scverse/scvi-tools" rel="noopener">代码</a> <a class="resource-link" href="https://docs.scvi-tools.org/en/stable/user_guide/models/multivi.html" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>单 GPU 推荐；百万细胞需要分块和充足内存 (single-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>BSD-3-Clause</li>
      <li><strong>已知限制：</strong>跨技术的缺失模态补全依赖共享生物结构，不能等同于真实测量。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="gears-2023" data-search="gears predicting transcriptional outcomes of novel multigene perturbations with gears 图扰动模型 single perturbation prediction, combinatorial perturbation scrna-seq none norman、adamson、dixit等细胞系扰动数据" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#gears-2023">GEARS</a></h2>
      <p class="resource-card__english">Predicting Transcriptional Outcomes of Novel Multigene Perturbations with GEARS · 2023 · 图扰动模型</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">利用基因知识图和共表达图预测新单基因与组合扰动，是Norman数据上的代表性任务模型。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>single perturbation prediction, combinatorial perturbation</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human；Norman、Adamson、Dixit等细胞系扰动数据</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41587-023-01905-6" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/snap-stanford/GEARS" rel="noopener">代码</a> <a class="resource-link" href="https://dataverse.harvard.edu/dataverse/gears" rel="noopener">数据</a> <a class="resource-link" href="https://github.com/snap-stanford/GEARS" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>GPU推荐；官方Colab部分流程需要较高显存 (single-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>MIT</li>
      <li><strong>已知限制：</strong>官方说明不支持仅单基因训练后可靠预测组合；跨细胞背景能力有限。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="geneformer-2023" data-search="geneformer transfer learning enables predictions in network biology 单细胞基础模型 cell classification, gene network, perturbation prioritization scrna-seq none 大规模人类单细胞转录组" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#geneformer-2023">Geneformer</a></h2>
      <p class="resource-card__english">Transfer Learning Enables Predictions in Network Biology · 2023 · 单细胞基础模型</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--weights-and-code">权重＋代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">使用按表达排序的基因token进行Transformer预训练，探索细胞分类、剂量敏感性和网络生物学迁移。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>cell classification, gene network, perturbation prioritization</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human；大规模人类单细胞转录组</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41586-023-06139-9" rel="noopener">论文</a> <a class="resource-link" href="https://huggingface.co/ctheodoris/Geneformer" rel="noopener">代码</a> <a class="resource-link" href="https://huggingface.co/ctheodoris/Geneformer" rel="noopener">权重</a> <a class="resource-link" href="https://huggingface.co/ctheodoris/Geneformer" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>推理可用单GPU；微调需求按模型版本变化 (single-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>见Hugging Face模型卡</li>
      <li><strong>已知限制：</strong>排序token丢失绝对表达；预训练收益与解释性需要任务级基线验证。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="cellrank-2022" data-search="cellrank：带不确定性的细胞命运映射 cellrank for directed single-cell fate mapping 细胞命运 fate mapping, trajectory inference, uncertainty scrna-seq, lineage none 发育、重编程和再生过程" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq|lineage">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#cellrank-2022">CellRank：带不确定性的细胞命运映射</a></h2>
      <p class="resource-card__english">CellRank for Directed Single-Cell Fate Mapping · 2022 · 细胞命运</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">结合表达相似性和 RNA velocity 构建马尔可夫链，估计终末状态与命运概率。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>fate mapping, trajectory inference, uncertainty</dd>
    <dt>模态</dt><dd>scRNA-seq, lineage</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human, mouse；发育、重编程和再生过程</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41592-021-01346-6" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/theislab/cellrank" rel="noopener">代码</a> <a class="resource-link" href="https://cellrank.readthedocs.io/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>CPU 可运行，大数据需稀疏线性代数资源 (cpu)</li>
      <li><strong>证据阶段：</strong>prospective</li>
      <li><strong>许可证：</strong>BSD-3-Clause</li>
      <li><strong>已知限制：</strong>方向性依赖 velocity 或其他核的可靠性，轨迹仍是群体层面的统计推断。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="scglue-2022" data-search="scglue：图连接的非配对多组学整合 multi-omics single-cell data integration and regulatory inference with graph-linked embedding 图多组学 multimodal integration, regulatory inference scrna-seq, scatac-seq, multiome none 非配对单细胞多组学及调控图" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq|scATAC-seq|multiome">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#scglue-2022">scGLUE：图连接的非配对多组学整合</a></h2>
      <p class="resource-card__english">Multi-Omics Single-Cell Data Integration and Regulatory Inference with Graph-Linked Embedding · 2022 · 图多组学</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">用调控先验图耦合组学专属自编码器，对齐非配对 RNA 与染色质数据。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>multimodal integration, regulatory inference</dd>
    <dt>模态</dt><dd>scRNA-seq, scATAC-seq, multiome</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human, mouse；非配对单细胞多组学及调控图</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41587-022-01284-4" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/gao-lab/GLUE" rel="noopener">代码</a> <a class="resource-link" href="https://scglue.readthedocs.io/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>单 GPU 推荐 (single-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>MIT</li>
      <li><strong>已知限制：</strong>结果受先验图质量和对抗对齐稳定性影响，跨模态邻近不代表调控因果。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="tangram-2021" data-search="tangram：单细胞与空间转录组对齐 deep learning and alignment of spatially resolved single-cell transcriptomes with tangram 空间映射 spatial mapping, deconvolution, gene imputation scrna-seq, spatial-transcriptomics none 匹配组织的单细胞参考与空间测量" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq|spatial-transcriptomics">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#tangram-2021">Tangram：单细胞与空间转录组对齐</a></h2>
      <p class="resource-card__english">Deep Learning and Alignment of Spatially Resolved Single-Cell Transcriptomes with Tangram · 2021 · 空间映射</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">学习单细胞参考到空间观测的概率映射，用于细胞定位、反卷积和基因补全。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>spatial mapping, deconvolution, gene imputation</dd>
    <dt>模态</dt><dd>scRNA-seq, spatial-transcriptomics</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human, mouse；匹配组织的单细胞参考与空间测量</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41592-021-01264-7" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/broadinstitute/Tangram" rel="noopener">代码</a> <a class="resource-link" href="https://tangram-sc.readthedocs.io/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>单 GPU 推荐 (single-gpu)</li>
      <li><strong>证据阶段：</strong>retrospective</li>
      <li><strong>许可证：</strong>BSD-3-Clause</li>
      <li><strong>已知限制：</strong>映射受参考细胞覆盖、共享基因和组织匹配程度影响，预测空间位置不是直接观测。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="totalvi-2021" data-search="totalvi：联合建模 rna 与表面蛋白 joint probabilistic modeling of single-cell multi-omic data with totalvi 多模态概率模型 multimodal integration, denoising, differential expression scrna-seq, protein none cite-seq 配对 rna 与表面蛋白" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq|protein">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#totalvi-2021">totalVI：联合建模 RNA 与表面蛋白</a></h2>
      <p class="resource-card__english">Joint Probabilistic Modeling of Single-Cell Multi-Omic Data with totalVI · 2021 · 多模态概率模型</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">以显式概率模型分离 CITE-seq 中的生物信号、蛋白背景和批次效应。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>multimodal integration, denoising, differential expression</dd>
    <dt>模态</dt><dd>scRNA-seq, protein</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human, mouse；CITE-seq 配对 RNA 与表面蛋白</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41592-020-01050-x" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/scverse/scvi-tools" rel="noopener">代码</a> <a class="resource-link" href="https://docs.scvi-tools.org/en/stable/user_guide/models/totalvi.html" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>小数据可用 CPU，训练推荐单 GPU (single-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>BSD-3-Clause</li>
      <li><strong>已知限制：</strong>依赖成对测量及正确的批次和蛋白背景设定，潜变量不能直接解释为机制。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="cpa-2021" data-search="组合扰动自编码器 predicting cellular responses to complex perturbations in high-throughput screens 组合扰动 drug response, dose response, combinatorial perturbation scrna-seq chemical 药物与遗传扰动的高通量单细胞筛选" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#cpa-2021">组合扰动自编码器</a></h2>
      <p class="resource-card__english">Predicting Cellular Responses to Complex Perturbations in High-Throughput Screens · 2021 · 组合扰动</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-only">仅代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">CPA把基础状态、扰动与协变量解耦，用于药物、剂量和组合条件的响应预测。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>drug response, dose response, combinatorial perturbation</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>chemical</dd>
    <dt>物种/背景</dt><dd>human；药物与遗传扰动的高通量单细胞筛选</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.15252/msb.202211517" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/theislab/cpa" rel="noopener">代码</a> <a class="resource-link" href="https://cpa-tools.readthedocs.io/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>GPU推荐 (single-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>BSD-3-Clause</li>
      <li><strong>已知限制：</strong>解耦与可加性假设需针对具体数据验证；跨背景表现依赖覆盖。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="waddington-ot-2019" data-search="waddington-ot：用最优传输连接时间点 optimal-transport analysis of single-cell gene expression identifies developmental trajectories 细胞动力学 trajectory inference, population dynamics scrna-seq, lineage none 重编程时间序列单细胞转录组" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq|lineage">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#waddington-ot-2019">Waddington-OT：用最优传输连接时间点</a></h2>
      <p class="resource-card__english">Optimal-Transport Analysis of Single-Cell Gene Expression Identifies Developmental Trajectories · 2019 · 细胞动力学</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-and-data">代码＋数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">用带增殖约束的最优传输连接不同时间点的细胞分布，估计祖先和后代关系。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>trajectory inference, population dynamics</dd>
    <dt>模态</dt><dd>scRNA-seq, lineage</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>mouse；重编程时间序列单细胞转录组</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1016/j.cell.2019.01.006" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/broadinstitute/wot" rel="noopener">代码</a> <a class="resource-link" href="https://broadinstitute.github.io/wot/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>CPU 可运行，中大型数据需要高内存 (cpu)</li>
      <li><strong>证据阶段：</strong>retrospective</li>
      <li><strong>许可证：</strong>BSD-3-Clause</li>
      <li><strong>已知限制：</strong>依赖离散时间点、代价函数和增殖估计，不提供真实细胞逐一配对。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="scgen-2019" data-search="scgen扰动响应预测 scgen predicts single-cell perturbation responses 条件生成 perturbation prediction, cross-cell-type transfer scrna-seq none 多个免疫与细胞系扰动数据" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="scRNA-seq">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#scgen-2019">scGen扰动响应预测</a></h2>
      <p class="resource-card__english">scGen Predicts Single-Cell Perturbation Responses · 2019 · 条件生成</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-only">仅代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">在VAE潜在空间中用状态差向量预测未见细胞背景响应，是早期可解释状态转换基线。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>perturbation prediction, cross-cell-type transfer</dd>
    <dt>模态</dt><dd>scRNA-seq</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human, mouse；多个免疫与细胞系扰动数据</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/s41592-019-0494-8" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/theislab/scgen" rel="noopener">代码</a> <a class="resource-link" href="https://scgen.readthedocs.io/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>单GPU或CPU小数据 (single-gpu)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>Apache-2.0</li>
      <li><strong>已知限制：</strong>潜在空间线性效应假设难以覆盖复杂分布与组合响应。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="codex-2018" data-search="codex：高度复用的组织蛋白成像 deep profiling of mouse splenic architecture with codex multiplexed imaging 空间蛋白成像 spatial proteomics, cell neighborhood analysis imaging, protein none 脾脏等组织的多重蛋白成像" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="imaging|protein">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#codex-2018">CODEX：高度复用的组织蛋白成像</a></h2>
      <p class="resource-card__english">Deep Profiling of Mouse Splenic Architecture with CODEX Multiplexed Imaging · 2018 · 空间蛋白成像</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--data-only">仅数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">通过循环 DNA 条形码抗体成像解析组织中的细胞类型、邻域与空间结构。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>spatial proteomics, cell neighborhood analysis</dd>
    <dt>模态</dt><dd>imaging, protein</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>mouse；脾脏等组织的多重蛋白成像</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1016/j.cell.2018.07.010" rel="noopener">论文</a> <a class="resource-link" href="https://pubmed.ncbi.nlm.nih.gov/30078711/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>高分辨图像需要高存储和并行处理 (single-gpu)</li>
      <li><strong>证据阶段：</strong>prospective</li>
      <li><strong>许可证：</strong>Article and data terms apply</li>
      <li><strong>已知限制：</strong>抗体面板限制可观察状态，分割和批次校正会显著影响下游邻域结论。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="cell-painting-2016" data-search="cell painting：高内涵形态学表型协议 cell painting, a high-content image-based assay for morphological profiling 成像实验技术 morphological profiling, phenotypic screening imaging genetic-knockout, chemical 培养细胞高内涵成像筛选" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="imaging">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#cell-painting-2016">Cell Painting：高内涵形态学表型协议</a></h2>
      <p class="resource-card__english">Cell Painting, a High-Content Image-Based Assay for Morphological Profiling · 2016 · 成像实验技术</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--documentation-only">仅文档</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">用多通道荧光染色提取细胞器与形态特征，支持遗传或化学扰动筛选。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>morphological profiling, phenotypic screening</dd>
    <dt>模态</dt><dd>imaging</dd>
    <dt>扰动</dt><dd>genetic-knockout, chemical</dd>
    <dt>物种/背景</dt><dd>human；培养细胞高内涵成像筛选</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1038/nprot.2016.105" rel="noopener">论文</a> <a class="resource-link" href="https://broadinstitute.github.io/cellpainting-gallery/overview.html" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>图像处理可从 CPU 扩展到 GPU 集群 (single-gpu)</li>
      <li><strong>证据阶段：</strong>prospective</li>
      <li><strong>许可证：</strong>Protocol and third-party data terms apply</li>
      <li><strong>已知限制：</strong>形态相似不等同于靶点或机制相同，批次和板位效应必须单独校正。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="merfish-2015" data-search="merfish：高复用单细胞空间 rna 成像 spatially resolved, highly multiplexed rna profiling in single cells 空间实验技术 spatial profiling, subcellular localization spatial-transcriptomics, imaging none 原位 rna 分子定位" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="spatial-transcriptomics|imaging">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#merfish-2015">MERFISH：高复用单细胞空间 RNA 成像</a></h2>
      <p class="resource-card__english">Spatially Resolved, Highly Multiplexed RNA Profiling in Single Cells · 2015 · 空间实验技术</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--data-only">仅数据</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">以纠错条形码和多轮成像在单细胞内同时定位大量 RNA 分子。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>spatial profiling, subcellular localization</dd>
    <dt>模态</dt><dd>spatial-transcriptomics, imaging</dd>
    <dt>扰动</dt><dd>none</dd>
    <dt>物种/背景</dt><dd>human, mouse；原位 RNA 分子定位</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1126/science.aaa6090" rel="noopener">论文</a> <a class="resource-link" href="https://vizgen.com/data-release-program/" rel="noopener">数据</a> <a class="resource-link" href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4662681/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>数据分析可用 CPU；原始图像需要高存储 (cpu)</li>
      <li><strong>证据阶段：</strong>prospective</li>
      <li><strong>许可证：</strong>Article and dataset terms apply</li>
      <li><strong>已知限制：</strong>靶向面板、分割和解码误差会限制覆盖度；不同版本实验不可直接混合。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
<article class="resource-card" id="whole-cell-karr-2012" data-search="首个全细胞计算模型 a whole-cell computational model predicts phenotype from genotype 机理虚拟细胞 whole-cell simulation, genotype-to-phenotype bulk-omics chemical 最小细菌细胞的机理与数据整合模型" data-recommendation="recommended" data-status="peer-reviewed" data-modalities="bulk-omics">
  <div class="resource-card__header">
    <div>
      <h2><a class="headerlink" href="#whole-cell-karr-2012">首个全细胞计算模型</a></h2>
      <p class="resource-card__english">A Whole-Cell Computational Model Predicts Phenotype from Genotype · 2012 · 机理虚拟细胞</p>
    </div>
    <div class="resource-badges"><span class="resource-badge resource-badge--recommended">推荐</span><span class="resource-badge resource-badge--peer-reviewed">同行评审</span><span class="resource-badge resource-badge--code-only">仅代码</span><span class="resource-badge resource-badge--verified">已核验</span></div>
  </div>
  <p class="resource-card__summary">整合多类细胞过程模拟支原体基因型到表型，是理解传统whole-cell modeling及其参数成本的关键工作。</p>
  <dl class="resource-card__facts">
    <dt>任务</dt><dd>whole-cell simulation, genotype-to-phenotype</dd>
    <dt>模态</dt><dd>bulk-omics</dd>
    <dt>扰动</dt><dd>chemical</dd>
    <dt>物种/背景</dt><dd>bacteria；最小细菌细胞的机理与数据整合模型</dd>
  </dl>
  <div class="resource-card__links"><a class="resource-link" href="https://doi.org/10.1016/j.cell.2012.05.044" rel="noopener">论文</a> <a class="resource-link" href="https://github.com/CovertLab/WholeCell" rel="noopener">代码</a> <a class="resource-link" href="https://www.wholecell.org/" rel="noopener">主页</a></div>
  <details class="resource-card__details">
    <summary>复现条件、许可证与限制</summary>
    <ul>
      <li><strong>计算需求：</strong>传统模拟工作站；以官方版本说明为准 (unknown)</li>
      <li><strong>证据阶段：</strong>in-silico</li>
      <li><strong>许可证：</strong>见WholeCell官方仓库</li>
      <li><strong>已知限制：</strong>物种和过程高度特定，不能直接外推到复杂人类细胞。</li>
      <li><strong>最后核验：</strong>2026-07-28 · 已核验</li>
    </ul>
  </details>
</article>
</div>
<p class="catalog-empty" hidden>没有匹配的资源，请调整筛选条件。</p>
