#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 18:06:09 2018

@author: seele
"""

from math import sqrt


class SecondOrderEqyationException(Exception):
    def __init__(self,message):
        self.message = message
        

class SecondOrderEqyation:
    def __init__(self,*,a ,b ,c ):
        if a == 0:
            raise SecondOrderEqyationException('a should not be set to 0')
        self.a = a 
        self.b = b
        self.c = c
        self.compute_delta()
        self.compute_roots()
        
        
    def __repr__(self):
        return f'SecondOrderEqyation(a={self.a},b={self.b},c={self.c})'
    
    def __str__(self):
        if self.a == 1:
            output_string = 'x^2'
        elif self.a == -1:
            output_string = '-x^2'
        else:
            output_string = f'{self.a}x^2'
        if self.b == 1:
            output_string += ' + x'
        elif self.b == -1:
            output_string += ' - x'
        elif self.b>0:
            output_string += f' + {self.b}x'
        elif self.b<0:
            output_string += f' - {-self.b}x'
        if self.c>0:
            output_string += f' + {self.c}'
        if self.c<0:
            output_string += f' - -{self.b}'
        output_string += ' =0'
        return output_string
            
            
    def compute_delta(self):
        return self.b**2-4*self.a*self.c
    
    def compute_roots(self):
        delta = self.compute_delta()
        if delta < 0:
            return None,None
        if delta == 0:
            root = -self.b/(2*self.a)
            return root,root
        self.root_1 =(-self.b-sqrt(delta))/(2*self.a)
        self.root_2 =(-self.b+sqrt(delta))/(2*self.a)
        return self.root_1,self.root_2
    
    def change_equation(self,*,a = None, b=None, c=None):
        if a == 0:
            raise SecondOrderEqyationException('a should not be set to 0')
        if a is not None:
            self.a = a
        if b is not None:
            self.b = b
        if c is not None:
            self.c = c
        self.compute_delta()
        self.compute_roots()
        
        
class SecondOrderEqutions:
    def __init__(self,equations):
        self.equations = equations
if __name__ == '__main__':
    import doctest
    doctest.testmod()