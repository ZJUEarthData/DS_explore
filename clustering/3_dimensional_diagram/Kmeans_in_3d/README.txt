********************************************** 
 
Version: Python 3.7.6 
IDE: Pycharm
@author: 王盛鑫
Time: 2020/08/28

**********************************************

使用库：
matplotlib、sklearn、mpl_toolkits、pandas、numpy

实现功能：
对Kmeans的模型差异三维化比较，差异性数据加载到Excel，任选3个维度投射到三维空间

数据集：
【test4.xlsx】：数据集中的TRUE VALUE一列为实际类别信息

参数调节：
clusters：即我们的k值，和KMeans类的n_clusters意义一样。 
model1：模型，具体调参参照Kmeans的调参
model2：同上
newphoto： 
True 降维之后的三维显示
False 抽维度显示（可以使用W1_,W2_,W3_）


draw3D函数调参：
X1：数据集（不含实际分类标签）
layout：布局，223，代表划分成2*2，子图3
title：主题，图片名
c：色彩或颜色序列
s：点的大小
alpha：阿尔法通道（默认None）
cmap：Colormap（默认None）
core：
默认（None）画原始图
core == True 绘制聚类中心点
core == False 绘制差异点
core_cluster_centers：默认（None），聚类中心点
W1_:默认0 抽维度的时候可以修改
W2_：默认1，抽维度的时候可以修改
W3_：默认2，抽维度的时候可以修改

需要做的进一步工作：
对其他聚类方法进行补充和融合

注意：
本文件在.py运行后，可以详细使用三维图，在Jupyter Notebook中使用，反而失去了三维性
cm是聚类点的颜色，较为浅色，默认只有6种颜色，可以根据自己的需要加
cm2是聚类中心点的颜色，较重，默认只有6种颜色，可以根据自己的需要加
newphoto：决定显示降维之后的三维图还是抽维度单位图，我目前没办法统一两个实现，否则同时出现会让第二张图出问题
#Excel中True代表两个模型预测的是相同的，False代表不相同

*********************************************
