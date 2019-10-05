#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 19:54:33 2018

@author: seele
"""

from stack_adt import *
from queue_adt import *
from collections import defaultdict

def tree():
    return defaultdict(tree)

our_tree = tree()
our_tree[1][2][3] = None
our_tree[1][4] = None
our_tree[1][5][6][7] = None
our_tree[1][5][6][8][9] = None
our_tree[1][5][6][10] =None
our_tree[1][5][11][12] = None
our_tree[1][5][13] = None

print(our_tree)
# our_tree = {1:[2,4,5], 2:[3], 5:[6,11,13], 6:[7,8,10], 8:[9], 11:[12]}
#depth first search
def explore_tree_DFS(tree):
    stack = Stack()
    stack.push(([],tree))
    while not stack.is_empty():
        path,tree = stack.pop()
        print(path)
        if tree:
            for e in reversed(list(tree.keys())):
                stack.push((path +[e],tree[e]))
                
explore_tree_DFS(our_tree)            

# Breadth_First Search
def explore_tree_BFS(tree):
    queue = Queue()
    queue.enqueue(([],tree))
    while not queue.is_empty():
        path,tree = queue.dequeue()
        print(path)
        if tree:
            for e in reversed(list(tree.keys())):
                stack.enqueue((path +[e],tree[e]))
                print(queue._data)
explore_tree_BFS(our_tree)
