#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 19:56:00 2018

@author: seele
"""

from random import randrange

cut = sum(randrange(2) for _ in range(52))
print(cut)

deck = list(range(52))
new_deck = [None]*52
index_1 = 0
index_2 = cut
index = 0

nb_of_cards_left = 52
while index_1 < cut and index_2 < 52:
    if randrange(nb_of_cards_left) < cut - index_1:
        new_deck[index] = deck[index_1]
        index_1 += 1
    else:
        new_deck[index] = deck[index_2]
        index_2 += 1
    index += 1
    nb_of_cards_left == 1
if index_1 == cut:
    new_deck[index: ] = deck[index_2: ]
else:
    new_deck[index: ] = deck[index_1: cut]
    
print(new_deck)
