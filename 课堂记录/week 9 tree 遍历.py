#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 19:19:33 2018

@author: seele
"""

from stack_adt import *
from collections import defaultdict

our_tree = {1:[2,4,5], 2:[3], 5:[6,11,13], 6:[7,8,10], 8:[9], 11:[12]}
#depth first search
def explore_tree_DFS(tree,root):
    stack = Stack()
    stack.push([root])
    while not stack.is_empty():
        path = stack.pop()
        print(path)
        if path[-1] in tree:
            for e in reversed(tree[path[-1]]):
                stack.push(path +[e])
                print(stack._data)

explore_tree_DFS(our_tree,1)   