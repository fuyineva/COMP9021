#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 17:06:14 2018

@author: seele
"""

class Tree:
    def __init__(self,value = None):
        self.value = value
        if value is None:
            self.left_subtree = None
            self.right_subtree = None
        else:
            self.left_subtree = Tree()
            self.right_subtree = Tree()
        