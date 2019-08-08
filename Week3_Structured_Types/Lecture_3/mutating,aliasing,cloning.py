#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 11:39:51 2019

@author: MASTER
"""

# write a code to remove duplicates from two lists

L1 = [1,2,3,4]
L2 = [1,2,3,4]
def remove_dup(L1, L2):
    for e in L1:
        if e in L2:
            L1.remove(e)
    print(L1, L2)
    return L1 
    
L1 = [1,2,3,4]
L2 = [1,2,3,4]    
print(remove_dup(L1, L2))

# clone list first 
# by making a copy, by cloning the list first 
# now when im mutating L1, I've still got something that im iterating over 
# that hasnt change beacuse its pointing to different structure

def remove_dup_new(L1, L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)
    print(L1, L2)
    return L1
    
print(remove_dup_new([1,2,3,4],[1,2,3,4]))
        
