#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 11:22:28 2019

@author: MASTER
"""

#Exercise:Coordinate

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        print(type(self).__name__)
        #print(type(self).__dict__)
        return self.x
        
    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    
    def __eq__(self, other):
        #First make sure other is the same type 
        assert type(other) == type(self)
        #Since other is the same type, test if coordinate are equals
        #returns True if coordinates refer to same point in the plane
        return self.getX() == other.getX() and self.getY() == other.getY()
    
    def __repr__(self):
        #return str that looks like a valid Python expression
        #eval(repr(c)) == c
        #that could be used to recreate an object with the same value
        #given the definition of __eq__
        return 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')'
    
#   def __repr__(self):
#        return "Coordinate({},{})".format(self.getX(), self.getY())  

      
c = Coordinate(3, 4)
print(type(c).__name__)
origin = Coordinate(3, 6)
print(c.getX())
print(c.x)
print(c)
print(c.__eq__(origin))
print(origin.__eq__(origin))
print(c.__repr__())
print(origin.__repr__())
Coordinate.__dict__.keys()
#my mistakes dont use getY and getX
#idk the use of assert 
#        return self.x == other.x:
#          
        