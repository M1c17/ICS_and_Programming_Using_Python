#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 19:40:48 2019

@author: MASTER
"""

class Dunder_demo:
    def __init__(self, _x=0):
        self.x = 2
        self._x = 3
        self.__x = 4
        self.__x__ = 5

d = Dunder_demo(5)    
print(d)