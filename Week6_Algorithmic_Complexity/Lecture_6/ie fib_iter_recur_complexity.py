#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 14:02:33 2019

@author: MASTER
"""

def fib_iter(n):
    if n == 0:
        return 0  #constant O(1)
    elif n == 1:
        return 1  #constant O(1)
    else:
        fib_i = 0    #constant O(1)
        fib_ii = 1
        for i in range(n-1):
            tmp = fib_i
            fib_ii = fib_ii             #linear O(n)
            fib_ii = tmp + fib_ii
        return fib_ii                   #constant O(1)
    
#Best case: O(1)
#Worst case: O(1) + O(n) + O(1) = O(n)

def fib_recur(n):
    '''assumes n an int >= 0'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n-2) #O(c^n)
    
#Worst case: O(2^n)

    
    