#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 19:15:27 2018

@author: seele
"""

from binary_tree_adt import *
from math import log


class PriorityQueue(BinaryTree):
    def __init__(self,value=None):
        super().__init__()
        self.value = value
        self.n = 0
        if self.value is not None:
            self.left_node = PriorityQueue()
            self.right_node = PriorityQueue()
        else:
            self.left_node = None
            self.right_node = None

    def insert(self, value):
        if self.value is None:
            self.value = value
            self.left_node = PriorityQueue()
            self.right_node = PriorityQueue()
        elif self.left_node.value is None and self.right_node.value is None:
            if value < self.value:
                value,self.value = self.value,value
            self.left_node = PriorityQueue(value)
            self.n+=1
        elif self.left_node.value is not None and self.right_node.value is None:
            if value < self.value:
                value,self.value = self.value,value
            self.right_node = PriorityQueue(value)
            self.n+=1
        else:
            if self.left_node.value is not None and self.right_node.value is not None:
                if value < self.value:
                    value,self.value = self.value,value
                if self.left_node.n<2:
                    self.left_node.insert(value)
                elif self.left_node.n==2 and self.right_node.n<2:
                    self.right_node.insert(value)
                else:
                    if self.left_node.n==2 and self.right_node.n==2:
                        self.left_node.insert(value)
        
        
        