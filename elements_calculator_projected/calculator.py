#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import re
import time

def find_num(major_el_name):
    """
    找到列名中主量元素的阳离子个数和氧原子个数

    :param major_el_name: 主量元素的列名
    :return: 阳离子个数和氧原子个数
    """
    length = len(major_el_name)
    temp_ion_num = [re.findall('\d?O', major_el_name[i], re.I) for i in range(length)]
    ion_num = []
    for i in range(length):
        ion_num.extend(temp_ion_num[i])
    for j in range(length):
        ion_num[j] = re.findall('\d*', ion_num[j])[0]
        if ion_num[j] == '':
            ion_num[j] = 1
        else:
            ion_num[j] = int(ion_num[j])

    temp_oxy_num = [re.findall('O\d?', major_el_name[i], re.I) for i in range(length)]
    oxy_num = []
    for i in range(length):
        oxy_num.extend(temp_oxy_num[i])
    for j in range(length):
        oxy_num[j] = re.findall('\d*', oxy_num[j])[1]
        if oxy_num[j] == '':
            oxy_num[j] = 1
        else:
            oxy_num[j] = int(oxy_num[j])
    return ion_num, oxy_num

def find_ion(major_el_name):
    """
    找到列名中主量元素中的阳离子

    :param major_el_name: 主量元素的列名
    :return:  阳离子
    """
    length = len(major_el_name)
    temp = []
    for i in range(length):
        a = re.findall('[a-zA-Z]{1,2}[\d*]?', major_el_name[i], re.I)
        temp.append(a[0])
    ion = []
    for i in range(length):
        ion.extend(re.findall('[a-zA-Z]{1,2}', temp[i], re.I))
    return ion

def rel_mole_weight(ion, ion_num, oxy_num):
    """
    计算相对分子量

    :param ion: 各阳离子
    :param ion_num: 各阳离子个数
    :param oxy_num: 各阳离子对应的氧原子数
    :return: 相对分子质量
    """
    ion_dict = {'Si':28.085, 'Ti':47.867, 'Al':26.981, 'Cr':51.996, 'Fe':55.845, 'Mn':54.938,
                'Mg':24.305, 'Ca':40.078, 'Na':22.989, 'K':39.098, 'P':30.974, 'Ni':58.693,
                'Zn':65.390, 'Li':6.941, 'Zr':91.224, 'V':50.941, 'O':15.999}
    length = len(ion)
    if length != len(ion_num) or length != len(oxy_num):
        raise Exception

    relative_molecular_weight = []
    for i in range(length):
        a = ion_dict[ion[i]] * ion_num[i] + ion_dict['O'] * oxy_num[i]
        relative_molecular_weight.append(a)
    return relative_molecular_weight

def conver_ratio(rmw, oxy_num, mf):
    """
    计算换算系数

    :param rmw: 相对分子质量
    :param mf: 主量元素的质量分数
    :return: 换算系数的值
    """
    conversion_ratio = float(6) / sum(np.array(oxy_num) * np.array(mf) / np.array(rmw))
    return conversion_ratio

def output(cr, rmw, ion_num, mf):
    '''
    计算各阳离子的输出y

    :param cr: 换算系数
    :param rmw: 相对分子质量
    :param ion_num: 阳离子数量
    :param mf: 主量元素的质量分数
    :return: 各阳离子的输出y
    '''
    y = cr * np.array(mf) * np.array(ion_num) / np.array(rmw)
    return y

def projection(index, target, y):
    '''
    计算特定阳离子的投射值，范围为0~1

    :param index: 指定的阳离子列表的索引
    :param target: 指定的阳离子列表
    :param y: 各阳离子的输出值y
    :return: 特定阳离子的投射值
    '''
    sum = 0
    for i in range(len(target)):
        sum += np.array(y[target[i]])
    # sum = np.array(y[target[0]]) + np.array(y[target[1]]) + np.array(y[target[2]])
    proj = np.array(y[target[index]]) / sum
    return proj


def main():
    start_time = time.time()
    print("读取文件............")
    data = pd.read_excel('cal_data_4th.xlsx')         # 读取数据集
    data.fillna(0, inplace=True)                      # 插值为零，不能有空值

    data_columns = list(data.columns)
    # print("列名：", data_columns)                    # 列名：主量元素

    ion_num, oxy_num = find_num(data_columns)
    ion = find_ion(data_columns)
    # print("阳离子: ", ion)                           # 展现阳离子
    # print("阳离子个数: ", ion_num)                    # 阳离子个数
    # print("氧原子个数: ",oxy_num)                     # 氧原子个数
    # print("维度:", len(ion), len(ion_num), len(oxy_num)) # 比较纬度是否相同

    rmw = rel_mole_weight(ion, ion_num, oxy_num)
    # print("相对分子质量:", np.array(rmw))             # 相对分子质量
    cr_columns = []
    data_num = data.shape[0]
    for i in range(data_num):
        a = data.iloc[i, :]
        cr = conver_ratio(rmw, oxy_num, a)            # 计算换算系数
        cr_columns.append(cr)                         # 保存换算系数

    temp = []
    for j in range(data_num):
        b = data.iloc[j, :]
        y = output(cr_columns[j], rmw, ion_num, b)    # 计算各阳离子的输出值y
        temp.append(y)                                # 保存输出值y
    temp_df = pd.DataFrame(temp)                      # 新建保存输出值y的DataFrame表格
    temp_df.columns = ion                             # 给输出值y的DataFrame表格添加列名
    # print(temp_df)
    data['换算系数'] = np.array(cr_columns).reshape(-1, 1)  # 在原数据集【data】新增【换算系数】一列
    # print(data['换算系数'])
    # print(data)                                     # 含有换算系数的原数据集
    new_df = pd.concat([data, temp_df], axis=1)       # 将原数据集的DataFrame表格同输出值y的DataFrame表格合并
    # print(new_df)                                   # 含有换算系数和各阳离子输出值y列的数据集

    target = ['Fe', 'Mg', 'Ca']                       # 选定需要投射的阳离子
    df1 = new_df[target]
    target_list = []
    for i in range(data_num):
        y = df1.iloc[i, :]
        ls = []
        for j in range(len(target)):
            proj = projection(j, target, y)           # 计算指定阳离子的投射值
            ls.append(proj)                           # 保存投射值
        #print(ls)
        target_list.append(ls)
    target_df = pd.DataFrame(target_list)             # 新建保存投射值的DataFrame表格
    # print(pd.DataFrame(target_list))
    project_name = [target[i] + '_projected' for i in range(len(target))]   # 构造含有投射值的新列名
    target_df.columns = project_name                                        # 给保存投射值的DataFrame表格添加列名
    final_df = pd.concat([new_df, target_df], axis=1)  # 合并含有换算系数和输出值有的原数据表格和保存投射值的DF表格
    # print(final_df)                                  # 我们最终要的表格

    final_df.to_csv("new_cal_data_4th.csv")            # 以csv文件格式保存最后的表格

    end_time = time.time()
    print("程序运行时间:{}s".format(end_time-start_time))
    
    
if __name__ == '__main__':
    main()



