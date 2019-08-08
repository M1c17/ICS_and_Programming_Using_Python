#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:45:18 2019

@author: MASTER
"""

def f():
    a = 55
    def g():
        global a
        print(f'a is {a}')
    g()
f()
###
def f():
    a = 55
    def g():
        nonlocal a
        print(f'a is {a}')
    g()
f()

####

t = 66

def cc():
    s = 55
    def test():
        y = s + 4 
        w = t + 6
        print(y,w)
    test()
cc()
    