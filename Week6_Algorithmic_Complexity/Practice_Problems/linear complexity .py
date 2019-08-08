#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 19:37:54 2019

@author: MASTER
"""

# add characters of a string, assumed to be composed of decimal digits 
# it is linear in the length of str 
def addDigits(n):
    
    val = 0 #constant
    s = str(n)
    for c in s:
        val += int(c)#constant
    return val #constant 

c = addDigits('34343')
print(c)

#linear O(len(s)) but what in terms of input n?
#tricky part:
    #covert integerto str
    # iterate over length of string, not magnitud of input n 
    # so if its linear in the order of the length of the string 
    # its O(log(n)) in the size of the input n / base doesnt matter

#complexity can depend on number of recursive calls
import time

def factorial_iter(n):
    prod = 1 #constant
    for i in range(1, n+1): #constant
        prod *= i           #constant
    return prod             #constant

p = factorial_iter(5)
print(p)
#number of times around loop is n
#number the operations inside loop is a constant

#O() FOR RECURSIVE FACTORIAL

def fact_recur(n):
    """assume n > 0 """
    if n <= 1:
        return 1
    else:
        return n*fact_recur(n - 1)

p = fact_recur(5)
print(p)
    
#the number of the function call is linear in n 
start_clock = time.clock()
print(factorial_iter(5))
print("factorial_iter time: ", time.clock() - start_clock)
print(fact_recur(5))
print("factor_recur time:", time.clock() - start_clock)
