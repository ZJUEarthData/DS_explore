********************************************** 
 
Version: Python 3.7.6 
IDE: Jupyter Notebook
@author: 何灿 Sany
Time: 2020/07/28

**********************************************
Package:
numpy、pandas、matplotlib、sklearn

Realiztion:
1. Stratified sampling based on clustering results (eg. kmeans)
2. Contrast pure random sampling with stratified sampling (take the multi-classifier constructed by LogisticRegression as an example)
3. Construct a cross-validation class based on stratified sampling (take the multi-classifier constructed by SGD Classifier and the Linear Regressor as examples)

Dataset:
【Test_2.xlsx】: The TRUE VALUE column in the data set is the actual category information
【Test2_result.csv】: A data set containing clustering results obtained through clustering【clustering_test_202007121.ipynb】

Grading:
It can be evaluated by the score of classification (or regression) model over stratified sampling/pure random sampling

Further work:
You can apply it into the classification or regression model (such as neural network, SVM, linear, polynomial, etc.)

Note:
1. For the cross-validation of stratified sampling, there is no built-in library like 'cross_val_score' in the python package library, so you can construct the corresponding class yourself
2. The complete data set refers to the original data set that has not been divided (layered or purely random)


使用库：
numpy、pandas、matplolib、sklearn

实现功能：
1.基于聚类结果的分层抽样（以kmeans为例）
2.进行纯随机抽样和分层抽样对比（以LogisticRegression构造的多元分类器为例）
3.构造一个基于分层抽样的交叉验证的类（以SGDClassifier构造的多元分类器和LinearRegression构造的线性回归器为例）

数据集：
【Test_2.xlsx】：数据集中的TRUE VALUE一列为实际类别信息
【test2_result.csv】：经过【clustering_test_202007121.ipynb】聚类获得的，含聚类结果的数据集

评分标准：
可通过分层取样/纯随机取样+分类（或回归）的模型的评分来比对

进一步工作：
可自行DIY到分类或回归的模型中去（如神经网络、SVM、线性、多项式等）

注意：
1.对于分层取样的交叉验证，python的库里没有像cross_val_score一样建好的库可调，因此可自己构造相应的类
2.完整数据集是指没有经过划分（分层或纯随机）的原始数据集

*********************************************

