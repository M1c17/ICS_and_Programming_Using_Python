#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 16:27:13 2019

@author: MASTER
"""

class Iterable(object):
    def __init__(self, x):
        self.x = x
    def __iter__(self):
        return self.__next__()
    def __next__(self):
        for i in self.vals:
            yield  i 
            
x = Iterable([1,2,3])
print(x.__iter__())
#<generator object Iterable.__next__ at 0x10e48e6d0>
print(x.__next__())
#<generator object Iterable.__next__ at 0x10d99a048>

class Iterable(object):
    def __init__(self, x):
        self.x = x
    def __iter__(self):
        for i in self.vals:
            yield  i 
            
x = Iterable([1,2,3])
print(x.__iter__())
#<generator object Iterable.__iter__ at 0x10e4a1af0>

class Iterable(object):
    def __init__(self, x):
        self.x = x
    def __iter__(self):
        return self

    def __next__(self):
        for i in self.vals:
            yield i 
            
x = Iterable([1,2,3])
print(x.__iter__())

class Iterable(object):
    def __init__(self, x):
        self.x = x

    def __iter__(self):
        return iter(self.vals)
    
x = Iterable([1,2,3])
#print(x.__iter__())


'''
  def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.vals.pop(0)
        except IndexError:
            raise StopIteration '''