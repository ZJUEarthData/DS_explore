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
7. Early stopping

Note:
Place 【data.xlsx】, 【linear_polynomial_reg.ipynb】 in same working directory.

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


