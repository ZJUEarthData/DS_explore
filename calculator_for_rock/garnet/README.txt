**********************************************
  
Version: Python 3.7.6
IDE: Pycharm
@author: 何灿 Sany
Time：2020/10/19

**********************************************

Package:
numpy、pandas、re(built-in)、time(built-in)

Realization:
1. Calculate the conversion factor, output y and projection value of specific element in the column name of the main quantity element
2. Place the data in the form of 【garnet_input.xlsx】 and a series of data table (excel or csv format) with the column containing the above values can be automatically generated


Data set:
【Pyroxene end element calculation.xlsx】: Data is provided by the pyroxene group
【Cal_data_4th.xlsx】: only include the column of main quantity elements in 【pyroxene end element calculation.xlsx】
【Result.csv】: Automatically generated form


Note:
【Cal_data_4th.xlsx】The column name must be in oxidized form, such as 【FeO, Cr2O3】


Further work that needs to be done:
Improve the relative atomic mass of cations in ion_dict in 【calculator.py】


Operating parameters:
【Calculator.py】 the projection cation of the target list
