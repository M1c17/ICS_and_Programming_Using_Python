#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 20:30:23 2019

@author: MASTER
"""

nameHandle = open('kid', 'w')
nameHandle.write('Michael\n')
nameHandle.write('Mark\n')
nameHandle.close()

nameHandle = open('kid', 'r')
for line in nameHandle:
    print(line[:-1])
nameHandle.close()

#open the file for appending 
nameHandle = open('kid', 'a')
nameHandle.write('David\n')
nameHandle.write('Andrea\n')
nameHandle.close()
nameHandle = open('kid', 'r')
for line in nameHandle:
    print(line[:-1])
nameHandle.close()   