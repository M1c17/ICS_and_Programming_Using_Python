#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 22:25:56 2019

@author: MASTER
"""

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[i]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

#1 given a list dive into half size and sort 
def merge_sort(L):
    '''
    at first recursion level
    n/2 elements in each list
    O(n) + O(n) = O(n) where n is len(L)
    at second recursion level
    n/4 elements in each list
    two merges - O(n) where n is len(L)
    Each recursion level is O(n) where n is len(L)
    dividin list in half with each recursive call 
    O(log(n)) where n is len(L)
    overall complexity is O(n log(n) where n is len(L))
    '''
    if len(L) < 2:  #base case 
        return L[:]
    else:
        middle = len(L)//2 #divide list into half 
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)  #conquer with the merge step 

    
    
            
    