# 扰动响应预测 Notebook

前六章按顺序阅读，均使用小型合成 AnnData，离线、无 GPU 可运行：

1. 问题定义与反事实状态；
2. AnnData 契约 v2、QC 与实验单位；
3. 扰动级拆分和控制细胞防泄漏；
4. 控制均值、平均效应、基因身份 Ridge；
5. 明确标记为非生物表示的标签哈希 MLP 冒烟测试；
6. 误差分析、预测工件和 Arc 指标映射。

`gears-norman-colab.ipynb` 是独立的进阶路径，需要 Colab GPU、网络下载以及
`cell-gears==0.1.2`、`cell-eval==0.8.1`。它生成细胞级预测与运行清单，不把条件均值
重复成伪细胞。

```bash
pip install -e ".[notebooks]"
jupyter lab notebooks/perturbation-response
```

合成数据只验证代码路径，不提供生物学证据。真实数据和运行产物均不提交到仓库。
