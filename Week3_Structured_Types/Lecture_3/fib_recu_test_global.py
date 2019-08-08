#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 19:41:21 2019

@author: MASTER
"""

# Recursive implementation of Fibonacci sequence

def fib(n):
    '''Assumes n int > 0
    Retur Fibonacci of n'''
    global numFibCalls
    numFibCalls += 1 
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
    
def testfib(n):
    for i in range(n + 1):
        global numFibCalls
        numFibCalls = 0     
        print('fib of', i, ' = ', fib(i))
        print('fib called ', numFibCalls, 'times.')
print(testfib(6))