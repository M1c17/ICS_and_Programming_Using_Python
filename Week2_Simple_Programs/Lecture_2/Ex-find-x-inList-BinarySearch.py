#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 20:10:15 2019

@author: MASTER
"""
# Find x in list

def binary_search(x, search_list):
    
    iteration = 1
    left = 0 
    rigth = len(search_list)-1
    mid = (left + rigth)//2

    while left <= rigth :
        
        if x == search_list[mid]:
            return mid
        
        elif x > search_list[mid]:
            left = mid + 1
            
        else:
            right = mid - 1
            
        mid = (left + right)//2
        iteration += 1
        
    print('iteration: ' , iteration)
    return mid 

print(binary_search(1, [4, 8, 9, 10, 24, 32, 45, 56]))