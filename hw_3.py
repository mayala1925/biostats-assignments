#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 17:49:27 2021

@author: matthewayala
"""
import pandas as pd
import numpy as np



# Reading in the file
birth_data = pd.read_csv('LowBirth.csv')


# Checking the first 5 rows and the shape of the data.
print(birth_data.head())
print(birth_data.shape)

# Answer to problem #1 is 100 because there are 100 rows
#%%
# Part 2 - Creating new variable Lowapgar5

birth_data['Lowapgar5'] = np.where((birth_data['APGAR5'] >= 5), 0, 1)

print(birth_data.head(10))

#%%
# Part 3 - Reporting proportions and 95% C.I
import scipy.stats

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m * 100, (m-h)* 100, (m+h) * 100

# 1
lowapgar_prop = (birth_data['Lowapgar5'].sum() / 100) * 100

print(lowapgar_prop)

# 95% C.I for lowapgar data.
mean_1, ci_ap1, ci_ap2 = mean_confidence_interval(birth_data['Lowapgar5'])
print(mean_1, ci_ap1,ci_ap2)

# 2
hem_prop = (birth_data['GRMHEM'].sum() / 100) * 100
print(hem_prop)
mean_2, ci_hem1, ci_hem2 = mean_confidence_interval(birth_data['GRMHEM'])
print(mean_2,ci_hem1,ci_hem2)

#%%
# 3

# Subsetting data for only mothers with toxemia.
tox_data = birth_data[birth_data['TOX'] == 1]

# Shows 21 mothers with toxemia.
print(tox_data.shape)

tox_hem_prop = (tox_data['GRMHEM'].sum() / 21) * 100

print(tox_hem_prop)

mean_3, ci_tox1,ci_tox2 = mean_confidence_interval(tox_data['GRMHEM'])

print(mean_3,ci_tox1,ci_tox2)

#%%
# 4

# Subsetting for mothers without toxemia

non_tox_data = birth_data[birth_data['TOX'] == 0]

# Shows 79 mothers without toxemia.
print(non_tox_data.shape)

non_tox_hem_prop = (non_tox_data['GRMHEM'].sum() / 79) * 100

print(non_tox_hem_prop)

mean_4, ci_nontox1,ci_nontox2 = mean_confidence_interval(non_tox_data['GRMHEM'])

print(mean_4, ci_nontox1, ci_nontox2)

