********************************************** 
 
Version: Python 3.7.6 
IDE: Jupyter Notebook
@author: 何灿 Sany
Time: 2020/07/23
Email: sanyhew1097618435@163.com
Related Video: https://www.youtube.com/watch?v=J9Do8FD_uyA

**********************************************

Library used: 
numpy、pandas、matplolib、sklearn

Function realized: 
 - 1.Ordinary PCA (linear projection): Principal component axis expression of feature space, Squared distance of reconstructed data and original data, Two-dimensional visualization, componential biplot, componential plot in 3d

 - 2.Kernel PCA (non-linear projection): four kernel methods (linear, rbf, poly, sigmoid), Squared distance, Two-dimensional visualization.

 - 3.For large data sets, you can use Incremental PCA and Randomized PCA, and compare the running time of Ordinary PCA, Incremental PCA and Randomized PCA.

 - 4.Find the optimal parameters of Kernel PCA through GridSearchCV, with the score of Classification model or Regression model.

 - 5.Manifold learning (non-linear projection): four common types, Two-dimensional visualization.


Data set: 
"dataset.xlsx": the [TRUE VALUE] column in the data set is Actual category information

Scoring criteria (for specific use, please refer to relevant information): 
 - 1.By the squared distance between the reconstructed data and the original data
 - 2.Determine the quality of the model by scoring the dimensionality reduction + classification (or regression) model.


Hyperparameter adjustment (the official documentation can be refered to find adjustable hyperparameters. The hyperparameters listed below are involved in [dimensionality_reduction.ipynb]): 
 - 1.sklean.decomposition.PCA
   n_components: adjustable, dimensions to be downgraded to 
 - 2.sklean.decomposition.KernelPCA
   n_components: adjustable, dimensions to be downgraded to 
   kernel: adjustable, six kernal methods (linear, poly, rbf, sigmoid, cosine, precomputed)
   Gamma: adjustable, used in four kernal methods (poly, rbf, sigmoid), value range is 0~1, default is 1/feature number
   coef: adjustable, used in two kernal methods (poly, sigmoid), value range is 0~1, default is 1
   Degree: adjustable, used in poly kernal method, value range is 0~1, default is 3
 - 3.sklearn.model_selection.GridSearchCV
   cv: adjustable, number of cross-validation, default is 5
   scoring: adjustable, select the evaluation criteria in "sklearn.metrics" according to the model category
   params: modifiable params dictionary
 - 4.sklearn.manifold.LocallyLinearEmbedding
   n_components: adjustable, dimensions to be downgraded to 
   n_neighbors: adjustable
 - 5.sklearn.manifold.Isomap, TSNE, MDS
   n_components: adjustable, dimensions to be downgraded to 


Further work needed: 
If the data is large, random PCA and incremental PCA algorithms can be used to reduce running time and storage memory.


Notice:
Dimensionality reduction and same clustering can both be used with regression or classification models, DIY code blocks can be used, and standardized processing is required before it is used.

*********************************************

