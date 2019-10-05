#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 20:30:41 2018

@author: seele
"""

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self):
    	L=self.duplicate()
    	n=len(L)
    	temp = L.value_at(n>>1)
    	if n%2 != 0:
    		while n>0:
    			L.delete_value(temp)
    			self.delete_value(temp)
    			self.append(temp)
    			n=n-1
    			if n%2 == 0:
    				temp = L.value_at((n-1)//2)
    			else:
    				temp = L.value_at(n>>1)
    	else:
    		while n>0:
    			L.delete_value(temp)
    			self.delete_value(temp)
    			self.append(temp)
    			n=n-1
    			if n%2 == 0:
    				temp = L.value_at(n>>1)
    			else:
    				temp = L.value_at((n-1)//2)
    	# while n>0:
    	# 	L.delete_value(temp)
    	# 	self.delete_value(temp)
    	# 	self.append(temp)
    	# 	n=n-1
    	# 	if n%2 == 0:
    	# 		temp = L.value_at((n-1)//2)
    	# 	else:
    	# 		temp = L.value_at(n>>1)