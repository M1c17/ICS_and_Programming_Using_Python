#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 08:54:07 2019

@author: MASTER
"""

 
# 1.what are the data attributes i want to glue together 
# define internal representation - two int = numerator - denominator
# 2.whats the interface
# the method that im going to use to interact with instances of those fraction objects?
# - print representation 
# - add, substract
# - convert to a float - then i can use standart Py arithmetic operations on 
#
#Create something that lets me access data attributes = getters 
#now i can create add, subtract 

#INITIAL FRACTION CLASS
# create a new object to represent a number as a fraction

class fraction(object):
#internal representation
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
#interface
    def __str__(self):
        return str(self.numer) + '/' + str(self.denom)
    def getNumer(self):
        return self.numer
    def getDenom(self):
        return self.denom
#create a new instance 
    def __add__(self, other):
        numerNew = other.getDenom() * self.getNumer() \
                   + other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom() 
        return fraction(numerNew, denomNew)
    def __sub__(self, other):
        numerNew = other.getDenom() * self.getNumer() \
                   - other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew)
    def convert(self):
        return self.getNumer() / self.getDenom()
    

oneHalf = fraction(1, 2)
twoThirds = fraction(2, 3)
print(oneHalf) 
print(twoThirds)      
print(oneHalf.getNumer())
new = oneHalf + twoThirds
print(new)
new = oneHalf - twoThirds
print(new)
threeQuarters = fraction(3, 4)
print(threeQuarters)
secondNew = twoThirds - threeQuarters
print(secondNew)
print(secondNew.convert())


