#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 23:47:15 2018

@author: seele
"""

# Randomly generates a binary search tree whose number of nodes
# is determined by user input, with labels ranging between 0 and 999,999,
# displays it, and outputs the maximum difference between consecutive leaves.
#
# Written by *** and Eric Martin for COMP9021

import sys
from random import seed, randrange
from binary_tree_adt import *

# Possibly define some functions
leaves_list = []
def traversal(tree):
    if tree.value is None:
        return
    else:
        if tree.left_node.value is None and tree.right_node.value is None:
            leaves_list.append(tree.value)
        traversal(tree.left_node)  
        traversal(tree.right_node)
    return leaves_list
    

    
def max_diff_in_consecutive_leaves(tree):
    traversal(tree)
    print(leaves_list)
    max_difference = 0
    for i in range(0, len(leaves_list)-1):
        more_big = abs(leaves_list[i] - leaves_list[i+1])
        if more_big > max_difference:
            max_difference = more_big
    return max_difference
    # Replace pass above with your code


provided_input = input('Enter two integers, the second one being positive: ')
try:
    arg_for_seed, nb_of_nodes = provided_input.split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, nb_of_nodes = int(arg_for_seed), int(nb_of_nodes)
    if nb_of_nodes < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
tree = BinaryTree()
for _ in range(nb_of_nodes):
    datum = randrange(1000000)
    tree.insert_in_bst(datum)
print('Here is the tree that has been generated:')
tree.print_binary_tree()
print('The maximum difference between consecutive leaves is: ', end = '')
print(max_diff_in_consecutive_leaves(tree))