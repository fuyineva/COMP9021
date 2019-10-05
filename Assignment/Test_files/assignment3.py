#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 14:31:00 2018

@author: seele
"""

import sys

open_file = input('Which data file do you want to use? ')

try:
    f = open(open_file,'r')
    
except FileNotFoundError:
    print("Your file not be founded,give up")
    sys.exit()



def jisuan(l):
    s=0
    for m in l:
        x=m[0]
        y=m[1]
        while y<m[3]:
            for n in l:
                if n[1]<=y<n[3] and n[0]<x<n[2]: #这个是重叠的 不记录 print就知道了 n[0]<x<n[2]保证点在矩形里 
                    y+=1                        # 也就是重叠部分的点
                    break
                elif n == l[-1]:#这个是不重叠的记录  取下不取上 while y<m[3] 没有等于 防止两个链接重复记录一个点
                    y+=1
                    s+=1
    return(s)


l=[]
for line in f:
        l.append(line.split())

for r in range(0,len(l)):
    l[r] = [int(element) for element in l[r]]

c = sorted(l)
print(c)     
kuan = jisuan(c)

for i in range(0,len(l)):
    l[i][0],l[i][1] = l[i][1],l[i][0]
    l[i][2],l[i][3] = l[i][3],l[i][2]
v = sorted(l)
chang = jisuan(v)

shuchu = chang*2 + kuan*2
print(f'The perimeter is: {shuchu}')