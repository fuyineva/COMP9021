#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 20:14:45 2018

@author: seele
"""

def convert_to_binary(N):
    if N <= 1:
        print(N,end='')
    else:
        convert_to_binary(N//2)
        print(N%2,end='')
        