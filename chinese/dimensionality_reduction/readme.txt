********************************************** 
 
Version: Python 3.7.6 
IDE: Jupyter Notebook
@author: 何灿 Sany
Time: 2020/07/23
Email: sanyhew1097618435@163.com
Related Video: https://www.youtube.com/watch?v=J9Do8FD_uyA

**********************************************

使用库：
numpy、pandas、matplolib、sklearn

实现功能：
1.普通PCA（线性投影）：特征空间的主成分轴表达式，重构数据与原数据的平方距离、二维可视化
2.核PCA（非线性投影）：四种核手段（linear,rbf,poly,sigmoid）、平方距离、二维可视化
3.针对大型数据集，可使用增量PCA和随机PCA，比较普通PCA、增量PCA、随机PCA运行时间
4.通过GridSearchCV，配合分类（或回归）模型的评分查找核PCA最优参数
5.流形学习（非线性投影）：常见的四种类型、二维可视化

数据集：
【dataset.xlsx】：数据集中的TRUE VALUE一列为实际类别信息

评分标准(具体使用可查阅相关资料)：
1.可通过重构数据与原数据的平方距离
2.可通过降维+分类（或回归）的模型的评分来确定模型好坏

超参数调节（可参考官方文档找可调超参数，下面所列超参数为【dimensionality_reduction.ipynb】所涉及）：
1.sklean.decomposition.PCA
n_components：可调，需要降至的维度
2.sklean.decomposition.KernelPCA
n_components：可调，需要降至的维度
kernel：可调，核技巧（6种 linear、poly、rbf、sigmoid、cosine、precomputed）
Gamma：可调，用于poly、rbf和sigmoid四种核技巧，取值范围为0~1，默认为1/特征数
coef：可调，用于poly，sigmoid两种核技巧，取值范围为0~1，默认为1
Degree：可调，用于poly核技巧，默认为3
3.sklearn.model_selection.GridSearchCV
cv：可调，交叉验证次数，默认为5
scoring：可调，根据模型类别选择sklearn.metrics里面的评价标准
params：可改动params字典
4.sklearn.manifold.LocallyLinearEmbedding
n_components:可调，降到的维度
n_neighbors:可调
5.sklearn.manifold.Isomap, TSNE, MDS
n_components:可调，降到的维度

需要做的进一步工作：
如果数据量大的话，可以采用随机PCA和增量PCA算法，降低运行时间和存储内存

注意：
降维同聚类都可以配合回归或分类模型使用，可DIY代码块，使用前需进行标准化处理

*********************************************

