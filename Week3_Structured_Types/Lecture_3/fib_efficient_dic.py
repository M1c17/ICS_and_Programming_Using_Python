#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 11:58:41 2019

@author: MASTER
"""
def fib(n):
    print(n)
    if n == 1:
        return 1
    elif n == 2 :
        return 2
    else:
        return fib(n-1) + fib(n-2)
    
    

#FIBONACCI & DICTIONARIES
#method sometimes call memoization

def fib_efficient(n, d): # the nth of fib & dictionary
    if n in d:
        return d[n] # if i already done the work just look it up and return it
    else: # recursive call
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        print(d)
        d[n] = ans # store the value away in the dictionary 
        return ans 
        
d = {1:1, 2:2} # base cases

argToUse = 5
print("")
print('using fib')
print(fib(argToUse))
print("")
print('using fib_efficient')
print(fib_efficient(argToUse, d))
