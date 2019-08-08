#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 18:28:45 2019

@author: MASTER
"""

# Write an iterative function to find factorial of any number x
# 5! = 4*3*2*1 = 120

#recursion

def factorial(x):

    if x == 0:  # base case 
        return 1
    else:       # recursion 
        return x * factorial(x-1)

print(factorial(5))