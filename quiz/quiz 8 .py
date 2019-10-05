#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 18:58:29 2018

@author: seele
"""

import sys
from random import seed, randrange

from queue_adt import *


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))


def find_next_point(need_queue,direction):
    nextstep=[]
    (row,colume)=need_queue[-1]
    if direction==(1,0):
        moving=[(0,-1),(1,0),(0,1)]
    elif direction==(-1,0):
        moving=[(0,1),(-1,0),(0,-1)]
    elif direction==(0,1):
        moving=[(1,0),(0,1),(-1,0)]
    else:
        moving=[(-1,0),(0,-1),(1,0)]
   
    for (i,j) in moving:
        r,c=row+i,colume+j
        if r>=0 and r<10 and c>=0 and c<10 and grid[r][c]==1:
            if (r,c) in need_queue:
                pass
            else:
                possible_path=need_queue[:]
                possible_path.append((r,c))
                nextstep.append(possible_path)
    return nextstep


def leftmost_longest_path_from_top_left_corner():
    queue=Queue()
    need_queue = []
    if grid[0][0] == 1 :
        queue.enqueue([(0,0)])
        while not queue.is_empty():
            need_queue=queue.dequeue()
            if len(need_queue)>1:
                direction=(need_queue[-1][0]-need_queue[-2][0],need_queue[-1][1]-need_queue[-2][1])
            else:
                direction=(0,1)
                           
            nextpath=find_next_point(need_queue,direction)
            for i in range(len(nextpath)):
                queue.enqueue(nextpath[i])
    return need_queue
    # Replace pass above with your code


provided_input = input('Enter one integer: ')
try:
    for_seed = int(provided_input)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
grid = [[randrange(2) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()
path = leftmost_longest_path_from_top_left_corner()
if not path:
    print('There is no path from the top left corner.')
else:
    print(f'The leftmost longest path from the top left corner is: {path}')
           