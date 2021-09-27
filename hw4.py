#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 21:00:58 2021

@author: matthewayala
"""
# Importing libraries and data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

healthdata = pd.read_csv('HealthData.csv')

print(healthdata.head())
print(healthdata.shape)


#%%
# 2 - Making a histogram

g = plt.hist(healthdata['BMI'], edgecolor = 'black')
plt.xlabel('Body Mass Index (BMI)')
plt.ylabel('Count')

plt.show()

#%%
# 3 - Calculating mean and SD

print(healthdata['BMI'].mean()) # Mean

print(np.std(healthdata['BMI'])) # Standard Deviation

#%%
# 4 - Creating Boxplot
income_names = {1:'Low', 2:'Medium',3:'High'} # Dictionary to map new names to income values

renamed_df = healthdata.replace({'Income':income_names}) # Renaming income values

sns.boxplot(data = renamed_df, x = 'Income', y = 'BMI', order = ['Low','Medium','High']).set(title = 'BMI vs. Income')

plt.show()

#%%
# 6 - Calculating mean, std, variance, IQR of income groups

stats_2 = renamed_df.groupby('Income')['BMI'].describe()

print(stats_2)

# Calculating variance
print(np.var(renamed_df[renamed_df['Income'] == 'Low']['BMI'])) # Low income variance

print(np.var(renamed_df[renamed_df['Income'] == 'Medium']['BMI'])) # Medium income variance

print(np.var(renamed_df[renamed_df['Income'] == 'High']['BMI'])) # High income variance


#%%
# 7 - Creating Histogram of hemoglobin

plt.hist(renamed_df['Hemoglobin'], edgecolor = 'black')
plt.xlabel('Hemoglobin')
plt.ylabel('Count')
plt.show()

#%%
# 8 - Creating histogram of hemoglobin stratified by sex.
sex_names = {1:'Female', 2: 'Male'}
renamed_df = renamed_df.replace({'Sex':sex_names})

sns.boxplot(data = renamed_df, x = 'Hemoglobin', y = 'Sex').set(title = 'Sex vs. Hemoglobin')

plt.show()


#%%
# 10 - Calculating mean and std of hemoglobin groups.


# Hemoglobin Stats 
print(renamed_df['Hemoglobin'].mean()) # Overall
print(renamed_df['Hemoglobin'].std())

print(renamed_df[renamed_df['Sex'] == 'Female']['Hemoglobin'].mean()) 
print(renamed_df[renamed_df['Sex'] == 'Male']['Hemoglobin'].mean()) 

print(renamed_df[renamed_df['Sex'] == 'Female']['Hemoglobin'].std()) 
print(renamed_df[renamed_df['Sex'] == 'Male']['Hemoglobin'].std()) 

#%%

# BMI Stats
print(renamed_df['BMI'].mean()) # Overall
print(renamed_df['BMI'].std())

print(renamed_df[renamed_df['Sex'] == 'Female']['BMI'].mean()) 
print(renamed_df[renamed_df['Sex'] == 'Male']['BMI'].mean()) 

print(renamed_df[renamed_df['Sex'] == 'Female']['BMI'].std()) 
print(renamed_df[renamed_df['Sex'] == 'Male']['BMI'].std()) 

