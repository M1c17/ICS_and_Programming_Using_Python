#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 14:25:02 2019

@author: MASTER
"""

#COMPLEXITY OF BOGO SORT 

def bogo_sort(L):
    while not is_sorted(L):
        random.shuffle(L)
        
