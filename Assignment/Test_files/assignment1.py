#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 20:20:20 2018

@author: seele
"""

import sys
from itertools import product
        
open_file = input('Which data file do you want to use?:')

try:
    f = open(open_file,'r')
    
except FileNotFoundError:
    print("Your file not be founded,give up")
    sys.exit()

l=[]

#for line in f:
#    l.append(line.split())
#print(l)       
#
#for i in range(0,len(l)):
#    for j in range(0,len(l[i])):
#        l[i][j] = int(l[i][j])

#for r in range(0,len(l)):
    #l[r] = [int(element) for element in l[r]]
    
for line in f:
    l.append([int(v) for v in line.split()])
    
print(l)
layers = len(l)

binary_path = list(map(list,product([0,1],repeat = layers-1)))

for i in binary_path:
    i.insert(0,0)    

list_path = []
path = []
s_list_path = []
for k in range(len(binary_path)):
    for p in range(len(l)):
        if p < len(l):
            a = sum(binary_path[k][0:p+1])
            path.append(l[p][a])            
        else:
            break

n = 0
while n< len(path):
    b = sum(path[n:n+len(l)])
    list_path.append(path[n:n+len(l)])
    s_list_path.append(b)         
    n=n+len(l)

largest_sum = max(s_list_path)
print(f'The largest sum is: {largest_sum}')
nb_of_path = s_list_path.count(max(s_list_path))
print(f'The number of paths yielding this sum is: {nb_of_path}')

location = s_list_path.index(max(s_list_path))
shuchu = list_path[location]
print(f'The leftmost path yielding this sum is: {shuchu}')