#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 20:02:07 2019

@author: MASTER
"""

#List are iterable
# Compute the sum of elements of a list 
L=[3,5,6,8,90,34]
total = 0
for i in range(len(L)):
    total +=L[i]
print(total)

#much cleaner is to recognize that i can simply iterate over the elements 
#of the list themselves

total = 0

for i in L:
    total += i
print(total)


