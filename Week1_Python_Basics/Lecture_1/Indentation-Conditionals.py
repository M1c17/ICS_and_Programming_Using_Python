#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lecture 1:
Video: Operators and Branching programs.
Indentantion - Conditionals.
= vs ==.

"""

x = float (input("enter a number for x: "))
y = float (input("enter a number for y: "))
if x == y:
    print ("x and y are equal")
    if y != 0:
        print ("therefore, x / y is", x/y)
elif x < y:
    print ("x is smaller")
else:
    print ("y is smaller")
print ("thanks!!")