#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 13:03:50 2019

@author: MASTER
"""

#write a code that take a str and return a reverse str

def revers_str(my_str):
    
    for l in range(len(my_str) -1,-1,-1):
        yield my_str[l] 
        
p1 = revers_str('hello')
print(p1.__next__())

for i in revers_str('hello'):
    print(i)
    
def revers_str(my_str):
    word = ''
    for l in range(len(my_str) -1,-1,-1):
        word += my_str[l]
    return word 
        
p2 = revers_str('hello')
print(p2)