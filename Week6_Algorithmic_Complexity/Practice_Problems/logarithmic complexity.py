#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 18:38:46 2019

@author: MASTER
"""

# write code that convert an int into a str

def intTostr(i):
    digits = '0123456789'
    
    if i == 0:
        return 0
    result = '' 
    
    while i > 0:
        #take i, gets its remainder base 10 - the lowest order digit - 
        #index into digits & add it onto result 
        result = digits[i % 10] + result
        # shift right 
        i = i //10
    return result 