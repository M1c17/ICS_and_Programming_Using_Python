#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 18:13:18 2019

@author: MASTER
"""

# Write an iterative function to find factorial of any number x
# 5! = 4*3*2*1 = 120
#iterative
def factorial(x):
    ans = 1 
    
    while x != 0:
        ans *= x
        x -=1
    return ans
    
print(factorial(5))