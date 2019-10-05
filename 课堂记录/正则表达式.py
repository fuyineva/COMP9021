#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 20:50:30 2018

@author: seele
"""

from re import findall

L = 'dasd+das == das'
words = findall('[A-Z a-z]+',L)
print(words)

l = set(''.join(words))
print(l)

str.maketrans()

string = "A1.45，b5，6.45，8.82"
print(findall(r"\d+\.?\d*",string)) #?代表前面的.可以没有