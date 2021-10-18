#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 18:02:07 2021

@author: matthewayala
"""

# Importing data and libraries
import pandas as pd
import numpy as np
from scipy.stats import fisher_exact


data = pd.read_csv('eye.csv')

print(data.head())

#%%
#1 - Risk proportion of people with carrot gene requiring contact lenses.

carrot_people = data[data['carrot'] == 1]

# Risk proportion
print(len(carrot_people[carrot_people['lenses'] == 1]) / len(carrot_people))

#%%
#2 - Risk proportion of people without carrot gene requiring contact lenses

noncarrot_people = data[data['carrot'] == 0]

# Risk Proportion
print(len(noncarrot_people[noncarrot_people['lenses'] == 1]) / len(noncarrot_people))

#%%

#3 - Difference in risk proportion between carrot people and noncarrot people
print(0.4118 - 0.6531)

#%%

# 5- Risk ratio of people that have the carrot gene and people who do not have the carrot gene.

#print(0.4118 / 0.6531)

# Creating contingency table
cont_table = [[21,30],[32,17]]

cont_table = np.array(cont_table)

# Performing fisher exact test
odds_rat, p_val = fisher_exact(cont_table)

print(odds_rat,p_val)

#%%
# 7 - Calculating odds ratio.
odd_rat = (21 * 17) / (30 * 32)
print(odd_rat)



#%%
# 8 - New categorical variable for latitude levels.

data['Latitude_level'] = np.where((data['latitude'] >= 40),
                                  'High Latitude',
                                  'Low Latitude')

#%%
# 9 - Risk ratio for latitude

high_lat = data[data['Latitude_level'] == 'High Latitude']
low_lat = data[data['Latitude_level'] == 'Low Latitude']


highLatRisk = len(high_lat[high_lat['lenses'] == 1]) / len(high_lat)
lowLatRisk = len(low_lat[low_lat['lenses'] == 1]) / len(low_lat)

lat_ratio = highLatRisk / lowLatRisk

print(lat_ratio)

# Finding p-value

lat_table = np.array([[20,19],[33,28]])

lat_odds, p_val_odds = fisher_exact(lat_table)
print(lat_odds,p_val_odds)


