#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 08:52:10 2019

@author: MASTER
"""

class intSet(list):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""
#initialize inSet directly as a list, or as a list sub-class and it will
# automatically inherit all list type methods
    def __init__(self, *e):
        """Create an empty set of integers"""
        self.extend(e)

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self:
            self.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def intersect(self, other):
        return intSet(*[x for x in self if x in other])

    def __str__(self):
        """Returns a string representation of self"""
        return '{' + ','.join(str(e) for e in sorted(self)) + '}'
    
    
    