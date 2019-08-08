#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 16:36:32 2019

@author: MASTER
"""

#when no key is provided, sort uses exclusively the < operator

class A:
    def __init__(self,a):
        self.a = a
    def __lt__(self,other):
        return self.a < other.a

    def __repr__(self):
        return str(self.a)

lst = [A(12),A(10),A(44)]
print(sorted(lst))

#sort used the defined __lt__ (less than) operator internally, only,
# not equal not superior. Sorting is only performed with < operator