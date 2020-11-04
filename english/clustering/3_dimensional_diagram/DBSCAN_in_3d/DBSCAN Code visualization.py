import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.cluster import DBSCAN
from sklearn.metrics.pairwise import pairwise_distances_argmin
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## Set property to prevent garbled code
mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False

#Read dataset
df = pd.read_excel('E:/A/工作/聚类/聚类算法包ver3.0/聚类算法包/DBSCAN/test4.xlsx')
# Separate the real classification label from the feature
X = df.drop(['TRUE VALUE'], axis=1)
Y = df['TRUE VALUE']
labels = list(X.columns.values)
NX = np.array(X)

#PCA
pca3 = PCA(n_components = 3)
X = pca3.fit_transform(X)


###################################################################################
#model1
model1 = "DBSCAN(eps=0.6,min_samples=7)"
db1 = DBSCAN(eps=0.6,min_samples=7) #0.5 5
db1.fit(X)  #train model1
#model2
###################################################################################
model2 = "DBSCAN(eps=0.8,min_samples=7)"
db2 = DBSCAN(eps=0.8,min_samples=7)
db2.fit(X)
###################################################################################

#Results
db1_labels = db1.fit_predict(X)
db2_labels = db2.fit_predict(X)

fig = plt.figure(figsize=(14, 8), facecolor='w')
plt.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=0.9)

n_clusters_1= len(set(db1_labels)) - (1 if -1 in db1_labels else 0) #
print(n_clusters_1)
n_clusters_2 = len(set(db2_labels)) - (1 if -1 in db2_labels else 0) #
print(n_clusters_2)

unique_labels1 = set(db1_labels)
print(unique_labels1)
unique_labels2 = set(db2_labels)
print(unique_labels2)


cm = mpl.colors.ListedColormap(['#FFC2CC', '#C2FFCC', '#CCC2FF','#B0E0E6','#7FFFAA','#FFD700','#F0D700'])

#plt.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=0.9)
def draw3D(X1,layout,title,c,s,W1=0,W2=1,W3=2,alpha=None,cmap=None,core=None,core_cluster_centers=None):
    ax = fig.add_subplot(layout, projection='3d')
    ax.scatter(X1[:, W1], X1[:, W2], X1[:, W3], alpha=alpha, c=c,s=s,cmap=cmap)  # 生成散点.利用c控制颜色序列,s控制大小
    if core == False:
        ax.scatter(X1[different, W1], X1[different, W2], X1[different, W3], c="#FF0000", s=15,edgecolors='none',marker="*")
    plt.title(title)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.grid(True)

#Get the number of samples with inconsistent predictions of the two algorithms
different = list(map(lambda x: x==-2,db1_labels))
print(different)
for k in range(len(db1_labels)):
    different += ((db1_labels == k) != (db2_labels == k))
identic = np.logical_not(different)
different_nodes = len(list(filter(lambda x:x, different)))
notdifferent = (1-different).astype(np.bool)

###################################################################################
newphoto = True


#Plot after dimension reduction

if newphoto == False:
    draw3D(X, 221, u'原始数据分布图', c=Y, s=6)
    draw3D(X, 222, model1+u'算法聚类结果图' , c=db1_labels, s=6,cmap=cm)
    draw3D(X, 223, model2+u'算法聚类结果图', c=db2_labels, s=6,cmap=cm)
    draw3D(X, 224, model1+model2+ '预测不一致的点数:'+str(different_nodes), c="#000000", alpha=0.1, s=6,core=False)
    plt.show()
###################################################################################
else:
# Display after Dimension Extraction
    W1_ = 1
    W2_ = 2
    W3_ = 7

    if(W1_==W2_ or W2_==W3_ or W1_==W3_):
        raise Exception(print(u'exist same dimension'))
    if(W1_ >= len(labels) or W2_ >= len(labels) or W3_ >= len(labels)):
        raise Exception(print(u'out of range'+" Maximum: "+len(labels)))

    draw3D(NX, 221, u'Dimension Extraction from original data distribution' + "Dimension1：" + labels[W1_] + "Dimension2：" + labels[W2_] + "Dimension3：" + labels[W3_], c=Y, s=6,
            W1=W1_, W2=W2_, W3=W3_)
    draw3D(NX, 222, u'' + model1 + "Dimension1：" + labels[W1_] + "Dimension2：" + labels[W2_] + "Dimension3：" + labels[W3_], c=db1_labels, s=6,
            W1=W1_, W2=W2_, W3=W3_)
    draw3D(NX, 223, u'' + model2 + "Dimension1：" + labels[W1_] + "Dimension2：" + labels[W2_] + "Dimension3：" + labels[W3_], c=db2_labels, s=6,
            W1=W1_, W2=W2_, W3=W3_)
    draw3D(NX, 224, u'' + model1 + model2 + labels[W1_] + " " + labels[W2_] + " " + labels[W3_] + 'The number of inconsistent prediction points:' + str(
        different_nodes), c="#000000", alpha=0.1, s=6,  core=False, W1=W1_, W2=W2_, W3=W3_)
    plt.show()
###################################################################################

#Write the results of clustering into the original table
#True means that the predictions of the two models are the same, and false means that they are not the same
def to_excel(title):
    df['model1'] = db1_labels
    df['model2'] = db2_labels
    df['is_different'] = notdifferent
    df.to_excel(title)

to_excel('result.xlsx')
