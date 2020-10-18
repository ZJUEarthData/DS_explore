#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import re
import time

try:
    import openpyxl
except Exception:
    print("*************WARNING*************")
    print("Please download the specific library : openpyxl")
    print("Method for downloading :  pip install openpyxl ")
    print("--------------------------------- \n")

def find_num(formula):
    """
    find the number of cation and oxygen atom in the formula

    :param formula: the molecular formula
    :return: the number of cation and oxygen atom
    """
    length = len(formula)
    temp_ion_num = [re.findall('\d?O', formula[i], re.I) for i in range(length)]
    ion_num = []
    for i in range(length):
        ion_num.extend(temp_ion_num[i])
    for j in range(length):
        ion_num[j] = re.findall('\d*', ion_num[j])[0]
        if ion_num[j] == '':
            ion_num[j] = 1
        else:
            ion_num[j] = int(ion_num[j])

    temp_oxy_num = [re.findall('O\d?', formula[i], re.I) for i in range(length)]
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

def find_ion(formula):
    """
    find the cation of the formula

    :param formula: the molecular formula
    :return: ion
    """
    length = len(formula)
    temp = []
    for i in range(length):
        a = re.findall('[a-zA-Z]{1,2}[\d*]?', formula[i], re.I)
        temp.append(a[0])
    ion = []
    for i in range(length):
        ion.extend(re.findall('[a-zA-Z]{1,2}', temp[i], re.I))
    return ion

def rel_mole_weight(ion, ion_num, oxy_num):
    """
    calculate the relative molecular mass of the formula

    :param ion: cation
    :param ion_num: the number of the cation
    :param oxy_num: the number of the oxygen atom
    :return: the relative molecular mass
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

def normalization_factor_calculation(rmw, oxy_num, data_input):
    normalization_factor = []
    data_num = data_input.shape[0]
    for i in range(data_num):
        single_data = data_input.iloc[i, :]
        nf = float(12) / sum(np.array(oxy_num) * np.array(single_data) / np.array(rmw))
        normalization_factor.append(nf)
    return normalization_factor

def cation_formula_calculation(normalization_factor, rmw, ion_num, data, ion):
    data_num = data.shape[0]
    cation = []
    for j in range(data_num):
        single_data = data.iloc[j, :]
        cation_formula = normalization_factor[j] * np.array(single_data) * np.array(ion_num) / np.array(rmw)
        cation.append(cation_formula)
    cation_df = pd.DataFrame(cation)
    cation_df.columns = ion
    return cation_df

def total_cation_fomular_calculation(cation_formula):
    data_num = cation_formula.shape[0]
    total_cation_fomular = np.array([np.array(cation_formula.iloc[i, :]).sum() for i in range(data_num)]).reshape(-1, 1)
    return total_cation_fomular

def corrected_cation_calculation(df_exc_fe, df_inc_fe):
    corrected_df = df_exc_fe.iloc[:, :-1].copy()
    for i in range(df_exc_fe.shape[0]):
        corrected_df.iloc[i, :] = np.array(df_exc_fe.iloc[i, :-1]) * 8 / df_exc_fe["total_cation_formula"][i]
    fe3 = []
    fe2 = []
    for j in range(df_inc_fe.shape[0]):
        fe3_temp = 24 * (1 - 8 / df_inc_fe["total_cation_formula"][j])
        fe3.append(fe3_temp)
        fe2_temp = df_inc_fe["Fe"][j] * 8 / df_inc_fe["total_cation_formula"][j] - fe3_temp
        fe2.append(fe2_temp)
    corrected_df["Fe2+"] = np.array(fe2).reshape(-1, 1)
    corrected_df["Fe3+"] = np.array(fe3).reshape(-1, 1)
    return corrected_df

def corrected_oxides_calculation(corrected_cation, df_input):
    corrected_oxides = df_input.drop("FeO", axis=1)
    feo = []
    fe2o3 = []
    for i in range(df_input.shape[0]):
        temp_feo = df_input["FeO"][i] * corrected_cation["Fe2+"][i] / (corrected_cation["Fe2+"][i] + corrected_cation["Fe3+"][i])
        temp_fe2o3 = 1.113 * (df_input["FeO"][i] - temp_feo)
        feo.append(temp_feo)
        fe2o3.append(temp_fe2o3)
    corrected_oxides["FeO"] = np.array(feo).reshape(-1, 1)
    corrected_oxides["Fe2O3"] = np.array(fe2o3).reshape(-1, 1)
    return corrected_oxides

def mole_fraction_calculation(corrected_cation, target):
    target_df = corrected_cation[target]
    mole_fraction = []
    data_num = corrected_cation.shape[0]
    for i in range(data_num):
        single_target_data = target_df.iloc[i, :]
        temp_molecular_fraction = []
        for j in range(len(target)):
            sum = 0
            for k in range(len(target)):
                sum += np.array(single_target_data[target[k]])
            single_molecular_fraction = np.array(single_target_data[target[j]]) / sum
            temp_molecular_fraction.append(single_molecular_fraction)
        mole_fraction.append(temp_molecular_fraction)
    molecular_fraction_df = pd.DataFrame(mole_fraction)
    columns_name = ['X' + target[l] for l in range(len(target))]
    molecular_fraction_df.columns = columns_name
    return molecular_fraction_df

def end_members_calculation(molecular_fraction_VIII, molecular_fraction_VI, target):
    data_num = molecular_fraction_VIII.shape[0]
    end_members = []
    columns_name = []
    for i in range(len(target)):
        if target[i].lower() == 'almandine':
            end_members.append(np.array(molecular_fraction_VIII['XFe2+']) * 100)
            columns_name.append(target[i])
        elif target[i].lower() == 'spessartine':
            end_members.append(np.array(molecular_fraction_VIII['XMn']) * 100)
            columns_name.append(target[i])
        elif target[i].lower() == 'pyrope':
            end_members.append(np.array(molecular_fraction_VIII['XMg']) * 100)
            columns_name.append(target[i])
        elif target[i].lower() == 'grossular':
            end_members.append(np.array(molecular_fraction_VIII['XCa']) * np.array(molecular_fraction_VI['XAl']) * 100)
            columns_name.append(target[i])
        elif target[i].lower() == 'andradite':
            end_members.append(np.array(molecular_fraction_VIII['XCa']) * np.array((molecular_fraction_VI['XFe3+'])) * 100)
            columns_name.append(target[i])
        elif target[i].lower() == 'uvarovite':
            end_members.append(np.array(molecular_fraction_VIII['XCa']) * np.array(molecular_fraction_VI['XCr']) * 100)
            columns_name.append(target[i])
        else:
            print("Please check whether the name '{}' is appropriate?".format(target[i]))
    end_members_df = pd.DataFrame(np.array(end_members).reshape(data_num, len(target)))
    end_members_df.columns = columns_name
    return end_members_df

def result2sheet(df, df_name):
    try:
        df.to_excel("{}.xlsx".format(df_name))
        print("Successfully store the results of {} in '{}.xlsx' \n".format(df_name, df_name))
    except ModuleNotFoundError:
        df.to_csv("{}.csv".format(df_name))
        print("Successfully store the results of {} in '{}.csv' \n".format(df_name, df_name))

def main():
    start_time = time.time()
    print("Reading the sheet............\n")
    data = pd.read_excel('garnet_input.xlsx')         # Reading the dataset
    data.fillna(0, inplace=True)                      # interpolate in case that the null values exist

    data_columns = list(data.columns)                 # the name of the oxides

    ion_num, oxy_num = find_num(data_columns)         # the number of cation and oxygen atom
    ion = find_ion(data_columns)                      # the name of the cation

    rmw = rel_mole_weight(ion, ion_num, oxy_num)      # relative molecular mass

    # calculate the normalization factor
    normalization_factor = normalization_factor_calculation(rmw, oxy_num, data)

    # calculate the cation of the formula
    cation_formula = cation_formula_calculation(normalization_factor, rmw, ion_num, data, ion)

    # calculate total cation of the formula and append it to cation_formula(DataFrame)
    total_cation_formula = total_cation_fomular_calculation(cation_formula)
    cation_formula["total_cation_formula"] = total_cation_formula

    # format the cation of the formula, normalization and the total cation of the formula
    temp_df = data.copy()
    temp_df['Normalization factor'] = np.array(normalization_factor).reshape(-1, 1)
    temp_df = pd.concat([temp_df, cation_formula], axis=1)
    result2sheet(temp_df, "cation")

    # calculate the corrected cation of the formula and format it
    cation_df_exc_fe = cation_formula.drop("Fe", axis=1)
    cation_df_inc_fe = pd.concat([cation_formula["Fe"], cation_formula["total_cation_formula"]], axis=1)
    corrected_cation = corrected_cation_calculation(cation_df_exc_fe, cation_df_inc_fe)
    result2sheet(corrected_cation, "corrected_cation")

    # calculate the corrected oxides and format it
    corrected_oxides = corrected_oxides_calculation(corrected_cation, data)
    result2sheet(corrected_oxides, "corrected_oxides")

    # calculate the molecular fraction
    XVIII = ['Fe2+', 'Mn', 'Mg', 'Ca']
    XVI = ['Al', 'Fe3+', 'Cr']
    mole_fraction_VIII = mole_fraction_calculation(corrected_cation, XVIII)
    mole_fraction_VI = mole_fraction_calculation(corrected_cation, XVI)
    mole_fraction = pd.concat([mole_fraction_VIII, mole_fraction_VI], axis=1)
    result2sheet(mole_fraction, "molecular_fraction")

    # calculate the end members of garnet and format it
    end_members_name = ['Almandine', 'Spessartine', 'Pyrope', 'Grossular', 'Andradite', 'Uvarovite']
    end_members = end_members_calculation(mole_fraction_VIII, mole_fraction_VI, end_members_name)
    result2sheet(end_members, "end_members")

    end_time = time.time()
    print("Time for running:{}s".format(end_time-start_time))
    
if __name__ == '__main__':
    main()



