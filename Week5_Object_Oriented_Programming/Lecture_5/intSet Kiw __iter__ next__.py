#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 10:11:28 2019

@author: MASTER
"""

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __iter__(self):
        return self

    def __next__(self):
        try:
            try:
                self.__i += 1
            except AttributeError:
                self.__i = 0
            return self.vals[self.__i]
            # return self.vals.pop(0)
        except IndexError:
            del self.__i
            raise StopIteration

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

ii = intSet()
for i in range(7): ii.insert(i)
print(ii)
print(next(ii))
print(next(ii))
print()
for i in ii: print(i, end=', ')
print('\ntry again')
print(ii)
for i in ii: print(i, end=', ')
print('\nrestart')
ii = intSet()
for i in range(7): ii.insert(i)
for i in ii: print(i, end=', ')