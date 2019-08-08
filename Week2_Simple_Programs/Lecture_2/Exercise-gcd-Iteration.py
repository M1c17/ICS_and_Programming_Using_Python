#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 18:50:04 2019

@author: MASTER
"""

# The greatest common divisor of two positive integers is the largest 
# integer that divides each of them without remainder

# iterative for loop 
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
# first determine the smaller of the two number since gcd can only be less
# or equal to the smalles number 
    if a < b:
        smaller = a
    else:
        smaller = b
# in each iteration, we check if our number perfectly 
# divides both the input numbers      
    for i in range(1,smaller+1):
        if (a % i == 0 ) & (b % i == 0):
            gcd = i 
    return gcd 

print(gcdIter(24,16))
print(gcdIter(48,256))