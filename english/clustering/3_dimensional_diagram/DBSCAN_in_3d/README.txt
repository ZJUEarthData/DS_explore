**********************************************
Version: Python 3.7.6
IDE: Pycharm
@Author: Wang Shengxin
Time: 2020/09/02
**********************************************
Use library:
matplotlib、sklearn、mpl_ toolkits、pandas、numpy
Implementation function:
For the three-dimensional comparison of DBSCAN model differences, the difference data is loaded into excel, and any three dimensions are projected into the three-dimensional space
Question: how do the two DBSCAN models compare the differences
Solution: because of different models, DBSCAN may be divided into different categories. Therefore, after simplification, DBSCAN is directly classified according to the characteristics
Although it may not be as good as kmeans to bind the center, there is no better way to do so
Disadvantages: the same category is different label, is considered to be divided into different
Data set:
[test4. Xlsx]: the true value column in the dataset is the actual category information
Parameter adjustment:
Model1: model. For specific parameter adjustment, refer to the parameter adjustment of DBSCAN
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
Core = = false draw difference points
W1_ : 0 by default. It can be modified when dimension is extracted
W2_ : 1 by default. It can be modified when dimension is selected
W3_ : default 2, which can be modified when dimension is selected
Further work needs to be done:
Other clustering methods are supplemented and fused
Tip:
After running in. Py, you can use 3D graphics in detail, but you will lose the three-dimensional property when you use it in jupyter notebook
Cm is the color of cluster points, which is lighter. There are only 7 colors by default, which can be added according to your own needs
Newphoto: to decide whether to display the 3D drawing after dimension reduction or to extract the dimension unit graph, I can't unify the two implementations at present, otherwise, it will cause problems in the second picture
#In Excel, true means that the predictions of the two models are the same, and false means that they are not the same
*********************************************