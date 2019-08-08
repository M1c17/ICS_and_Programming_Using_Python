#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 21:06:50 2019

@author: MASTER
"""

#genPrimes
'''Write a generator, genPrimes, that returns the sequence of prime numbers on 
successive calls to its next() method: 2, 3, 5, 7, 11
Have the generator keep a list of the primes it's generated.
A candidate number x is prime if (x % p) != 0 for all earlier primes p.'''

def genPrimes():
    primes = [] #primes generated so far
    guess = 1
    
    while True:
        guess +=1
        for p in primes:
            if guess % p == 0:
                break
        else:
            primes.append(guess)
            yield guess
            print(primes)

       
p = genPrimes()
print(p.__next__())
print(p.__next__())            
print(p.__next__())                
print(p.__next__())    
print(p.__next__()) 
   
        