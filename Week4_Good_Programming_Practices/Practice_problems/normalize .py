#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 13:28:45 2019

@author: MASTER
"""

def normalize(numbers):
    max_number = max(numbers)
    for i in range(len(numbers)):
        numbers[i] /= float(max_number)
    return numbers

try:
      normalize([0, 0, 0])
except ZeroDivisionError:
      print('Invalid maximum element')
      
#Does the try block throw (also known as raise) an exception?
#Yes
#What is the name of the exception the code is trying to catch?
#ZeroDivisionError
#What is the output?
#Invalid maximum element
#Since we are dividing by the maximum element in a list of positive numbers,
# we know that normalize will return a value between 0 and 1. What type of 
#condition is this?
# post condition
#We also know the result is not meaningful when the maximum element is 0, 
#so we want to ensure that the numbers in the list do not violate this.
# What type of condition is this?
# pre condition

#Now assume the definition of the function normalize is rewritten as follows

def normalize(numbers):
    max_number = max(numbers)
    assert(max_number != 0), "Cannot divide by 0"
    for i in range(len(numbers)):
        numbers[i]  /= float(max_number)
        assert(0.0 <= numbers[i] <= 1.0), "output not between 0 and 1"
    return numbers

normalize([0, 0, 0])

#Which condition does the line assert(max_number != 0) correspond to?
# pre condition
#
#Which condition does the line assert(0.0 <= numbers[i] <= 1.0) correspond to?
#post condition
#What does the function call normalize([0, 0, 0]) print out?
#AssertionError: Cannot divide by 0