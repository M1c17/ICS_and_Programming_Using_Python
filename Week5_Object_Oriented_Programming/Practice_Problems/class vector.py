#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 12:22:28 2019

@author: MASTER
"""

#code a simple two dimesional vector class

from math import hypot 

class Vector(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)
    def __abs__(self):
        return hypot(self.x, self.y)
    def __bool__(self):
        #it returns False if the magnitude of the vector is zero, True otherwise
        return bool(abs(self))
    # a faster implementation 
#    def __bool__(self):
#        return bool(self.x or self.y)  
    def __add__(self, other):
        #create and return a new instance of Vector,
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    def __mul__(self, scalar):
        #create and return a new instance of Vector,
        return Vector(self.x * scalar, self.y * scalar)
    
v1 = Vector(3, 4)
v2 = Vector(2, 4)

print(v2.__repr__())
print(v1.__abs__())
print(abs(v1))
print(v1.__bool__())
print(bool(v1))
v3 = v1 + v2
print(v3)
v3 = v1 * 1
print(v3)



        