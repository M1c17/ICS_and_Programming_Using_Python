#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 20:00:23 2019

@author: MASTER
"""

# newborn pair of rabbits (1 female , 1 male) are put in a pen 
# rabbits mate at age of one month
# rabbits have a one month gestation period 
# assume rabbits never die, that female always produces one new pair 
# 1 male 1 female every month from its secon month on 

# how many female rabbits are ther at the end of one year?
'''
Recursive case
females(n) = females(n-1) +females(n-2)
bases cases :
    female (0) = 1
    female (1) = 1
'''

def fib(x):
    '''assumes x an int >=0
    returns Fibonacci of x'''
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
print(fib(7))