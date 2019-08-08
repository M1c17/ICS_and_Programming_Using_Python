#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lets s be a string that contains a sequence of decimal numbers
separeted by , e.g. = '1.23,2.4,3.123'. 
write a program that prints the sum of the number in s.
floating point values cannot have comma.
first split the string based in comma.

"""
s ='1.23,2.4,3.123'
print(s.split(','))
#convert each and every element of that list to float 
#add them together 
total = sum(map(float, s.split(',')))
print(total)