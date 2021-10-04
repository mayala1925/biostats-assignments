#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 12:32:01 2021

@author: matthewayala
"""

# Importing libraries and data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

cal_20_data = pd.read_csv('calcium20.csv')
cal_100_data = pd.read_csv('calcium100.csv')
cal_500_data = pd.read_csv('calcium500.csv')

print(cal_20_data.head())
print(cal_100_data.head())
print(cal_500_data.head())

#%%
# 1 - Creating histograms of serum calcium

sns.histplot(data= cal_20_data, x = 'calcium').set(title = 'Serum Calcium (n = 20)')


#%%
sns.histplot(data= cal_100_data, x = 'calcium').set(title = 'Serum Calcium (n = 100)')

#%%
sns.histplot(data= cal_500_data, x = 'calcium').set(title = 'Serum Calcium (n = 500)')


#%%
# 2- Calculating mean, std, and sem

def calc_stats(data,sample_size):
    mean = np.mean(data['calcium'])
    
    std = np.std(data['calcium'])
    
    SE = std / np.sqrt(sample_size)
    
    return mean, std, SE

# n=20
print(calc_stats(cal_20_data, 20))

# n=100
print(calc_stats(cal_100_data, 100))

# n=500
print(calc_stats(cal_500_data, 500))

#%%
# 3 - Calculating 95% CI

import scipy.stats as st

# n=20
print(st.norm.interval(alpha=0.95, loc=np.mean(cal_20_data['calcium']),
                 scale=st.sem(cal_20_data['calcium'])))

# n=100
print(st.norm.interval(alpha=0.95, loc=np.mean(cal_100_data['calcium']),
                 scale=st.sem(cal_100_data['calcium'])))

# n=500
print(st.norm.interval(alpha=0.95, loc=np.mean(cal_500_data['calcium']),
                 scale=st.sem(cal_500_data['calcium'])))


#%%
# 4 - Creating new age category for cal_500_data

cal_500_data['AgeCat'] = np.where((cal_500_data['age'] >= 50),
                                  '>= 50 years old',
                                  '< 50 years old')

print(cal_500_data.head())

# n=500, 95% CI for women younger than 50
print(st.norm.interval(alpha=0.95, loc=np.mean(cal_500_data[cal_500_data['AgeCat'] == '< 50 years old']['calcium']),
                 scale=st.sem(cal_500_data[cal_500_data['AgeCat'] == '< 50 years old']['calcium'])))




