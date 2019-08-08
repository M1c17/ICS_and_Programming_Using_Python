#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
find a positive integer that is divisible by 11 and 12 
 x = 132 

"""
x = 1
while True:
    if x % 11 == 0 and x % 12 == 0 :
        break 
    x = x + 1
print('x is divisible by 11 and 12')