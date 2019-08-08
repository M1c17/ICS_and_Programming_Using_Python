#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 16:49:29 2019

@author: MASTER
"""

while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError:
        print('Input not an integer: try again')
print('Correct input of an integer')
        