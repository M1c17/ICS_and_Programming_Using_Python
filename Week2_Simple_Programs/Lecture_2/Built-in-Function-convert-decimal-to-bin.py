#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 11:30:17 2018

@author: MASTER
"""


#ways to do decimal-binary conversions using Python's built-in functions like so:
    
x = "10001" 
c = int(x, 2)

print(c)

x = 11 
c = (bin(x).replace("0b", ""))

print(c)

x = 0.5 
c = (bin(int(x)).replace("0b", ""))

print(c)