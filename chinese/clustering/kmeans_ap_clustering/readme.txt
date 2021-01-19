********************************************** 
 
Version: Python 3.9.0 
IDE: Jupyter Notebook
@author: 何灿 Sany
Time: 2020/07/17

**********************************************

使用库：
numpy、pandas、matplolib、sklearn

实现功能：
1.使用k-means和AP进行聚类，前者使用8种评分标准，后者有7种
2.画出轮廓图表
3.比较KMeans和MiniBatchKmeans 运行时间
4.使用GridSearchCV对两类算法进行参数最优查找，及保存最优模型
5.k-means使用PCA降维后可视化
6.以三种评分探讨K-means的两种初始化方法(k-means++和random)及可视化
7.实现基于分类结果的分层抽样

数据集：
【data.xlsx】：数据集中的TRUE VALUE一列为实际类别信息
【data_after_clustering.csv】：经过【kmeans_ap_clustering.ipynb】聚类获得的，含聚类结果的数据集


评分标准(具体使用可查阅相关资料)：
聚类评估主要包括：估计聚类趋势、确定数据集中的簇数、测定聚类质量。
1.k-means自身的评价指标
Mean Inertia Score: 簇中某一点到簇中距离的和
2.外部评价指标：需要实际类别信息（5种）
Homogeneity Score:同质性，取值范围为[0,1]，每一个聚出的类仅包含一个类别的程度度量。
Completeness Score:完整性，取值范围为[0,1]，每一个类别被指向相同聚出的类的程度度量。
V Measure Score:同质性和完整性的调和平均，取值范围为[0,1]
Adjusted Rand Score: 调整兰德系数，取值范围为[-1,1],值越大意味着聚类结果与真实情况越吻合
Adjusted Mutual Information Score:调整互信息，取值范围为[-1,1]，值越大意味着聚类结果与真实情况越吻合
3.内部指标：不需要实际类别信息(2种，主要是这两种作为评分标准)
Calinski Harabasz Score: 值越大说明聚类效果越好
Silhouette Score: 轮廓系数，取值范围为[-1,1]，同类别样本越距离相近且不同类别样本距离越远，分数越高。


超参数调节：
1.sklean.clustering.KMeans
n_clusters:可调，簇中心的数量，默认为8
init:可调，两种，初始化方法
n_init:可调，迭代次数，默认为10
2.sklean.clustering.affinity_propagation
Preference：可调，为负值
Damping：可调，衰减系数，范围为[0,1]，默认为0.5
3.sklearn.model_selection.GridSearchCV
cv:可调，交叉验证次数，默认为5
scoring:可调，根据模型类别选择sklearn.metrics里面的评价标准
4.sklearn.decomposition.PCA
n_components:可调，降到的维度


需要做的进一步工作：
根据实际需要，选取聚类的评分标准,如对于KMeans而言，主要看轮廓系数和inertia

注意：
1.【data.xlsx】、【kmeans_ap_clustering.ipynb】需位于同一目录下
2.【data.xlsx】与【data_after_clustering.csv】是同一份数据，区别在于后者含聚类结果

*********************************************

