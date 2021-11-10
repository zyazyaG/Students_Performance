#!/usr/bin/env python
# coding: utf-8

# # Data Exploring Functions

# This file contains functions that will help to explore the datasets and find out the missing values persentage

# In[1]:


import pandas as pd
import numpy as np


# The "show_info" function displays the dataset column names with missing values percentage and type of the data.

# In[3]:


def show_info(df):
    persent = df.isnull().sum() * 100 / len(df)
    
    
    missing_values = pd.DataFrame({'missing_values_%': persent})
    missing_values['Data_type'] = df.dtypes
        
    print("Lenght of Dataset: " + str(len(df)))
    print(missing_values)
    
    return 



def values (df, col_list):
    
    df_values = df[col_list]
    
    for col in df_values:
        print(df_values[col].value_counts()) 
        print("\n")
    
    return
  
def missing_values (df, r1, r2):
    
    persent = df.isnull().sum() * 100 / len(df)
    
    
    m_values = pd.DataFrame({'missing_values_%': persent})
    
    index = m_values.index
    condition = (m_values["missing_values_%"] > r1) & (m_values["missing_values_%"] < r2)
    
    indices = index[condition]
    cols = indices.tolist()
    
    return cols


def conversion (df, column, d_type):
    
    for col in column:
        df[col] = df[col].astype(d_type)
        
    return



def chi_test(cross_tabs):
    
    chi, p, dof, con_table = stats.chi2_contingency(cross_tabs)
    print(f'Chi-Squared = {chi}')
    print(f'p-value= {p}')
    print(f'Degrees of Freedom = {dof}')



def percentage(cross_tab):
    
    df = pd.DataFrame(columns = ['Pass', 'Fail', 'Withdraw', 'Distinct', 'Success', 'Failure'])
    
    for i, row in cross_tab.iterrows():
        
        percent = row[0] + row[1] + row[2] + row[3]
        
        df.loc[i,'Distinct'] = round((row[0] * 100 / percent),2)
        df.loc[i,'Fail'] = round((row[1] * 100 / percent),2)
        df.loc[i,'Pass']= round((row[2] * 100 / percent),2)
        df.loc[i,'Withdraw'] = round((row[3] * 100 / percent),2)
        df.loc[i,'Success'] = df.loc[i,'Distinct'] + df.loc[i,'Pass']
        df.loc[i,'Failure'] =  df.loc[i,'Fail'] + df.loc[i,'Withdraw']
        
    return df
    
                           
                