#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 17:04:13 2019

@author: MASTER
"""

# Open a file
fo = open("foo.txt", "wb")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)
#print ("Softspace flag : ", fo.softspace)

import os 
os.mkdir("test")

import os
os.getcwd()