#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 21:48:12 2021

@author: matthewayala
"""
# Importing libraries and data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


fev_data = pd.read_csv('FEV.csv')
book_data = pd.read_csv('BookPrice.csv')

# Looking at the head of the data
print(fev_data.head())
print(book_data.head())

#%%
# Adding labels for non-smokers and smokers

fev_data['Smoke'] = np.where((fev_data['Smoke'] == 1), 'Smoker','Nonsmoker')

#%%
# 1 - Creating boxplots of FEV for smoker and nonsmoker groups

sns.boxplot(data = fev_data,x = 'Smoke', y = 'fev')

plt.title('Nonsmoker and Smoker FEV Boxplot')
plt.ylabel('Forced expiratory volume (Liters)')
plt.xlabel('Smoker Status')

#%%

# 2 - Histograms for the nonsmoker and smoker FEV

sns.histplot(data = fev_data, x = 'fev', hue = 'Smoke')

plt.title('Nonsmoker and Smoker FEV Histograms')
plt.xlabel('Forced expiratory volume (Liters)')

#%%
# 3 - Checking n for each group.

print(fev_data['Smoke'].value_counts()) # Each group n > 25

#%%
# 5 - Statistics

smoke_mean = fev_data.groupby(['Smoke']).mean()
print(smoke_mean)

mean_diff = 3.277 - 2.566
print('Mean Difference: ',mean_diff)

