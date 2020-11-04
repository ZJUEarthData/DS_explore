**********************************************
Version: Python 3.7.6
IDE: Jupyter Notebook
@Author: he can Sany
Time: 2020/07/17
**********************************************
Use library:
numpy、pandas、matplolib、sklearn
Implementation function:
1. K-means and AP are used for clustering. The former uses 8 scoring criteria and the latter has 7
2. Draw the outline chart
3. Compare the running time of kmeans and minibatch kmeans
4. Use gridsearchcv to search the optimal parameters of the two algorithms and save the optimal model
5. K-means visualization after dimension reduction by PCA
6. Discuss two initialization methods of k-means (K-means + + and random) and visualization with three grades
7. Implement stratified sampling based on classification results
Data set:
【Test_ 2. Xlsx]: the true value column in the dataset is the actual category information
【test2_ result.csv 】: a new data set with clustering algorithm results
Scoring criteria (for specific use, please refer to relevant information)
Clustering evaluation mainly includes: estimating the clustering trend, determining the number of clusters in the data set, and measuring the clustering quality.
1. The evaluation index of k-means
Mean inertia score: sum of distances from a point in a cluster to a cluster
2. External evaluation index: need actual category information (5 kinds)
Homogeneity score: homogeneity, the value range is [0,1], and each aggregated class contains only one category degree measure.
Completeness score: integrity, the value range is [0,1], and the degree to which each category is pointed to the same aggregated class.
V Measure score: harmonic mean of homogeneity and integrity, with the value range of [0,1]
Adjusted Rand score: adjust the RAND coefficient, and the value range is [- 1,1]. The larger the value, the more consistent the clustering results are with the real situation
Adjusted mutual information score: adjust mutual information, and the value range is [- 1,1]. The larger the value, the more consistent the clustering results are with the real situation
3. Internal indicators: there is no need for actual category information (2, mainly these two are used as scoring criteria)
Calinski harabasz score: the higher the value, the better the clustering effect
Silhouette score: contour coefficient, the value range is [- 1,1], the closer the same class samples are and the farther the distance between different types of samples, the higher the score is.
Super parameter adjustment:
One sklean.clustering.KMeans
N_ Clusters: adjustable. The number of cluster centers is 8 by default
Init: adjustable, two, initialization method
N_ Init: adjustable, iteration times, the default is 10
Two sklean.clustering.affinity_ propagation
Preference: adjustable, negative value
Damping: adjustable, attenuation coefficient, the range is [0,1], the default is 0.5
Three sklearn.model_ selection.GridSearchCV
CV: adjustable, cross validation times, the default is 5
Scoring: adjustable, selected according to the model category sklearn.metrics Evaluation criteria in it
Four sklearn.decomposition.PCA
N_ Components: adjustable dimension
Further work needs to be done:
According to the actual needs, select the clustering score standard, for example, for kmeans, mainly focus on the contour coefficient and inertia
Tip:
【Test_ 2.xlsx】、【kmeans_ Ap_ clustering.ipynb 】It needs to be in the same directory
*********************************************