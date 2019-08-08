#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 18:52:33 2019

@author: MASTER
"""
#get the sorted string of a dictionary 
def str(hand):
    output = ''
    hand_keys = sorted(hand.keys())
    for letter in hand_keys:
        for j in range(hand[letter]):
            output += letter
    return output
        
hand = {'a':3, 'b':1, 'n':2}
str(hand)