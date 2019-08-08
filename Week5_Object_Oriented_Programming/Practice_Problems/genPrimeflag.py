#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 23:30:13 2019

@author: MASTER
"""

def genPrimes():
    primesList = []
    nextPrime = 2
    temp = 3
    while True:
        if nextPrime not in primesList:
            yield nextPrime
            primesList.append(nextPrime)
        flag = True
        for p in primesList:
            if (temp % p) == 0:
                flag = False
        if flag == True:
            nextPrime = temp
        temp += 1
        
p = genPrimes()
print(p.__next__())
print(p.__next__())            
print(p.__next__())                
print(p.__next__())    
print(p.__next__())