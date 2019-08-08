#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 12:37:27 2019

@author: MASTER
"""

# getters & setters
#class P:
#    def __init__(self, x):
#        self.__x = x
#    
#    def get_x(self):
#        return self.__x
#    
#    def set_x(self, x):
#        self.__x = x

  #change the class      
class P:
    def __init__(self, x):
        self.__x = x
    
    def get_x(self):
        return self.__x
    
    def set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
               
p1 = P(42)
p2 = P(4711)
#The attribute x is not available anymore
#p1.__x = 1001
print(p1.get_x())
p1.set_x(47)
p1.set_x(p1.get_x() + p2.get_x())
print(p1.get_x())
# how i can access to my first p1 ????
#print(p1.x)
print(p2.get_x())

