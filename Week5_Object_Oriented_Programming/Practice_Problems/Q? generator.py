#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 10:56:38 2019

@author: MASTER
"""
'''
if a procedure has only one yield statement, but that statement 
will never be executed, then the procedure is not a generator.

Explanation:'''
    
def generator1():
    if True:
        yield 1 

def generator2():
    if False:   
        yield 1
    else:
        yield 2

g1 = generator1()
g2 = generator2()

print(type(g1))
print(type(g2))
print(next(g1))
print(next(g2))
print()
'''
If we were to use a generator to iterate over a million numbers,
 how many numbers do we need to store in memory at once?
 Explanation:

We need to store 2 numbers - one for the current value, and one for the max value.'''


def genOneMillion():
    maxNum = 1000000
    current = -1
    while current < maxNum:
        current += 1
        yield current
  
p1 = genOneMillion()      
print(p1.__next__())
print(p1.__next__())
print(p1.__next__())
print()

def genM():
    for i in range(1000000):
        yield i

p2 = genM()      
print(p2.__next__())
print(p2.__next__())