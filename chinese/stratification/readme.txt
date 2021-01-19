********************************************** 
 
Version: Python 3.9.0 
IDE: Jupyter Notebook
@author: 何灿 Sany
Time: 2020/07/28

**********************************************
使用库：
numpy、pandas、matplolib、sklearn

实现功能：
1.基于聚类结果的分层抽样（以kmeans为例）
2.进行纯随机抽样和分层抽样对比（以LogisticRegression构造的多元分类器为例）
3.构造一个基于分层抽样的交叉验证的类（以SGDClassifier构造的多元分类器和LinearRegression构造的线性回归器为例）

数据集：
【data.xlsx】：数据集中的TRUE VALUE一列为实际类别信息
【data_after_clustering.csv】：经过【kmeans_ap_clustering.ipynb】聚类获得的，含聚类结果的数据集

评分标准：
可通过分层取样/纯随机取样+分类（或回归）的模型的评分来比对

进一步工作：
可自行DIY到分类或回归的模型中去（如神经网络、SVM、线性、多项式等）

注意：
1.对于分层取样的交叉验证，python的库里没有像cross_val_score一样建好的库可调，因此可自己构造相应的类
2.完整数据集是指没有经过划分（分层或纯随机）的原始数据集
3.【data.xlsx】与【data_after_clustering.csv】是同一份数据，区别在于后者含聚类结果

*********************************************

