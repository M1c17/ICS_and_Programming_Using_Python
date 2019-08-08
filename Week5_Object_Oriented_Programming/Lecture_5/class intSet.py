#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 09:54:32 2019

@author: MASTER
"""

# build a collection, a set of integer that appears only once inside the set
# representation invariant enforced by the code 
# internal data representation
# use list to store the elements of a set 
# interface
# insert(e)-insert integer e into set if not there
# member(e)-return True if integer e is in set, False else
# remove(e)-remove integer e from set, error if not present 

class intSet(object):
    '''An inSet is a set of int
    The value is represented by the list of ints, self.vals.
    Each int in the set occurs in self.vals exactly one'''
    #internal data representation
    def __init__(self):
        '''Create an empty set of int'''
        self.vals = []
    #interface
    def insert(self, e):  # representation invariant
        '''Assumes e is an integer 
        Returns True if e is in self, and False otherwise'''
        if not e in self.vals:
            self.vals.append(e)
            
    def member(self, e):
        '''Assumes e is int 
        Returns True if e is in self, and False otherwise'''
        return e in self.vals

    def remove(self, e):
        '''Assumes e is an int & removes e from self
        Raises ValueError if e is not in self''' 
        try:
            self.vals.remove(e)
        except: # can use exception to catch attempt to remove nonexistent element
            raise ValueError(str(e) + ' not found')
            
    def __str__(self):
        '''Return a string representation of self'''
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ',' 
        return '{' + result[:-1] + '}'
    
s = intSet()
print(s)
s.insert(3)
s.insert(4)
s.insert(3)
print(s)
print(s.member(6))
print(s.member(3))
s.remove(3)
s.insert(6)
print(s)
s.remove(3)
        
        