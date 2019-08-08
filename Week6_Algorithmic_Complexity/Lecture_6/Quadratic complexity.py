#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 09:43:26 2019

@author: MASTER
"""

#QUADRATIC COMPLEXITY

def isSubset(L1, L2):
    for e1 in L1:            
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True

L1 = [1,4,5]
L2 = [4,5,7,8]      
p1 = isSubset(L1, L2)
print(p1)
#O(len(L1)*(L2)
#worst case when L1 & L2 same length 
#O((len)^2)
#the fact that we might break out of the loop earlier doesnt change the 
#orden growth of the algorithm 


'''write a code when you need to find the intersection in two List, 
return a List when the elements appearing only once'''

def intersection(L1, L2):
    temp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                temp.append(e1)               
#clean the repetition in the List
    res = []
    for e in temp:
        if e not in res:
            res.append(e)
    return res
L1 = [1,4,5,6]
L2 = [4,5,7,8]      
p2 = intersection(L1, L2)
print(p2)

#when dealing with nested loop look at the ranges 

def g(n):
    '''assume n >=0'''
    x = 0
    for i in range(n):
        for j in range(n):
            x +=1
    return x