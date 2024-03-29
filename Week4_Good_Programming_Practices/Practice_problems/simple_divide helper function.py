#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 22:15:57 2019

@author: MASTER
"""
#Suppose we rewrite the FancyDivide function to use a helper function.

#This code raises a ZeroDivisionError exception for the following call:
 #   fancy_divide([0, 2, 4], 0)
#Your task is to change the definition of simple_divide so that the call
# does not raise an exception. When dividing by 0, fancy_divide should 
#return a list with all 0 elements. Any other error cases should still 
#raise exceptions. You should only handle the ZeroDivisionError.


def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    try:
        return item /denom
    except ZeroDivisionError:    # 'except' handles the specified error type.
        return 0
        #print("Received ZeroDivisionError in try block")
        

print(fancy_divide([0, 2, 4], 0))

