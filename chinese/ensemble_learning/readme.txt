********************************************** 
 
Version: Python 3.7.6 
IDE: Jupyter Notebook
@author: 何灿 Sany
Time: 2020/08/07

**********************************************

Package:
numpy、pandas、matplolib、sklearn、os、xgboost

Realization (demo: classification algorithm):
1. Implement common ensemble learning models: Voting Classifier, Bagging and Pasting, Random Forest, Adaboost, GradientBoosting (including xgboost), Stacking Ensemble
2. Feature importance and visualization: Random Forest, Adaboost, GradientBoosting (xgboost)
3. Two-dimensional visualized single classifier and ensemble learning model

Dataset:
【hydrogen_test_classification.xlsx】：The TRUE VALUE column in the data set is the actual category information

Further work that needs to be done:
Deploy the integrated learning algorithm on the existing framework and explore each integrated algorithm in depth

Note:
1. This is just a rough version of exploration and application of the ensemble learning algorithm. The classifier with the optimal parameters can be put into the ensemble learning model
2. Ensemble learning can be used in regression or classification models. Customized code blocks can be used. Here is only classification demo and regression demo will be implemented after then
3. Hyperparameter tuning can be refered to official documents. The hyperparameters of ensemble learning based on the tree model are mostly the same. Here we only explore the hyperparameters that are obviously different in various ensemble learning models.
4. 【learning_images】, 【hydrogen_test_classification.xlsx】, 【ensemble_learning.ipynb】need to be placed in the same working directory


使用库：
numpy、pandas、matplolib、sklearn、os、xgboost

实现功能（以分类为demo）：
1.实现常见的集成学习模型：Voting Classifier投票分类器、Bagging and Pasting 、Random Forest随机森林、Adaboost、GradientBoosting（含xgboost）、Stacking Ensemble
2.特征重要性及可视化：Random Forest、Adaboost、GradientBoosting（xgboost）
3.二维可视化单分类器与集成学习模型

数据集：
【hydrogen_test_classification.xlsx】：数据集中的TRUE VALUE一列为实际类别信息

需要做的进一步工作：
将集成学习算法部署在现有的框架上，深入探究每一个集成算法

注意：
1.这里只是对集成学习算法的应用做粗浅地探索及应用，可将调整到最优参数的分类器放入集成学习的模型中
2.集成学习都可以配合回归或分类模型使用，可DIY代码块，这里只做分类demo，之后再做回归demo
3.超参数调节，可参考官方文档找可调超参数，基于树模型的集成学习超参数大多相同，这里只对不同集成学习模型中有明显不同的超参数做探索
4.需将【learning_images】、【hydrogen_test_classification.xlsx】、【ensemble_learning.ipynb】置于同一工作目录下

*********************************************

