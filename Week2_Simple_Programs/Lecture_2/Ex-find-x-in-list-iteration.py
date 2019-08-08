#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 09:37:26 2019

@author: MASTER
"""

# Find x in list

def linearsearch(x, search_list):
    """
    Return the index of the x if found in search_list
    Else return -1
    """
    iteration = 0
    idx = 0 
    while idx < len(search_list):
        iteration += 1
        if x == search_list[idx]:
            print('iterations= ' + str(iteration))
            return idx
        idx += 1 
    return - 1
print(linearsearch(32, [4, 8, 45, 24, 10, 32, 9, 56])




        
        
        
        
        
        
        
        
        
        