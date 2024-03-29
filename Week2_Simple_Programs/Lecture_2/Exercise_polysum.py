#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 17:29:10 2019

@author: MASTER
"""
from math import*

# A regular polygon has n number of sides. Each side has length s.
#
# The perimeter of a polygon is: length of the boundary of the polygon
# Write a function called polysum that takes 2 arguments, n and s.
# This function should sum the area and square of the perimeter of the regular
# polygon. The function returns the sum, rounded to 4 decimal places.

def polysum(n,s):
    
    import math
    area = (0.25 * n * (s ** 2)) / math.tan(math.pi/n)
    perimeter = n * s
    
    result = area + perimeter ** 2 
    return round(result,4)

print(polysum(2, 4))


def polysum(n,s):
    
    area = (0.25 * n * (s ** 2)) / tan(pi/n)
    perimeter = n * s
    
    result = area + perimeter ** 2 
    return round(result,4)

print(polysum(2, 4))