#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 10:57:28 2018

@author: seele
"""

import sys
from math import sqrt


def f(n):
    '''
    Won't be tested for n greater than 10_000_000
    
    >>> f(3)
    The largest prime strictly smaller than 3 is 2.
    >>> f(10)
    The largest prime strictly smaller than 10 is 7.
    >>> f(20)
    The largest prime strictly smaller than 20 is 19.
    >>> f(210)
    The largest prime strictly smaller than 210 is 199.
    >>> f(1318)
    The largest prime strictly smaller than 1318 is 1307.
    '''
    if n <= 2:
        sys.exit()
    largest_prime_strictly_smaller_than_n = 0
    # Insert your code here
    if n == 3:
        largest_prime_strictly_smaller_than_n = 2
    else:
        c = n
        s=int(sqrt(n))+1
        lp=2
        while lp<s and c>0:
            if c%lp == 0:
                c-=1
                lp=2
            else:
                lp+=1
            
              
        largest_prime_strictly_smaller_than_n = c
    print(f'The largest prime strictly smaller than {n} is {largest_prime_strictly_smaller_than_n}.')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
