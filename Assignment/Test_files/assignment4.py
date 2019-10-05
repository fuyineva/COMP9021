#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 14:46:26 2018

@author: seele
"""

import sys
import re

open_file = input('Which data file do you want to use?:')

try:
    f = open(open_file,'r')
    
except FileNotFoundError:
    print("Your file not be founded,give up")
    sys.exit()
    

l=[]
for line in f:
        l.append(re.split(r'[\n , R ()]',line))

print(l)

l1 = []
l2 = []
for i in range(len(l)):
    a = int(l[i][2])
    b = int(l[i][3])
    l1.append(a)
    l1.append(b)
    l2.append([a,b])
    
l1 = list(set(l1))

print(l1)
print('l2:', l2)

temp=[]
for i in l2:
    for j in l2:
        if i[1]==j[0] and [i[0],j[1]] not in temp:
            temp.append([i[0],j[1]])
print('temp  ', temp)

#temp是查重复的 是一个点可以走到的另一个点 eg 3到2到1 从3可以到1 如果3直接到1 则是重复
#重点：：：就是找一个点到另一个点最长路线 中间有隔的，如过没有且不是直接路径则删

for i in temp:
    for j in l2:
        if i==j:
            l2.remove(j) #去除是去掉已经存在最长的 不会影响后面判断
        if i!=j and i[1]==j[0]:
            if [i[0],j[1]] not in temp:
                temp.append([i[0],j[1]])
                #这里投个递归 就是从跳一点可以达到 进一次判断跳两个达到 再对比是否重复 从两个判断3个 一直到没有多余的
                #print('temp: ',temp)
                #n=temp[-1]
                #print('n  ',n)
print()                    
print(temp)
print(l2)
print('The nonredundant facts are: ')
for i in l2:
    if i not in temp:
        print(f'R({i[0]},{i[1]})')