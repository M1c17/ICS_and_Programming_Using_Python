#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 11:49:43 2019

@author: MASTER
"""

class Coordinate (object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x
    def getY(self):

        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __repr__(self):  
        return 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')'

c = Coordinate(2, -8)
origin = Coordinate(0, 0)
print(c)
print(origin.__repr__())