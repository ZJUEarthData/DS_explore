********************************************** 
 
Version: Python 3.7.6 
IDE: Pycharm
@author: 何灿 Sany
Time：2020/07/14

**********************************************

Package:
numpy、pandas、re(built-in)、time(built-in)


Realization:
1. Calculate the conversion factor, output y and projection value of specific element in the column name of the main quantity element
2. Place the data in the form of 【cal_data_4th.xlsx】 and a new data table (csv format) with the column containing the above values can be automatically generated


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


使用库：
numpy、pandas、re(内置)、time(内置)

实现功能：
1.计算列名中主量元素的换算系数、输出值y和特定元素投影值
2.只需按【cal_data_4th.xlsx】形式放置数据，即可自动生成含有上述值的列的新数据表格(csv格式)

数据集：
【辉石端元计算.xlsx】：是辉石组提供的数据
【cal_data_4th.xlsx】：只包含【辉石端元计算.xlsx】中主量元素的列
【result.csv】：自动化生成的表格

注意：
【cal_data_4th.xlsx】列名必须为氧化形式，例如【FeO、Cr2O3】

需要做的进一步工作：
完善【calculator.py】中ion_dict的阳离子相对原子质量

操作参数：
【calculator.py】中target列表的投射阳离子

*********************************************

