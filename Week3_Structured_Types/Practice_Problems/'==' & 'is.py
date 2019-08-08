#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:15:59 2019

@author: MASTER
"""

varA = [1, 2, 3, 4]
varB = [1, 2, 3, 4]
varC = varA
varA == varB    #(True)
varA == varC    #(True)
varA is varB    #(False)
varA is varC    #(True)


l = [1, 2, ['internal list']]
l1 = l[:]

print(l == l1, l is l1, id(l), id(l1))

print(l[2] == l1[2], l[2] is l1[2], id(l[2]), id(l1[2]))







