#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 20:45:14 2019

@author: MASTER
"""

class Weird(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return x 
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

X = 7
Y = 8
w1 = Weird(X, Y)
#print(w1.getX()) # error
#print(w1.getY()) # error
w2 = Wild(X, Y)
print(w2.getX()) #7 
print(w2.getY()) #8
w3 = Wild(17, 18)
print(w3.getX()) #17
print(w3.getY()) #18
w4 = Wild(X, 18)
print(w4.getX()) #7
print(w4.getY()) #18
X = w4.getX() + w3.getX() + w2.getX() 
print(X) # 31
print(w4.getX()) #7
Y = w4.getY() + w3.getY() 
Y = Y + w2.getY() 
print(Y) #44
print(w2.getY()) #8