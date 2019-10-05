#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 11:52:58 2018

@author: seele
"""

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)       
        
    def rearrange(self):
        current_node = self.head
        min_value = self.head
        Node1 = None
        Node2 = None
        Node3 = None
        Node4 = None
        while current_node.next_node:
            Node3 = Node4
            Node4 = current_node
            if min_value.value > current_node.next_node.value:
                min_value = current_node.next_node
                Node1 = Node3
                Node2 = current_node
                current_node = current_node.next_node
            else:
                current_node = current_node.next_node
        Node3 = Node3.next_node
        Node4 = Node4.next_node
        if not Node2:
            Node1 = Node3
            Node2 = Node4
        if not Node1:
            Node1 = Node4
        Node4.next_node = self.head
        Node1.next_node = None
        self.head = Node2
        
        first_node = self.head
        second_node = self.head.next_node
        change_first = self.head
        change_second = self.head.next_node
        new_begin = self.head.next_node
        while True:
            if second_node.next_node and second_node.next_node.next_node:
                change_first = second_node.next_node
                change_second = second_node.next_node.next_node
                first_node.next_node = change_second
                second_node.next_node = first_node
                first_node = change_first
                second_node = change_second
            else:
                if not second_node.next_node:
                    first_node.next_node = None
                    second_node.next_node = first_node
                    break
                break
            
        self.head = new_begin
        
        
        
        
        
        

            
    
        # Replace pass above with your code