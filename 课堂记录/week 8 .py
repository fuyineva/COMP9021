#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 17:46:15 2018

@author: seele
"""

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class Linkedlist:
    def __init__(self, L = None , key = lambda x: x):
        self.key = key
        if not L:
            self.head = None
            self.length = 0
        else:
            self.head = Node(L[0])
            node = self.head
            self.length = 1
            #go through each element in what remains of the sequance
            for e in L[1:]:
                # make a new node out at the element we process
                new_node = Node(e)
                # ...and link it to what is currently the last node
                # in the linked list under construction
                node.next = new_node
                # Now the newly created 
                #
                node = new_node
                self.length += 1
                
    def __len__(self):
        
        return self.length
    
    def print_list(self,separator = ', '):
        if self.head:
            # collect all nodes
            # first getting the first node's value
            nodes = []
            node = self.head.next
            # ...and the,starting from the node following the head
            # if any,putting that node in the list of nodes
            # and moving to its following node, if any.
            while node:
                nodes.append(str(node.value))
                node = node.next
            print(separator.join(nodes))
            
    
    def extend(self,LL):
        if not self.head:
            self.head = LL.head
            return
        node = self.head
        # go all the way to the end of my linked list
        while node.next:
            node = node.next
        # connect last node to LL's head
        node.next = LL.head
        
    
    def is_sorted(self):
        if len(self)<2:
            return True
        node = self.head
        #for as long as the curreny node has a following node
        while node.next:
            # if following node's value is strictly smaller
            if self.key(node.next.value) < self.key(node.vvalue):
                return False
            node = node.next
        return True
            
    def delete_element(self,to_delete):
        if not self.head:
            return
        if self.head.value == to_delete:
            self.head = self.head.next
            return
        node = self.head
        #for as long as current node has following node and that following node
        #does not store the value to delete,then keep moving
        while node and node.value != to_delete:
            node = node.next
        # if next node exists,it has to store the value to delete
        if node.next:
            node.next = node.next.next
    
    def reverse(self):
        if len(self)<2:
            return
        R = self.head
        node = self.head.next
        self.head.next = None
        while node.next:
            next_node = node.next
            node.next = R
            R = node
            node = next_node
        node.next = R
        self.head = node
        
    def recursive_reverse(self):
        if len(self) <2:
            return
        node = self.head
        while node.next.next:
            node = node.next
        new_head = node.next
        node.next = None # cut link 
        self.recursive_reverse()
        new_head.next = self.head
        self.head = new_head