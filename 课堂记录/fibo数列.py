#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 18:32:17 2018

@author: seele
"""

def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1)+fibo(n-2)
#复杂每次都要算前面 指数级增长
def fibo_1(n):
    if n <= 1:
        return n
    previours, current = 0, 1
    for _ in range(2,n+1):
        previours, current =  current ,previours+current   
    return current
  
def fibo_2(n,fibonacci = {0:0,1:1}):
    if n not in fibonacci:
        fibonacci[n] = fibo_2(n-1) + fibo_2(n-2)
    return fibonacci[n]

