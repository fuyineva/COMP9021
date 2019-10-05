#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 22:46:13 2018

@author: seele
"""

import sys

open_file = input('Which data file do you want to use?:')

try:
    f = open(open_file,'r')
    
except FileNotFoundError:
    print("Your file not be founded,give up")
    sys.exit()
    

l=[]
for line in f:
        l.append(line.split('R'))
print(l)

l1 = []
l2 = []
for i in range(len(l)):
    a = int(l[i][0][2])
    b = int(l[i][0][4])
    l1.append(a)
    l1.append(b)
    l2.append([a,b])
    
l1 = list(set(l1))
print(l1)
print(l2)

    