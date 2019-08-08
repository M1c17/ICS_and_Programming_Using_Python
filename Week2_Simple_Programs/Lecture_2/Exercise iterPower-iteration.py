#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 11:32:23 2019

@author: MASTER
"""

#Write an iterative function iterPower(base, exp) that calculates
#the exponential base ^ exp by simply using successive multiplication.
#For example, iterPower(base, exp) should compute
# by multiplying base times itself exp times. 
#
#This function should take in two values - base can be a 
#float or an integer; exp will be an integer >= 0. It should 
#return one numerical value. Your code must be iterative - use of 
#the ** operator is not allowed.


#iteration 

def iterPower(base,exp):
    result = 1
    while exp > 0:
        result *= base 
        exp -=1
    return result 

print(iterPower(2,3))






