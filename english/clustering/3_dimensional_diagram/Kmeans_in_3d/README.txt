**********************************************
Version: Python 3.7.6
IDE: Pycharm
@Author: Wang Shengxin
Time: 2020/08/28
**********************************************
Use library:
matplotlib、sklearn、mpl_ toolkits、pandas、numpy
Implementation function:
For the three-dimensional comparison of kmeans model differences, the difference data is loaded into excel, and any three dimensions are projected into the three-dimensional space
Data set:
[test4. Xlsx]: the true value column in the dataset is the actual category information
Parameter adjustment:
Clusters: our K value and N of kmeans class_ The meaning of clusters is the same.
Model1: model. For specific parameter adjustment, refer to kmeans' parameter adjustment
Model2: same as above
newphoto：
3D display after true dimension reduction
False dimension display (W1 can be used_ ,W2_ ,W3_）
Parameter adjustment of draw3D function:
X1: data set (without actual classification label)
Layout: layout, 223, representing 2 * 2, subgraph 3
Title: theme, picture name
c: Color or color sequence
s: The size of the point
Alpha: alpha channel (default none)
CMAP: colormap (default none)
core：
Draw the original image by default (none)
Core = = true draws the cluster center point
Core = = false draw difference points
core_ cluster_ Centers: the default (none), cluster center point
W1_ : 0 by default. It can be modified when dimension is extracted
W2_ : 1 by default. It can be modified when dimension is selected
W3_ : default 2, which can be modified when dimension is selected
Further work needs to be done:
Other clustering methods are supplemented and fused
Tip:
After running in. Py, you can use 3D graphics in detail, but you will lose the three-dimensional property when you use it in jupyter notebook
Cm is the color of cluster points, which is light color. There are only 6 colors by default, which can be added according to your own needs
Cm2 is the color of the cluster center, which is heavy. There are only 6 colors by default, which can be added according to your own needs
Newphoto: to decide whether to display the 3D drawing after dimension reduction or to extract the dimension unit graph, I can't unify the two implementations at present, otherwise, it will cause problems in the second picture
#In Excel, true means that the predictions of the two models are the same, and false means that they are not the same
*********************************************