********************************************** 
 
Version: Python 3.7.6 
IDE: Jupyter Notebook
@author: 何灿 Sany
Time: 2020/08/31

**********************************************

使用库：
numpy、pandas、matplolib、sklearn、os、tensorflow

实现功能（主要以regression为模板，classification可照搬）：
1.使用Sequential API建立线性结构的DNN
2.使用Funtional API建立二输入的Wide$Deep DNN、二输出的正则化Wide&Deep DNN
3.利用Callback机制保存训练过程中最优模型
4.利用早期停止法防止过拟合
5.使用Subclassing API建立动态的二输入、二输出的正则化Wide&Deep DNN

数据集：
【Fe_test_regression.xlsx】：数据集中的[Fe3+/Fetot]一列为标签值
【hydrogen_test_classification.xlsx】：数据集中[TRUE VALUE]一列为标签值

需要做的进一步工作：
根据具体项目需要，构建输入层、隐藏层、输出层，选择损失函数、优化器

注意：
1.需下载TensorFlow2，可通过以下途径：
(1)$ python3 -m pip install --upgrade tensorflow
(2)如果下载到独立的环境，则可用以下方法建立虚拟环境
$ cd $ML_PATH  		    # ML.ipynb 所在的工作目录（e.g., $HOME/my_ml）
$ source env/bin/activate   # 适用于Linux or MacOSX
$ .\env\Scripts\activate    # 适用于Windows
2.TensorFlow的DNN搭建模式
(1)先搭建网络框架，如输入层、隐藏层、输出层
(2)在设置模型使用的损失函数、优化器、评价标准

*********************************************
