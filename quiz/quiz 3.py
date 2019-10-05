#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 18:09:34 2018

@author: seele
"""

# Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and finds out, for a given direction being
# one of N, E, S or W (for North, East, South or West) and for a given size greater than 1,
# the number of triangles pointing in that direction, and of that size.
#
# Triangles pointing North:
# - of size 2:
#   1
# 1 1 1
# - of size 3:
#     1
#   1 1 1
# 1 1 1 1 1
#
# Triangles pointing East:
# - of size 2:
# 1
# 1 1
# 1
# - of size 3:
# 1
# 1 1
# 1 1 1 
# 1 1
# 1
#
# Triangles pointing South:
# - of size 2:
# 1 1 1
#   1
# - of size 3:
# 1 1 1 1 1
#   1 1 1
#     1
#
# Triangles pointing West:
# - of size 2:
#   1
# 1 1
#   1
# - of size 3:
#     1
#   1 1
# 1 1 1 
#   1 1
#     1
#
# The output lists, for every direction and for every size, the number of triangles
# pointing in that direction and of that size, provided there is at least one such triangle.
# For a given direction, the possble sizes are listed from largest to smallest.
#
# We do not count triangles that are truncations of larger triangles, that is, obtained
# from the latter by ignoring at least one layer, starting from the base.
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))


def triangles_in_grid():   
    finally_list = defaultdict(list)
    for p in triangles_N(grid):
        finally_list['N'].append(p)
    for a in triangles_S():
        finally_list['S'].append(a)
    for b in triangles_W():
        finally_list['W'].append(b)
    for q in triangles_E():
        finally_list['E'].append(q)
    
    return finally_list
    # Replace return {} above with your code

# Possibly define other functions
    
def change_list(list_c):
    change = [[jj[ii] for jj in list_c] for ii in range(len(list_c[0]))]
    return change
#第一步是把23
#	 69
#	 05
#	 用ij=ji换成
#	 260
#	 359
def change_grid_90(grid_origanal):
    global new_grid
    new_grid = grid_origanal
    new_grid.reverse()
    new_grid = change_list(new_grid)
    
    return new_grid
#第二步是把260	
#	 359
#	 反转换成
#	 359
#	 260  得逆时针转的矩阵
def triangles_N(grid):
    grid = grid
    list_N = []
    l = []
    couple = ()
    large_size = int((len(grid)+1)/2)
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                continue
            else:
                m_size = 0
                for size in range(large_size,1,-1):
                    if  i+size-1 >= len(grid) or j-size+1 < 0 or j+size-1 >= len(grid):
                        continue
                    else:
                        for k in range(2*size-1):
                            if grid[i+size-1][j-size+1+k] == 0:
                                m_size = 0
                                break                                                        
                            else:
                                pass
                            if m_size < size:
                               m_size = size
                if m_size != 0:
                    l.append(m_size)
                
    for f_size in l:
        nb_of_size = l.count(f_size)
        couple = (f_size,nb_of_size)
        list_N.append(couple)
        list_N = list(sorted(set(list_N)))       
        list_N.reverse()

    return list_N

def triangles_S():
    grid_W1 = change_grid_90(grid)
    grid_S = change_grid_90(grid_W1)
    list_S = triangles_N(grid_S)
    
    return list_S

            
def triangles_W():
    grid_W = change_grid_90(grid)
    list_W = triangles_N(grid_W)
    
    return list_W


def triangles_E():
   grid_W2 = change_grid_90(grid)
   grid_SS = change_grid_90(grid_W2)
   grid_1  = change_grid_90(grid_SS)
   list_E = triangles_N(grid_1)
    
   return list_E                             
                            

try:
    arg_for_seed, density, dim = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density, dim = int(arg_for_seed), int(density), int(dim)
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
    
seed(arg_for_seed)

grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]	
print('Here is the grid that has been generated:')
print(grid)
display_grid()
# A dictionary whose keys are amongst 'N', 'E', 'S' and 'W',
# and whose values are pairs of the form (size, number_of_triangles_of_that_size),
# ordered from largest to smallest size.
if grid == []:
    triangles = {}
elif grid == [[0]]:
    triangles = {}
else:    
    triangles = triangles_in_grid()


for direction in sorted(triangles, key = lambda x: 'NESW'.index(x)):
    print(f'\nFor triangles pointing {direction}, we have:')
    for size, nb_of_triangles in triangles[direction]:
        triangle_or_triangles = 'triangle' if nb_of_triangles == 1 else 'triangles'
        print(f'     {nb_of_triangles} {triangle_or_triangles} of size {size}')