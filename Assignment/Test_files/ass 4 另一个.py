#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 14:46:26 2018

@author: seele
"""

import sys
import re


file_name = input('Which data file do you want to use? ')

L1=[]
L2=[]
try:
    file = open(file_name)
    while True:
        Read=file.readline()
        print(Read)
        if (Read==''):
            break
        Temp=re.split(r'[\n , R ()]',Read)
        print(Temp)
        Temp_unit=[int(Temp[2]),int(Temp[3])]
        L2.append(Temp_unit)
        L1.append(int(Temp[2]))
        L1.append(int(Temp[3]))
    if(L2==[]):
        raise ValueError
except ValueError:
    print('Your file not be founded,give up!')
    sys.exit()
except IOError:
    print('Your file not be founded,give up!')
    sys.exit()
file.close()

L1=list(set(L1))
print('L1 is: ',L1)
print('L2 is: ',L2)

temp=[]
for i in L2:
    for j in L2:
        if(i[1]==j[0] and [i[0],j[1]] not in temp):
            temp.append([i[0],j[1]])
#print('temp 1',temp)

len_L=[]
for k in range(len(L2)):
    #if (len(temp) in len_L):
        #break
    for i in temp:
        for j in L2:
            if(i==j):
                L2.remove(j)
            if(i!=j and i[1]==j[0]):
                if([i[0],j[1]] not in temp):
                    temp.append([i[0],j[1]])
                    #print('temp: ',temp)
                    #n=temp[-1]
                    #print(n)
                    
#print('temp 2',temp)
#print('length', len_L)


print('The nonredundant facts are: ')
for i in L2:
    if(i not in temp):
        print(f'R({i[0]},{i[1]})')