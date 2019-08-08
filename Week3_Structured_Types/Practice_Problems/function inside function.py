#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 15:06:56 2019

@author: MASTER
"""

def applyToEach(L, f):
    '''Assumes L is f a function 
    mutates L by replacing each element, e 
    of L by f(e)'''
    for i in range(len(L)):
        L[i] = f(L[i])
        
 
L = [1, -2, 3.4]
applyToEach(L, abs)
print(L)
applyToEach(L, int)
print(L)


def applyFunction(L, x):
    for f in L:
        print(f(x))
        
applyFunction([abs,int], -4.3)
