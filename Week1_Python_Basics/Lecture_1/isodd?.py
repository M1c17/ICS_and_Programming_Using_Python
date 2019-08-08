#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ask the user to input a integer.
and then print the largest odd number that was entered 
if no odd number was entered,it should be print a message to that effect

"""

largestodd = 0

for nums in range(10):
    nums = int(input('Enter a num: '))
    if nums % 2 == 1 and nums > largestodd:
        largestodd = nums
        
if largestodd:
    print('the largestodd is:', largestodd)
        
else :
    print('there were no largest odd') 