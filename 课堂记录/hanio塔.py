#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 19:07:34 2018

@author: seele
"""

def hanoi(n,A,B,C):
    if n == 1:
        print(f'Move disk from {A} to {C}')
    else:
        hanoi(n-1,A,C,B) #from A to B 
        print(f'Move disk from {A} to {B}')
        hanoi(n-1,B,A,C) #from B to C
        
        