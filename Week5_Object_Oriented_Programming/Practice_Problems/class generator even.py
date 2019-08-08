#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 23:14:01 2019

@author: MASTER
"""

class Evens:
    def __init__(self, x = 0):
        self.x = x
    def __next__(self):
        self.x +=2
        return self.x
    def __iter__(self):
        return self 
    
ee = Evens(12)
print(ee.__next__())