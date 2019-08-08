#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 19:52:49 2019

@author: MASTER
"""

# euclidean algorithm recursion

def euclidAlgo(a, b):
    # Base case is when b = 0
    if b == 0:
        return a
    # Recursive case
    else:
        return euclidAlgo(b, a % b)
    
print(euclidAlgo(24,16))
print(euclidAlgo(48,256))