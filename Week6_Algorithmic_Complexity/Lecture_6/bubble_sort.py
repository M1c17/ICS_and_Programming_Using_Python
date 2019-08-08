#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 14:51:41 2019

@author: MASTER
"""

#COMPLEXITY OF BUBBLE SORT 

def bubble_sort(L):
    swap = False
    while not swap: #outer while loop is for doing multiple passes #O(len(L))
        swap = True #until no more swap
        
        for j in range(1, len(L)): #inner for loop is for doing comparisons #O(len(L))
            print(L)
            if L[j - 1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j - 1]
                L[j - 1] = temp
        
                
#O(n^2) where n is len(L)
# TO DO O(len(L)-1) comparisons and O(len(L)-1)passes
L = [9,4,3,7,1,0]
test = [1,5,3,8,4,9,6,2]
print(bubble_sort(test))



