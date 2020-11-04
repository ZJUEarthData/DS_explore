********************************************** 
 
Version: Python 3.7.6 
IDE: Jupyter Notebook
@author: 何灿 Sany
Time: 2020/08/31

**********************************************

Library used: 
numpy、pandas、matplolib、sklearn、os、tensorflow

Function realized (mainly use regression as a template, classification can be copied):
 - 1.Use Sequential API to build a simple fully connected DNN
 - 2.Use Funtional API to create a two-input Wide$Deep DNN and a two-output regularized Wide&Deep DNN
 - 3.Use the Callback mechanism to save the optimal model during training
 - 4.Use early stopping method to prevent overfitting
 - 5.Use Subclassing API to build dynamic two-input and two-output regularized Wide&Deep DNN
 - 6.Use RandomizedSearchCV to find the optimal hyperparameter 

Data set:
"Fe_test_regression.xlsx": the [Fe3+/Fetot] column in the data set is Label value
"hydrogen_test_classification.xlsx": the [TRUE VALUE] column in the data set is Label value

Further work needed:
According to specific project needs, construct input layer, hidden layer, output layer, choose loss function, optimizer.

Notice: 
 - 1.Need to download TensorFlow2, through the following ways: 
(1)$ python3 -m pip install --upgrade tensorflow
(2)If you download to a separate environment, you can use the following methods to create a virtual environment. 
$ cd ML_PATH # working directory where ML.ipynb is located (e.g., $HOME/my_ml)
$ source env/bin/activate   # Suitable for Linux or MacOSX
$ .\env\Scripts\activate    # Suitable for Windows
 - 2.TensorFlow's DNN construction mode:
(1)Firstly build the network framework, such as input layer, hidden layer, output layer.
(2)Then set the loss function, optimizer, and evaluation criteria used in the model.

*********************************************
