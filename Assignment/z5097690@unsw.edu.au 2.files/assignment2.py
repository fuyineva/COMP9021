#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 14:32:46 2018

@author: seele
"""

import sys
import statistics

file_name = input('Which data file do you want to use? ')

L1=[]
L2=[]
try:
    f = open(file_name)
    R = f.readlines()
    #read is look at every line in the file
    if (R==[]):
        raise ValueError
        sys.exit()
    for line in R:
        data = line.split()
        for i in range(len(data)):
            if i % 2 == 0:
                L1.append(int(data[i]))#距离
            else:
                L2.append(int(data[i])) #鱼数量
except IOError:
    print("Your file not be founded,give up!")
    sys.exit()
except ValueError:
    print("Your file not be founded,give up!")
    sys.exit()


max_value = int(statistics.mean(L2))
min_value= int(min(L2))
me = int((max_value+min_value)/2)

def check(me):
    L=L2[:]
    for i in range(len(L)-1):
        if(L[i]<me):
            L[i+1] = L[i+1] - (me-L[i]) - (L1[i+1]-L1[i])
        if(L[i]>me):
            if( L[i]-me > (L1[i+1]-L1[i])):
                L[i+1]=L[i+1] + (L[i]-me) - ((L1[i+1]-L1[i]))
            if( L[i]-me <= (L1[i+1]-L1[i])):
                pass
        if(L[i]==me):
            pass
    if(L[-1]>me):
        # me can be achieved 
        return 1
    if(L[-1]<me):
        # me cannot be reached
        return 2
    if(L[-1]==me):
        #this is what we want
        return 0
    
last = 0
while check(me)!=0:
    if(check(me)==2):
        if max_value != me:
            max_value= me
            me= int((max_value+min_value)/2)
        else:
            last = me
            break
    if(check(me)==1):
        if min_value != me:
            min_value= me
            me= int((max_value+min_value)/2)
        else:
            last = me
            break
last = me


shuchu = int(last)
print(f'The maximum quantity of fish that each town can have is {shuchu}.')
    