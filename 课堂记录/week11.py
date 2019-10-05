#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 18:10:06 2018

@author: seele
"""

class PriorityQueue:
    def __init__(self,capacity = 20):
        self.capacity = capacity
        self.pq = [None]*(capacity+1)
        self.size = 0
        
    def insert(self,value):
        self.size += 1
        # if self.size < self.capacity
        # otherwise self.pq needs to be extended
        self.pq[self.size]=value
        self._bubble_up(self.size)
        
    def _bubble_up(self,position):
        if position ==1:
            return
        parent_position = position // 2
        if self.pq[parent_position] < self.pq[position]:
            self.pq[parent_position],self.pq[position] = self.pq[position],self.pq[parent_position]
            self._bubble_up(parent_position)
            
    def process_top_element(self):
        if self.size == 0:
            return
        element_being_processed = self.pq[1]
        self.pq[1],self.pq[self.size]=self.pq[self.size],self.pq[1]
        self.size -= 1
        self._bubble_down(1)
        
        return element_being_processed
    
    
    def _bubble_down(self,position):
        position_of_largest_child = 2*position
        # if there is a right child(and the also a left child) and right child holds
        # largest value,then need to bubble down with right child
        if 2*position+1 <= self.size and self.pq[2*position+1] >= self.pq[2*position]:
            position_of_largest_child += 1
        if 2*position <= self.size and self.pq[position_of_largest_child] > self.pq[position]:
            self.pq[position_of_largest_child],self.pq[position] =\
                                    self.pq[position],self.pq[position_of_largest_child]
            self._bubble_down(position_of_largest_child) 
            
if self.left_node.value is not None and self.right_node.value is not None:
            self.left_node.insert_in_tree(2*i)
        elif self.left_node.value is None            