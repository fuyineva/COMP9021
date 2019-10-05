#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 18:47:41 2018

@author: seele
"""

import os
from collections import defaultdict

directory_name = 'names'

years_by_names = defaultdict(list)

for filename in os.listdir(directory_name):
    if not filename.endswith('txt'):
        continue
    year = int(filename[3:7])
    # opening 1 file for reading purpose
    # and 2 files for writing purpose
    with open(directory_name + '/' + filename) as data_file:
        for line in data_file:
             #extracting th 3 dirls from the line 
             name,gender,count = line.split(',')
             if gender == 'M':
                 break
             years_by_names[name].append(year)
    
for gap,starting_year,name in sorted([(years_by_names[name][i+1]-years_by_names[name][i],years_by_names[name][i],
                                           name)
    for name in years_by_names
    for i in range(len(years_by_names[name])-1)
    ] , reverse = True
    )[:10]:
    print(f'{name} was given in {starting_year}, and then {gap} years later')
                 