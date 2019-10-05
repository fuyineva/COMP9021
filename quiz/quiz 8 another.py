#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 21:06:02 2018

@author: seele
"""

import sys
from random import seed, randint
from array_queue import *


dim = 10
grid = [[0] * dim for i in range(dim)]

def display_grid():
    for i in range(dim):
        print('    ', end = '')
        for j in range(dim):
            print(' ', grid[i][j], end = '')
        print()
    print()


def findnext(my_queue,direction):
    nextpath=[]
    (row,col)=my_queue[-1]
    if direction==(1,0):
        turning=[(0,-1),(1,0),(0,1)]
    elif direction==(-1,0):
        turning=[(0,1),(-1,0),(0,-1)]
    elif direction==(0,1):
        turning=[(1,0),(0,1),(-1,0)]
    else:
        turning=[(-1,0),(0,-1),(1,0)]
    for (i,j) in turning:
        r=row+i
        print(r)
        c=col+j
        print(c)
        if r>=0 and r<dim and c>=0 and c<dim and grid[r][c]==1:
            temp=[]
            if (r,c) in my_queue:
                pass
            else:
                temp=my_queue[:]
                temp.append((r,c))
                print(temp)
                nextpath.append(temp)
                print(nextpath)
                
    return nextpath
        
                                        
def leftmost_longest_path_from_top_left_corner():
    queue=ArrayQueue()
    route=[]
    my_queue=None
    if grid[0][0] == 1 :
        route.append((0,0))
        queue.enqueue(route)
        while not queue.is_empty():
            my_queue=queue.dequeue()
            print(queue._data)
            print(my_queue)
            if len(my_queue)>1:
                direction=(my_queue[-1][0]-my_queue[-2][0],my_queue[-1][1]-my_queue[-2][1])
            else:
                direction=(0,1)                           
            nextpath=findnext(my_queue,direction)
            for i in range(len(nextpath)):
                queue.enqueue(nextpath[i])
    return my_queue                                    
                                        


provided_input = input('Enter one integer: ')
try:
    seed_arg = int(provided_input)
except:
    print('Incorrect input, giving up.')
    sys.exit()
    
seed(seed_arg)
# We fill the grid with randomly generated 0s and 1s,
# with for every cell, a probability of 1/2 to generate a 0.
for i in range(dim):
    for j in range(dim):
        grid[i][j] = randint(0, 1)
        
print('Here is the grid that has been generated:')
display_grid()

path = leftmost_longest_path_from_top_left_corner()
if not path:
    print('There is no path from the top left corner')
else:
    print(f'The leftmost longest path from the top left corner is {path}')