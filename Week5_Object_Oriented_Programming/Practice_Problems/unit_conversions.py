#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 10:36:32 2019

@author: MASTER
"""
class Length:
    
    __metric = {"mm" : 0.001, "cm" : 0.01, "m" : 1, "km" : 1000,
                "in" : 0.0254, "ft" : 0.3048, "yd" : 0.9144,
                "mi" : 1609.344 }
    
    def __init__(self, value, unit = "m"):
        self.value = value
        self.unit = unit
        
    def Converse2Metres(self):
        return self.value * Length.__metric[self.unit]
    #read first self then other 
    def __add__(self, other):
        if type(other) == int or type(other) == float:
            l = self.Converse2Metres() + other
        else:
            l = self.Converse2Metres() + other.Converse2Metres()
            
        return Length(l / Length.__metric[self.unit], self.unit)
    
    def __iadd__(self, other):
        if type(other) == int or type(other) == float:
            l = self.Converse2Metres() + other
        else:
            l = self.Converse2Metres() + other.Converse2Metres()
            
        self.value = l / Length.__metric[self.unit]
        return self
    #reverse of add read first other then self 
    def __radd__(self, other):
        return Length.__add__(self,other)
    
    def __str__(self):
        return str(self.Converse2Metres())
    
    def __repr__(self):
        return "Length (" + str(self.value) + ",'" + self.unit + "')"

    
if __name__ == '__main__':
    x = Length(4)
    print(x)
    y = eval(repr(x))
    
    z = Length(4.5, "yd") + Length(1)
    print(repr(z))
    print(z)
    
    #method __add__
    x = Length(3, "yd") + 5
    print(x)
    #method __radd__
    x = 5 + Length(3, "yd")
    print(x)

    
    
