#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 11:05:19 2019

@author: MASTER
"""

list = [(0, 5), (1, 4), (2, 3)]

list2 = [(0, 5), (1, 4, 5), (2, 3)]

sorted(list, key = len)
#[(0, 5), (1, 4), (2, 3)]
sorted(list2, key = len)
#[(0, 5), (2, 3), (1, 4, 5)]
max(list2, key =len)
#(1, 4, 5)
max(list2, key = lambda x:x[1])
# (0, 5)
max(list)
#(2, 3)
max(list, key = len)
# (0, 5)
max(list, key = lambda x: x[1]) #sort by 2nd element 
# (0, 5)
##
#same as
def second_element(x):
    return x[1]

max(list, key = second_element)
