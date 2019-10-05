#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 14:13:35 2018

@author: seele
"""
import sys
from random import seed, randint


dim = 10
grid = [[None] * dim for _ in range(dim)]

def display_grid():
    for i in range(dim):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(dim)))
# Possibly define other functions
        
def replace_1_by_star(i,j):
    if grid[i][j] == 1:
        grid[i][j] = '*'
        if i:
            replace_1_by_star(i-1,j)
        if i < dim -1:
            replace_1_by_star(i+1,j)
        if j:
            replace_1_by_star(i,j-1)
        if j < dim -1:
            replace_1_by_star(i,j+1)

def replace_0_by_star(i,j):
    if grid[i][j] == 0:
        grid[i][j] = '*'
        if i:
            replace_0_by_star(i-1,j)
        if i < dim -1:
            replace_0_by_star(i+1,j)
        if j:
            replace_0_by_star(i,j-1)
        if j < dim -1:
            replace_0_by_star(i,j+1)
    

def check_1_by_star(i,j):
    if grid[i][j] == 1 and [i,j] not in l:
        l.append([i,j]) 
        if i:
            check_0_by_star(i-1,j)
        if i < dim -1:
            check_0_by_star(i+1,j)
        if j:
            check_0_by_star(i,j-1)
        if j < dim -1:
            check_0_by_star(i,j+1)
    return l

def check_0_by_star(i,j):
    if grid[i][j] == 0 and [i,j] not in l:
        l.append([i,j])
        if i:
            check_1_by_star(i-1,j)
        if i < dim -1:
            check_1_by_star(i+1,j)
        if j:
            check_1_by_star(i,j-1)
        if j < dim -1:
            check_1_by_star(i,j+1)
    return l
    
try:
    arg_for_seed, density = input('Enter two nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density = int(arg_for_seed), int(density)
    if arg_for_seed < 0 or density < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
# We fill the grid with randomly generated 0s and 1s,
# with for every cell, a probability of 1/(density + 1) to generate a 0.


for i in range(dim):
    for j in range(dim):
        grid[i][j] = int(randint(0, density) != 0)
print('Here is the grid that has been generated:')
display_grid()

# Replace this comment with your code
if grid[0][0] == 0:
    replace_0_by_star(0,0)
    change = 0
else:
    replace_1_by_star(0,0)
    change = 1

size_of_largest_homogenous_region_from_top_left_corner  = 0
for i in range(dim):
    for j in range(dim):
        if grid[i][j] == '*':
            grid[i][j] = change
            size_of_largest_homogenous_region_from_top_left_corner += 1
            
print(grid)          
print('The size_of the largest homogenous region from the top left corner is '
      f'{size_of_largest_homogenous_region_from_top_left_corner}.'
     )


max_size_of_region_with_checkers_structure = 0
# Replace this comment with your code
count_list = []
for i in range(dim):
    for j in range(dim):
        l = []
        if grid[i][j] == 0:
            count = len(check_0_by_star(i,j))
            count_list.append(count)
        else:
            count = len(check_1_by_star(i,j))
            count_list.append(count)

max_size_of_region_with_checkers_structure = max(count_list)

print('The size of the largest area with a checkers structure is '
      f'{max_size_of_region_with_checkers_structure}.'
     )


