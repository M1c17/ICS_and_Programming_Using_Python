#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:01:21 2019

@author: MASTER
"""
### GLOBAL VARIABLES INSIDE LOCAL VARIABLES 
# TO TRACK THE EFFICIENTY OF THIS TWO FUNCTION 

def fib(n):
#How often do i call the function?
#accesible from outside scope of function 
    global numFibCalls
    numFibCalls +=1
    if n == 1:
        return 1
    elif n == 2 :
        return 2
    else:
        return fib(n-1) + fib(n-2)
    
    
def fib_efficient(n, d): 
#How often do i call the function?
#accesible from outside scope of function 
    global numFibCalls
    numFibCalls +=1
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        #print(d)
        d[n] = ans
        return ans 
    
    
numFibCalls = 0       

argToUse = 12
print("")
print('using fib')
print(fib(argToUse))
print('function calls', numFibCalls )
print("")
numFibCalls = 0 
d = {1:1, 2:2}
print('using fib_efficient')
print(fib_efficient(argToUse, d))
print('function calls', numFibCalls)




