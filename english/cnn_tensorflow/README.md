```
********************************************** 
 
Version: Python 3.7.6 
IDE: Jupyter Notebook
@author: Jincen Song
Time: 2020/10/06

**********************************************
```

  
    
      
  
  



**Package：**
numpy、pandas、matplolib、sklearn、os、tensorflow2.0+



**Dataset：**

```
【hydrogen_test_classification.xlsx】：The [true value] column in the dataset is the label value
```

**Function：**
The CNN is used to classify the data5.5 in two category 



**Process**：

1.Use Sequential AP to build CNN and DNN

2.Innovatively, the data of 25 dimensions were input into CNN as 5 * 5 pictures, and the training accuracy was recorded as A1

3.The accuracy of training with large-scale fully connected networks is recorded as A2

4.No matter how many epochs are experienced, A1 is always greater than A2

5.Use checkpoint to save the model. The suffix of the model is CKPT, which is different from H5 file

6.Batch normalization is used at the bottom of neural network

7.The convolution kernel size of convolution neural network is 2. If the convolution kernel of size 3 is used, the feature extraction in the early stage is too abstract and the result is not good



**Result**：



![result](https://github.com/Geeksongs/new-algorithm/blob/master/cnn_tensorflow/result.png)



**Next steps：**
According to the needs of the project, the input layer size shape of convolution neural network is transformed. If the input is 30 dimension data, it can be reconstructed into a square with the same length and width by linear interpolation method or up sampling method, and input into the convolution neural network


**New algorithms can be explored：**

1.Regression by LSTM/GRU

2.The convolution neural network and sequence model are combined to process the data

3.Contact me by QQ：1342952373
