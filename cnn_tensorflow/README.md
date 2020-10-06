```
********************************************** 
 
Version: Python 3.7.6 
IDE: Jupyter Notebook
@author: Jincen Song
Time: 2020/10/06

**********************************************
```



**使用库：**
numpy、pandas、matplolib、sklearn、os、tensorflow2.0+



**数据集：**

```
【hydrogen_test_classification.xlsx】：数据集中[TRUE VALUE]一列为标签值
```



**实验过程**：

1.实现Sequential AP分别I建立卷积神经网络CNN和DNN

2.创新性地将25个维度的数据当作5*5的图片输入进入CNN,训练准确度记为A1

3.使用大规模全连接网络训练的准确度记为A2

4.实验发现不管经历多少个Epoch，A1总是大于A2

5.使用checkpoint保存模型，模型的后缀为ckpt，和h5文件有所不同

6.在神经网络的底层使用了BatchNormalization

7.卷积神经网络的卷积核大小为2，如果使用大小为3的卷积核，则会让前期抽取特征过于抽象，结果不太好



**训练结果**：



![result](F:\UNIVERSITY STUDY\new-algorithm-master\cnn_tensorflow\result.png)



**需要进一步做的工作：**
根据项目的需要，将卷积神经网络的输入层大小shape进行变换，如果输入为30维度数据，可以通过线性插值法或上采样的方法resize为一个长宽相同的正方形方块，输入进卷积神经网络。



**可以进行探索新的算法：**

1.利用深度学习当中的LSTM/GRU做回归问题

2.将卷积神经网络和序列模型相结合进行数据处理

3.欢迎有兴趣的同学和我一起讨论新的算法，联系方式QQ：1342952373