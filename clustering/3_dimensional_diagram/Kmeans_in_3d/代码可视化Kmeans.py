import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import pairwise_distances_argmin
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## 设置属性防止中文乱码
mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False

#读取数据集
df = pd.read_excel('E:/A/工作/聚类/聚类算法包ver3.0/聚类算法包/DBSCAN/test4.xlsx')
# 将真实的分类标签与特征分开
X = df.drop(['TRUE VALUE'], axis=1)
Y = df['TRUE VALUE']
labels = list(X.columns.values)
NX = np.array(X)

#降维处理
pca3 = PCA(n_components = 3)
X = pca3.fit_transform(X)


clusters = 4
###################################################################################
#构建model1算法
model1 = "Kmeans(kmeans++) K="+str(clusters)+" "
k_means1 = KMeans(init='k-means++', n_clusters=clusters, random_state=28)
k_means1.fit(X)  #训练模型
#构建model2算法
###################################################################################
model2 = "Kmeans(random) K="+str(clusters)+" "
k_means2 = KMeans(init='random', n_clusters=clusters, random_state=28)
k_means2.fit(X)
###################################################################################

#预测结果
km1_y_hat = k_means1.predict(X)
km2_y_hat = k_means2.predict(X)

print("###################################################################################")
##获取聚类中心点并聚类中心点进行排序
k_means_cluster_centers1 = k_means1.cluster_centers_
k_means_cluster_centers2 = k_means2.cluster_centers_
print (model1+"算法聚类中心点:\ncenter=", k_means_cluster_centers1)
print("###################################################################################")
print (model2+"算法聚类中心点:\ncenter=", k_means_cluster_centers2)
#使用欧几里得距离,返回的是X距离Y最近点的index，所以形状与X的形状一致。过程：挨个查找X列表中的点，返回该点距离最近Y点的index
#这样避免给同一种结果在两种模型是不同的标签
order = pairwise_distances_argmin(X=k_means_cluster_centers1,Y=k_means_cluster_centers2)
print("###################################################################################")
## 画图

fig = plt.figure(figsize=(14, 8), facecolor='w')
plt.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=0.9)
#点数多的时候，可以增加多种颜色，上面浅一点，下面重一点的颜色
cm = mpl.colors.ListedColormap(['#FFC2CC', '#C2FFCC', '#CCC2FF','#B0E0E6','#7FFFAA','#FFD700','#F0D700'])
cm2 = mpl.colors.ListedColormap(['#FF0000', '#00FF00', '#0000FF','#5F9EA0','#00FF7F','#DAA520','#FDD700'])

#plt.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=0.9)
def draw3D(X1,layout,title,c,s,W1=0,W2=1,W3=2,alpha=None,cmap=None,core=None,core_cluster_centers=None):
    ax = fig.add_subplot(layout, projection='3d')
    ax.scatter(X1[:, W1], X1[:, W2], X1[:, W3], alpha=alpha, c=c,s=s,cmap=cmap)  # 生成散点.利用c控制颜色序列,s控制大小
    if core == True:
        ax.scatter(core_cluster_centers[:, W1], core_cluster_centers[:, W2], core_cluster_centers[:, W3], c=range(clusters), s=60, cmap=cm2, edgecolors='none')
    if core == False:
        ax.scatter(X1[different, W1], X1[different, W2], X1[different, W3], c="#FF0000", s=15,edgecolors='none',marker="*")
    plt.title(title)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.grid(True)

# 获取两种算法预测不一致的样本数目
different = list(map(lambda x: x==-1,km1_y_hat))
for k in range(clusters):
    different += ((km1_y_hat == k) != (km2_y_hat == order[k]))
identic = np.logical_not(different)
different_nodes = len(list(filter(lambda x:x, different)))
notdifferent = (1-different).astype(np.bool)

###################################################################################
newphoto = False

#降维之后的显示
if newphoto==True:
    draw3D(X, 221, u'原始数据分布图', c=Y, s=6, cmap=cm)
    draw3D(X, 222, u'KMeans(Kmeans++)算法聚类结果图 clusters=' + u'' + str(clusters), c=km1_y_hat, s=6, cmap=cm, core=True,
           core_cluster_centers=k_means_cluster_centers1)
    draw3D(X, 223, u'KMeans(random) clusters=' + u'' + str(clusters), c=km2_y_hat, s=6, cmap=cm, core=True,
           core_cluster_centers=k_means_cluster_centers2)
    draw3D(X, 224, u'KMeans(Kmeans++)和KMeans(random)' + '预测不一致的点数:' + str(different_nodes), c="#000000", alpha=0.1, s=6,
           cmap=cm, core=False)
    plt.show()
###################################################################################
else:
# 抽维度之后的显示
    W1_ = 4
    W2_ = 5
    W3_ = 7

    if(W1_==W2_ or W2_==W3_ or W1_==W3_):
        raise Exception(print(u'维度存在相同的'))
    if(W1_ >= len(labels) or W2_ >= len(labels) or W3_ >= len(labels)):
        raise Exception(print(u'超出范围'+" 最大是: "+len(labels)))

    draw3D(NX, 221, u'原始数据分布图抽维度' + "维度1：" + labels[W1_] + "维度2：" + labels[W2_] + "维度3：" + labels[W3_], c=Y, s=6,
           cmap=cm, W1=W1_, W2=W2_, W3=W3_)
    draw3D(NX, 222, u'' + model1 + "维度1：" + labels[W1_] + "维度2：" + labels[W2_] + "维度3：" + labels[W3_], c=km1_y_hat, s=6,
           cmap=cm, W1=W1_, W2=W2_, W3=W3_)
    draw3D(NX, 223, u'' + model2 + "维度1：" + labels[W1_] + "维度2：" + labels[W2_] + "维度3：" + labels[W3_], c=km2_y_hat, s=6,
           cmap=cm, W1=W1_, W2=W2_, W3=W3_)
    draw3D(NX, 224, u'' + model1 + model2 + labels[W1_] + " " + labels[W2_] + " " + labels[W3_] + '预测不一致的点数:' + str(
        different_nodes), c="#000000", alpha=0.1, s=6, cmap=cm, core=False, W1=W1_, W2=W2_, W3=W3_)
    plt.show()
###################################################################################

#将聚类的结果写入原始表格中
#True代表两个模型预测的是相同的，False代表不相同
def to_excel(title):
    df['model1'] = km1_y_hat
    df['model2'] = km2_y_hat
    df['is_different'] = notdifferent
    df.to_excel(title)

to_excel('result.xlsx')