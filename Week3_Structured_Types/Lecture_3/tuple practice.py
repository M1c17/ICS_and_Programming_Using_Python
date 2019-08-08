#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 12:49:35 2019

@author: MASTER
"""
# TUPLES 
# Convenient for swapping variables
# it also allows me to return more than one value from a function 

def quation_and_remainder(x, y):
    r = x % y
    q = x // y
    return (q, r)
    
print(quation_and_remainder(4, 5))

###
def fun():
    str = 'abcdf'
    x = 3
    return(str, x) #Return tuple

str, x = fun()
print(str)
print(x)