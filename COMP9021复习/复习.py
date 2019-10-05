#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 16:04:04 2018

@author: seele
"""

x = 2  #x is object
y = [1,2,3]

'''
x.__class__
Out[195]: int

y = [1,2,3]

y.__class__
Out[197]: list

x.__class__.__class__
Out[198]: type

y.__class__.__class__
Out[199]: type

y.__class__.__class__
Out[200]: type

'''
class b:
    pass

class a(b):
    pass

class c(a):
    pass
'''
c.__class__
Out[204]: type

object
Out[205]: object

object.__class__
Out[206]: type

type.__class__
Out[207]: type
'''
'''
 c.__mro__
Out[227]: (__main__.c, __main__.a, __main__.b, object)
'''

def get_sum_of_from(desired_sum,number):
    R =  _get_sum_of_from(desired_sum,number)
    if R is not None:
        return sorted(R)
    
    
    
def _get_sum_of_from(desired_sum,number):
    
    
    if desired_sum <0:
        return
    if number ==0:
        if desired_sum==0:
            return [[]]
        return
    L1 = _get_sum_of_from(desired_sum,number//10)
    L2 = _get_sum_of_from(desired_sum-number%10,number//10)

    if not L2:
        return L1
    L2 = [R + [number%10] for R in L2]
    if L1:
        return L1+L2
    else:
        return L2
        
    
    
    




