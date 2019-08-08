#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 12:33:18 2019

@author: MASTER
"""

def swapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)
    
L = [1, 9, 0, 3, 5]
l2 = [2, 5, 6, 9, 0]

test1 = swapSort(L)
test2 = swapSort(l2)
print(test1)
print(test2)

def modSwapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)
    
L = [1, 9, 0, 3, 5]

test1 = modSwapSort(L)
test2 = modSwapSort(l2)
print(test1)
print(test2)
    