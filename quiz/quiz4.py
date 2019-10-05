#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 11:07:17 2018

@author: seele
"""

# Uses National Data on the relative frequency of given names in the population of U.S. births,
# stored in a directory "names", in files named "yobxxxx.txt with xxxx being the year of birth.
#
# Prompts the user for a first name, and finds out the first year
# when this name was most popular in terms of frequency of names being given,
# as a female name and as a male name.
# 
# Written by *** and Eric Martin for COMP9021


import os
from collections import defaultdict

first_name = input('Enter a first name: ')
directory = 'names'

min_male_frequency = 0
male_first_year = None
min_female_frequency = 0
female_first_year = None

# Replace this comment with your code


names_years_count_male = defaultdict(list)
names_years_count_female = defaultdict(list)
years_sum_count_M = defaultdict(list)
years_sum_count_F = defaultdict(list)
for filename in os.listdir(directory):
    if not filename.endswith('txt'):
        continue
    year = int(filename[3:7])
    with open(directory + '/' + filename) as data_file:
        for line in data_file:
             name,gender,count = line.split(',')
             if gender == 'M':
                 years_sum_count_M[year].append(int(count))
                 couple_M = (year,int(count))
                 names_years_count_male[name].append(couple_M)
             else:
                 years_sum_count_F[year].append(int(count))
                 couple_F = (year,int(count))
                 names_years_count_female[name].append(couple_F)
                 
                 

l = [] 
k = []
for year_M in years_sum_count_M:
    years_sum_count_M[year_M] = sum( years_sum_count_M[year_M])
    
    
for year_F in years_sum_count_F:    
    years_sum_count_F[year_F] = sum( years_sum_count_F[year_F])



if first_name in names_years_count_female:
    for i in range(len(names_years_count_female[first_name])):
        female_frequency = names_years_count_female[first_name][i][1]/years_sum_count_F[names_years_count_female[first_name][i][0]]
        cou = (female_frequency,names_years_count_female[first_name][i][0])
        l.append(cou)
    min_female_frequency = sorted(l,reverse = True)[0][0]*100
    female_first_year = sorted(l,reverse = True)[0][1]


if first_name in names_years_count_male:
    for j in range(len(names_years_count_male[first_name])):
        male_frequency = names_years_count_male[first_name][j][1]/years_sum_count_M[names_years_count_male[first_name][j][0]]
        co = (male_frequency,names_years_count_male[first_name][j][0])
        k.append(co)

    min_male_frequency = sorted(k,reverse = True)[0][0]*100
    male_first_year = sorted(k,reverse = True)[0][1]
    

if not female_first_year:
    print(f'In all years, {first_name} was never given as a female name.')
else:
    print(f'In terms of frequency, {first_name} was the most popular '
          f'as a female name first in the year {female_first_year}.\n'
          f'  It then accounted for {min_female_frequency:.2f}% of all female names.'
          )
if not male_first_year:
    print(f'In all years, {first_name} was never given as a male name.')
else:
    print(f'In terms of frequency, {first_name} was the most popular '
          f'as a male name first in the year {male_first_year}.\n'
          f'  It then accounted for {min_male_frequency:.2f}% of all male names.'
          )


               

