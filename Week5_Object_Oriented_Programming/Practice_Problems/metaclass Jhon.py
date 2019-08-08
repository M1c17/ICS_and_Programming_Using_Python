#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 11:08:17 2019

@author: MASTER
"""

#metaclass
class Jhon:
    def __init__(self):
        self.a = 5
        self.b = 6
    def fn(self, x, y):
        return x + y
    
print(Jhon.__class__)
Fred = type("Fred", (), {"a": 5, "b": 6, "fn": lambda self, x,y: x+y})
print(Fred.__class__)