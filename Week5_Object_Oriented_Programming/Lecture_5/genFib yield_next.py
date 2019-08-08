#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 19:47:29 2019

@author: MASTER
"""        
def genTest():
    yield 1
    yield 2
    
foo = genTest()
print(foo.__next__())
#1 
#Execution will proceed in body of foo, until reaches first yield statement;
#then returns value associated with that statement 
print(foo.__next__())
#print(foo.__next__())
#execution will resumen in boby of foo at point where stopped, until reaches
#yield statement; then return value associated with that statement

for n in genTest():
    print(n)
    
    
def genFib():
    fibn_1 = 1 #fib(n-1)
    fibn_2 = 0 #fib(n-2)
    while True:
        #fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next
        
fib = genFib()
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())

#for n in genFib():
#    print(n)
# it will print a infinite sequence