#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 10:50:43 2019

@author: MASTER
"""

#IMPLEMENTATION OF BISECTITION SEARCH
#complexity Analysis - recursive

def bisect_search(L, e):
    if L == []:
        return False  #O(1)
    elif len(L) == 1:
        return L[0] == e  #O(1)
    else:
        half = len(L)//2   #O(1)
        if L[half] > e:
            return bisect_search(L[:half], e) 
        else:
            return bisect_search(L[half:], e)
        
testList1 = bisect_search([1,4,5], 4)
print(testList1)

'''
implementation 1 - bisection search 1 
- O(log n) bisection search calls
- O(n) for each bisection search call to copy list 
- O(n log n) 
'''      
        
#ANOTHER WAY 
#KEEP THE LIST BUT JUST KEEP TRACK WHERE I'M LOOKING AT 

def bisect_search2(L, e):
    def bisect_search_helper(L, e, Low, high):
        if high == low:
            return L(low) == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: #nothing left to search
                return False
            else:
                return bisect_search_helper(L, e, Low, mid, -1)
        else:
            return bisect_search_helper(L, e, mid, +1, high)
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L), -1)

testList2 = bisect_search([1,4,5], 4)
print(testList2)    
'''
implementation 2 - bisection search and its helper 
- pass list and indices as parameters
- list never copied, just re- passed 
- O(log n)
This solution is much better than the first solution

'''