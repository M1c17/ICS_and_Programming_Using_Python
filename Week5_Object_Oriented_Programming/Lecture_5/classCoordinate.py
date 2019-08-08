#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 13:25:38 2019

@author: MASTER
"""

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y =y
    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2 #think of other.x as saying,
                                        #get the value of other. it point to a frame 
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"
    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)
    
c = Coordinate(3, 4)
origin = Coordinate(0,0)
print(c.x)
print(origin.x)
print(c.distance(origin))
print(Coordinate.distance(c, origin))
print(c)
print(type(c))
print(Coordinate, type(Coordinate))
print(isinstance(c, Coordinate))
foo = c - origin
print(foo)