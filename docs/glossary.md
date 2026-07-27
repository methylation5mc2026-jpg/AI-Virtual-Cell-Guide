---
title: 术语表
summary: AIVC、实验设计、单细胞、多模态、扰动建模与评测中的中英文术语。
level: beginner
prerequisites: []
estimated_time: 35 分钟
last_reviewed: 2026-07-28
---

# 术语表

术语按概念分组。第一次出现时保留英文；相近术语在不同论文中可能有不同定义，应以具体实验和模型接口为准。

## AIVC 与生物概念

| 术语 | 英文 | 简明解释 |
|---|---|---|
| 人工智能虚拟细胞 | AI Virtual Cell, AIVC | 从多模态数据学习细胞状态、变化并支持可检验虚拟实验的计算系统 |
| 传统虚拟细胞 | Mechanistic virtual cell | 基于已知反应、方程和参数模拟细胞过程的模型 |
| 全细胞模型 | Whole-cell model | 尝试在统一系统中连接细胞内多个功能模块 |
| 中心法则 | Central dogma | DNA、RNA 与蛋白信息流的基础框架，不代表单向静态流水线 |
| 基因调控网络 | Gene regulatory network, GRN | 基因、调控因子和候选调控关系组成的网络 |
| 通路 | Pathway | 共同参与某个分子或细胞过程的一组反应和分子 |
| 细胞类型 | Cell type | 相对稳定的细胞身份分类 |
| 细胞状态 | Cell state | 给定时间和测量空间中细胞特征的近似描述 |
| 细胞背景 | Cellular context | 细胞类型、供体、组织、疾病、环境和实验条件 |
| 表型 | Phenotype | 可观测的分子、形态、功能或行为特征 |
| 机制 | Mechanism | 能解释干预如何经中间过程导致结果的可检验关系 |
| 细胞命运 | Cell fate | 细胞未来可能达到的稳定或终末状态 |

## 实验设计与因果

| 术语 | 英文 | 简明解释 |
|---|---|---|
| 扰动 | Perturbation | 基因、药物、环境或其他可控干预 |
| 对照 | Control | 与目标扰动比较的匹配未处理或阴性条件 |
| 阳性控制 | Positive control | 应产生已知效应，用于检验实验能否检测响应 |
| 生物重复 | Biological replicate | 独立生物样本、培养或实验单位 |
| 技术重复 | Technical replicate | 同一生物样本的重复测量 |
| 实验单位 | Experimental unit | 可被独立随机分配处理的最小单位 |
| 伪重复 | Pseudoreplication | 把非独立细胞错误当作独立重复 |
| 随机化 | Randomization | 随机分配处理以减少系统混杂 |
| 混杂 | Confounding | 同时关联处理和结果，产生替代解释的变量 |
| 选择偏差 | Selection bias | 纳入、存活或过滤过程改变了比较群体 |
| 因果效应 | Causal effect | 同一目标在不同干预下潜在结果的差异 |
| 反事实 | Counterfactual | 未实际观察到的另一干预条件下结果 |
| 可识别性 | Identifiability | 目标量能否由观测数据和假设唯一确定 |
| 脱靶效应 | Off-target effect | 干预影响非预期靶点或过程 |
| 剂量响应 | Dose response | 响应随干预剂量变化的关系 |
| 协同 | Synergy | 组合效应超过所选无相互作用基线 |

参见[实验单位、重复与设计](01-foundations/experimental-design.md)和[扰动数据与因果推断](01-foundations/causal-inference.md)。

## 数据与实验模态

| 术语 | 英文 | 简明解释 |
|---|---|---|
| 单细胞 RNA 测序 | scRNA-seq | 在单细胞分辨率测量 RNA 计数 |
| 单核 RNA 测序 | snRNA-seq | 从细胞核测量 RNA，适合部分难解离或冻存组织 |
| 单细胞 ATAC 测序 | scATAC-seq | 测量单细胞染色质可及性 |
| CITE-seq | Cellular Indexing of Transcriptomes and Epitopes | 同细胞联合测量 RNA 和抗体标签蛋白 |
| 多组学 | Multi-omics | 联合 RNA、染色质、蛋白、代谢或成像等模态 |
| Multiome | Single-cell multiome | 在同一细胞中配对测量多个组学层 |
| 空间转录组 | Spatial transcriptomics | 保留组织空间位置的 RNA 测量 |
| MERFISH | Multiplexed Error-Robust FISH | 通过多轮纠错成像定位大量 RNA 分子 |
| Cell Painting | Cell Painting | 多通道高内涵成像的细胞形态画像实验 |
| Perturb-seq | Perturb-seq | pooled 基因扰动与单细胞 RNA 测序结合的实验 |
| CRISPRi | CRISPR interference | 用失活 Cas 蛋白抑制基因转录 |
| CRISPRa | CRISPR activation | 用 CRISPR 系统激活基因表达 |
| UMI | Unique molecular identifier | 用于区分原始分子与扩增副本的标签 |
| 双细胞 | Doublet | 一个观测中混入两个或更多细胞 |
| 环境 RNA | Ambient RNA | 游离 RNA 被错误计入液滴或细胞 |
| 批次效应 | Batch effect | 与目标生物问题无关的系统技术差异 |
| 原始计数 | Raw counts | 比对和计数产生、未经归一化的非负整数矩阵 |
| 归一化 | Normalization | 调整深度或技术尺度以支持比较的过程 |
| 高变基因 | Highly variable genes, HVG | 在给定模型下变异较大的特征集合 |
| 伪总体 | Pseudobulk | 按重复、条件或样本聚合单细胞计数 |
| AnnData | AnnData | 保存矩阵、观测元数据、特征元数据和多层数据的容器 |
| OME-Zarr | OME Next-Generation File Format | 面向多尺度显微图像的云原生分块格式与元数据规范 |

参见[数据版图](02-data-and-experiments/index.md)。

## 模型与表示

| 术语 | 英文 | 简明解释 |
|---|---|---|
| 表征 | Representation | 对细胞、基因或分子的向量或结构编码 |
| 嵌入 | Embedding | 位于连续空间的学习表示 |
| 潜变量 | Latent variable | 未直接观测、由模型推断的变量 |
| 主成分分析 | Principal component analysis, PCA | 线性降维与方差分解方法 |
| 广义线性模型 | Generalized linear model, GLM | 通过链接函数建模非高斯响应的统计模型 |
| 变分自编码器 | Variational autoencoder, VAE | 用近似变分推断学习生成式潜变量模型 |
| Transformer | Transformer | 以注意力为核心的序列或集合模型架构 |
| 图神经网络 | Graph neural network, GNN | 沿图节点和边传播信息的模型 |
| 扩散模型 | Diffusion model | 通过逐步加噪和去噪学习生成分布 |
| 流匹配 | Flow matching | 学习连续向量场连接概率分布 |
| 最优传输 | Optimal transport, OT | 在代价约束下连接两个分布的方法 |
| RNA velocity | RNA velocity | 由剪接等信息估计短时间转录变化方向 |
| 基础模型 | Foundation model | 在大规模多样数据上预训练并迁移到多任务的模型 |
| 预训练 | Pretraining | 在下游任务前使用大规模数据学习参数 |
| 微调 | Fine-tuning | 用下游数据更新部分或全部预训练参数 |
| 线性探针 | Linear probe | 冻结表征后训练线性下游模型 |
| Token 化 | Tokenization | 把基因和值转换为模型离散输入的过程 |
| 掩码建模 | Masked modeling | 隐藏部分输入并要求模型恢复的预训练目标 |
| 条件生成 | Conditional generation | 在扰动、剂量或背景条件下生成结果状态 |
| 混合模型 | Hybrid model | 组合数据驱动模块与方程、网络或其他机理约束 |

参见[模型版图](03-models/index.md)。

## 任务、泛化与评测

| 术语 | 英文 | 简明解释 |
|---|---|---|
| 细胞注释 | Cell annotation | 为细胞预测类型或状态标签 |
| 数据整合 | Data integration | 对齐批次、来源或模态，同时保留目标生物差异 |
| 标签迁移 | Label transfer | 从参考数据向查询数据传播注释 |
| 状态转换 | State transition | 从初始状态和条件预测后续状态 |
| 轨迹推断 | Trajectory inference | 从快照或方向信息重建状态变化路径 |
| 谱系追踪 | Lineage tracing | 用遗传条形码或成像记录祖先—后代关系 |
| 虚拟实验 | Virtual experiment | 在模型中比较可执行干预并产生可检验假设 |
| 主动学习 | Active learning | 根据效用与不确定性选择下一批实验 |
| 数据泄漏 | Data leakage | 测试信息直接或间接进入训练、预处理或调参 |
| 分布外 | Out of distribution, OOD | 测试条件超出训练数据覆盖 |
| 扰动 OOD | Perturbation OOD | 测试扰动目标、剂量或组合未在训练出现 |
| 背景 OOD | Context OOD | 测试细胞类型、供体或组织未在训练出现 |
| 技术 OOD | Technical OOD | 测试批次、平台或实验室未在训练出现 |
| 差异表达 | Differential expression, DE | 比较条件间表达变化及其不确定性 |
| 平均绝对误差 | Mean absolute error, MAE | 预测与真实值绝对差的平均 |
| 变化相关 | Delta correlation | 减去控制状态后预测与真实变化的相关 |
| Top-DE overlap | Top differential-expression overlap | 预测和真实高变化基因集合的重合比例 |
| DES | Differential Expression Score | Arc 指标：衡量差异表达集合恢复 |
| PDS | Perturbation Discrimination Score | Arc 指标：衡量扰动预测的特异性 |
| MMD | Maximum mean discrepancy | 用核均值差异比较两个分布 |
| 校准 | Calibration | 预测置信度与实际正确率或区间覆盖相匹配 |
| 偶然不确定性 | Aleatoric uncertainty | 数据生成与测量噪声带来的不可约不确定性 |
| 认知不确定性 | Epistemic uncertainty | 模型或有限训练数据带来的可减少不确定性 |
| 拒识 | Abstention / rejection | 对低置信或未知输入不输出强制标签 |
| 消融实验 | Ablation study | 移除组件或信息源，检验其真实贡献 |
| 前瞻验证 | Prospective validation | 模型先给出预测，随后执行新的真实实验 |

参见[评测原则](05-evaluation/index.md)。

## 复现与治理

| 术语 | 英文 | 简明解释 |
|---|---|---|
| 数据集卡 | Dataset card | 记录数据来源、结构、许可、偏差和用途 |
| 模型卡 | Model card | 记录模型输入、输出、训练、评测和限制 |
| 运行清单 | Run manifest | 固定一次运行的数据、代码、环境、硬件和产物 |
| 校验和 | Checksum | 用摘要验证文件内容和版本 |
| 语义化版本 | Semantic versioning | 用主、次、修订号表达兼容性变化 |
| 可复现性 | Reproducibility | 相同数据和方法能否得到一致结果 |
| 可重复性 | Replicability | 独立实验或数据能否支持同一结论 |
| FAIR | Findable, Accessible, Interoperable, Reusable | 可发现、可访问、可互操作、可复用原则 |
| 数据治理 | Data governance | 管理许可、同意、访问、用途和责任的制度 |
| 证据等级 | Evidence stage | 从概念、计算、外部验证到前瞻实验和部署的分级 |

## 建议

遇到新术语时同时问三个问题：它指的是实验观测、模型内部量，还是评测代理？它的单位和粒度是什么？哪些结论不能由它单独支持？
