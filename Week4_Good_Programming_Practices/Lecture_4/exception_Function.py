#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 12:49:25 2019

@author: MASTER
"""

def f():
    try:
        x = int("four")
    except ValueError as e:
        print("got it in the function", e)

try:
    f()
except ValueError as e:
        print("got it outside the function", e)
        
print("Let's get on")

