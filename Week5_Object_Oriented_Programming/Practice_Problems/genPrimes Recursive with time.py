#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 21:59:55 2019

@author: MASTER
"""

# recursive 
def genPrimes(n):
    p = 2
    while p <= n:
        next = p
        yield p
        prime_found = False
        while not prime_found:
            p+=1
            if all(p%i !=0 for i in genPrimes(int(p**(1/2)))):
                prime_found = True
                
p = genPrimes(17)
print(p.__next__())
print(p.__next__())            
print(p.__next__())            
print(p.__next__())    
print(p.__next__())
print(p.__next__())
print(p.__next__())

def timeit(s, n=1000000):
    """call with string & number - prints time then string"""
    from timeit import timeit
    print(f"{timeit(s, globals=globals(), number=n) :8e}   {s}")

print(timeit())