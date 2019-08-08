#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 21:44:41 2019

@author: MASTER
"""


class C:
    def __init__(self, i, t, l):
        print('before bindings')
        print(i, type(i), id(i))
        print(t, type(t), id(t))
        print(l, type(l), id(l))
        i = 1678
        t = (1,2,3)
        l[:] = [1,2,4,5]  # assign to a slice
        print('after bindings')
        print(i, type(i), id(i))
        print(t, type(t), id(t))
        print(l, type(l), id(l))
    def assign_to_list(self):
        l = [1,2,5]
        print('in class, binding to list change object?')
        print(l, type(l), id(l))
 
i, t, l = 1678, (1,2,3), [1,2,3]
print(i, type(i), id(i))
print(t, type(t), id(t))
print(l, type(l), id(l))
print('now initialize class')
c = C(i, t, l)
print("what's in them now")
print(i, type(i), id(i))
print(t, type(t), id(t))
print(l, type(l), id(l))
c.assign_to_list()
print("what's in l after assign in class")
print(l, type(l), id(l))