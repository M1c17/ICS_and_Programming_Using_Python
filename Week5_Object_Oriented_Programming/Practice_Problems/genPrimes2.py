#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 22:56:29 2019

@author: MASTER
"""

def genPrimes():
    p = 1
    primes = []
    while True:
        p += 1
        if all([p % i != 0 for i in primes]):
            #generates boolean used to decide if to append the list 
            primes.append(p)
            yield p
            
p = genPrimes()
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())
print()

#avoided the "for... else" structure by checking whether 
#the current variable is the last one in the list I'm looping.

def genPrimes():
    n = 1
    primeList = []
    while True:
        n += 2
        for p in primeList:
            if n % p == 0:
                break
            else:
                if p == primeList[-1]:
                    yield n
        primeList.append(n)
        
p = genPrimes()
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())