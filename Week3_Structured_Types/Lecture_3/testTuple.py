#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 12:21:20 2019

@author: MASTER
"""

def testTuple(red, yellow):
    """
        take in two parameters-- red, yellow -- of any type
        and return a tuple to assign to two variables
    """
    blue = red
    purple = yellow
    print(blue + str(purple))
    color = ()

    color = color + (blue,)
    print(color)
    color = color + (purple,)
    print(color)

    return (color)

pink = 'black'
sienna = 3
orange, green = testTuple(pink, sienna)

print(orange)
print(green)