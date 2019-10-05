#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 19:40:28 2018

@author: seele
"""

def permute(L):
    if len(L) <= 1:
        yield L
    else:
        for i in range(len(L)):
            L[0],L[i] = L[i],L[0]
            for L1 in permute(L[1:]):
                yield [L[0]]+L1

for i in permute([1,2,3,4]):
    print(i)
    