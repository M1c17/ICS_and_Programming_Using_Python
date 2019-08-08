#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 13:33:43 2019

@author: MASTER
"""

#write a clas with functions __iter__ & __next__ 
#powertwo

class PowTwo:
    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        result = 2 ** self.n
        self.n += 1
        return result
    
P1 = PowTwo(5)

print((P1.__iter__()))
print() 
print(next(P1))
print(next(P1))
print(next(P1))
print(next(P1))
print(next(P1))

#write a code with generator 

def PowTwo(max_N = 0):
    n = 2
    while n < max_N:
        result = 2 ** n
        yield result
        n += 2
        
P2 = PowTwo(5)      
print(next(P2))
print(next(P2))
#print(next(P2))
#print(next(P2))
        

   