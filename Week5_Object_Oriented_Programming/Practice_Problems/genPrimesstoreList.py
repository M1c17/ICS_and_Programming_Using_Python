#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 22:24:22 2019

@author: MASTER
"""

def genPrimes():
    p = 1
    primes = []
    while True:
        p += 2
        if all(p%2 for i in primes):
            primes += [p]
            yield p 
            
p = genPrimes()
print(p.__next__())
print(p.__next__())                
#you cant list an infinite series because it wont stop
# so you can use listcomp or you can store the result in a list

listPrimes = []
gp = genPrimes()
for _ in [1]* 10:
    listPrimes.append(next(gp))
print('\n', listPrimes)



        