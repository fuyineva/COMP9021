#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 18:04:38 2018

@author: seele
"""

def f(n):
    if n:
        print(n)
        f(n-1)
        print(n)
        
def add_up(L):
    S = 0
    for e in L:
        S += e
    return S

def add_up_1(L):
    if not L:
        return 0
    return add_up_1(L[:-1]) + L[-1]

def add_up_2(L):
    if not L:
        return 0
    return add_up_2(L[1:]) + L[0]

def add_up_3(L):
    if not L:
        return 0
    if len(L) == 1:
        return L[0]
    return add_up_3(L[:len(L)//2]) + add_up_3(L[len(L)//2:])