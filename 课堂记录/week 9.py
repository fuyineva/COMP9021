#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 18:06:36 2018

@author: seele
"""

from stack_adt import *

def checks_parentheses_are_balenced(expression):
    kinds_of_parentheses = {')':'(', ']':'[', '}':'{'}
    stack = Stack()
    for s in expression:
        if s in '([{':
            stack.push(s)
        
        elif s in ')]}':
#            #if stack is empty: imbalanced
#            if stack.is_empty():
#                return False
#            #if ) top of the stack should contain(
#            #if ] top of the stack should contain[
#            #if } top of the stack should contain{
            try:
                if kinds_of_parentheses[s] != stack.peek():
                    return False
            except EmptyStackError:
                return False
            #pop corresponding opening bracket from stack
            stack.pop()
        
    return stack.is_empty()

        
def evaluate(expression):
    operations = {'+':lambda x,y:x+y,
                  '-':lambda x,y:y-x,
                  '*':lambda x,y:x*y,
                  '/':lambda x,y:y/x}
    stack = Stack()
    processing_number = False #为了验证612 这种 不是一位数的 因为遍历是一个一个的不分几位数
    for s in expression:
        if s.isdigit():
            if not processing_number:
                processing_number = True
                #push the first digit in a number that is posiibly many digits long
                stack.push(int(s))
            else:
                #s is another digit as part of a number whose
                #precious digit have been processed,and 'assembled' into a number
                #which is now on top of our stack
                stack.push(stack.pop()*10+int(s))
        else:
            # eithe we just stop processing a number,
            # or we stopped before; so processing number
            #becaom false or it is fakse already
            processing_number = False
            if s in '+-*/':
                stack.push(operations[s](stack.pop(),stack.pop()))
    result = stack.pop()
    if not stack.is_empty():
        print('Expression incorrect')
    return result
                
            
                
            
            