#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 08:40:31 2019

@author: MASTER
"""
#Suppose that you are given the following functions:
def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

#Here is a different piece of code for working with lists:
def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result
        
#For each of the following questions, indicate what value is returned.
# If you believe that an error will occur, write the word 'error'.

print(applyEachTo([inc, square, halve, abs], -3))
#[-2 , 9, -1.5, 3]
print(applyEachTo([inc, square, halve, abs], 3.0))
#[4.0, 9.0, 1.5, 3.0]
print(applyEachTo([inc, max, int], -3))