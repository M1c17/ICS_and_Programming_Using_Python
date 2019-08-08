#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 12:05:15 2019

@author: MASTER
"""

#l3 = list
#l3 = list()
#l3.__class__
#print(dir(l3))
##['__add__','__class__','__contains__','__delattr__','__delitem__','__dir__',
#'__doc__','__eq__','__format__','__ge__','__getattribute__', '__getitem__',
#'__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__',
#'__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__','__new__',
#'__reduce__','__reduce_ex__', '__repr__','__reversed__','__rmul__','__setattr__',
#'__setitem__','__sizeof__','__str__','__subclasshook__','append','clear',
#'copy','count','extend','index','insert','pop','remove','reverse','sort']

class C:
    def __init__(self,deep):
        self.deep = deep
    def f():
        return 'fiftyfive'

print(dir(C))
print(C.__dict__)
print(C.f())
print(C.__dict__['f']())