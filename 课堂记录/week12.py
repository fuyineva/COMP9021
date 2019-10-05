#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 18:01:57 2018

@author: seele
"""

def merge_sort(L):
    if len(L):
        return
    _merge_sort(L,list(L),0,len(L))
    
def _merge_sort(L1,L2,start,end):
    if end-start<2:
        return 
    _merge_sort(L2[:len(L2)//2],L1[:len(L2)//2])