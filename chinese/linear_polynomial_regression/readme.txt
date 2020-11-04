********************************************** 
 
Version: Python 3.7.6 
IDE: Jupyter Notebook
@author: 何灿 Sany
Time: 2020/07/08

**********************************************

Realization:
1. Visualization of data exploration
2. Linear regression model  (analytical inference)
3. Polynomial regression model (analytical inference)
4. Regularized polynomial regression model  (analytical inference)
  Regularization is achieved with elastic network (a combination of Ridge regression and Lasso regression) 
5. Evaluation of the three models
6. The learning curve of the three models

Note:
Place 【3rd_dataset.csv】, 【fe_ml_3rd.ipynb】 in same working directory.

Further work that needs to be done:
Feature engineering (feature selection, feature scaling, feature expansion)

Problem:
Model regularization, high performance computing (computing time reduction, eg. SGD)

Hyperparameter:
 - 1.Linear regression model:
No need to tune hyperparameters in LinearRegression()

 - 2.Polynomial regression model:
The degree in PolynomialFeatures(degree=2) represents the highest number of times, adjustable

 - 3.Regularized polynomial regression model:
The range of alpha in ElasticNet (alpha=0.3, l1_ratio=0.3) is 0~1, and the range of l1_ratiao is 0~1, which represents the degree of regularization


实现功能：
1.数据探索可视化
2.线性回归模型计算器（公式可列出）
3.多项式回归模型计算器（公式可列出）
4.经过正则化的多项式回归模型计算器（公式可列出）
  采用的是弹性网络（Ridge回归和Lasso回归的简单混合）正则化
5.三个模型的评估
6.三个模型的学习曲线 

注意：
将3rd_dataset.csv, fe_ml_3rd.ipynb放置在同一目录下。

需要做的进一步工作：
特征工程（特征选取、特征缩放、特征拓展）

考虑问题：
模型正则化，降低运算时间（如SGD）

超参数:
1.线性回归模型：
LinearRegression() 中不用调超参数
2.多项式回归模型：
PolynomialFeatures(degree=2)中的degree代表最高的次数，可调
3.正则化的多项式回归模型：
ElasticNet(alpha=0.3, l1_ratio=0.3)中的alpha可调范围为0~1，l1_ratiao可调范围为0~1，代表正则化的强弱程度
