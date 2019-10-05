#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 14:01:50 2018

@author: seele
"""



# A dictionary whose keys are amongst 'N', 'E', 'S' and 'W',
# and whose values are pairs of the form (size, number_of_triangles_of_that_size),
# ordered from largest to smallest size.


triangles = {'N':[[3,5],[2,4],[1,1]],'S':[[4,6],[2,7]],'E':[[3,8],[5,2]],'W':[[2,3]]}
for direction in sorted(triangles, key=lambda x: 'NESW'.index(x)):
    print(f'\nFor triangles pointing {direction}, we have:')
#这个就是按照‘NESW’顺序 排序triangles，完事从‘N’开始读取, [3,5]是size和数量的值，运行就知道了。
    i=0
    for i in range(len(triangles[direction])):
        size =  triangles[direction][i][0]
        nb_of_triangles = triangles[direction][i][1]
        triangle_or_triangles = 'triangle' if nb_of_triangles == 1 else 'triangles'
        print(f'     {nb_of_triangles} {triangle_or_triangles} of size {size}')         
    

print(triangles['S'])