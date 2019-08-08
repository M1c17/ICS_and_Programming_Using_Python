#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 12:48:13 2019

@author: MASTER
"""

class Mine():
    def __init__(self,deep):
        self.deep = deep
        
    @property
    def deep(self):
        if self.__deep > 1000:
            return 1000
        return self.__deep
    
    @deep.setter
    def deep(self, deep):
        if deep > 2000:
            self.__deep = 2000
        elif deep <= 0:
            self.__deep = 0
        else:
            self.__deep = deep
            
SilverDollar = Mine(- 400)
print(SilverDollar.deep)
SilverDollar.deep = 1200
print(SilverDollar.deep)
SilverDollar._Mine__deep 
SilverDollar.deep = 5055
print(SilverDollar.deep)
SilverDollar._Mine__deep
    

#class Dunder_demo:
#    def __init__(self, x):
#        self.__x = x
#
#dd = Dunder_demo(55)
#print(dd.__x)