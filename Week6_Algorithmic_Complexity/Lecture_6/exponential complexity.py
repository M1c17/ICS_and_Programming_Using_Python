#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 10:48:08 2019

@author: MASTER
"""

#EXPONENTIAL COMPLEXITY 
'''times include time to solve the smaller probem plus time needed
to make a copy of all elements in smaller problem'''

'''write a code to count all the possible combinations subsets of n-element
 set'''

def genSubset(L):
    '''what's the size of smaller?
     make every possible subset of this set.'''
    if len(L) == 0:
        return [[]] #list of empty list 
    
    smaller = genSubset(L[:-1]) #all subset without the last element 
    extra = L[-1:] # create a List with just the last element
    new = []
    
    for small in smaller:
        new.append(small + extra) #for all smaller solutions, 
                                    #add one with last element 
    return smaller + new  #combine those with last element and those whitout
  
L = [1,2,3]
p1 = genSubset(L)
print(p1)

#Each step is built by creating copy of element from all previous steps with
# appended in new element.

#W can see that if we have 1 element then there are 2 possible subsets which
# i will denote as 1e -> 2s, going further we have: 
#2e -> 4s, 3e -> 8s, 4e -> 16s. It starts to be visible that number of those
# subsets can be seen as  where n is number of elements in our list L.

#There are literally  possible subsets and we assume that each append operation
# creates one of them without any repetitions

#denotes depth of recursive call, 0 is the first call. Each step is built by
# creating copy of element from all previous steps with appended new element.
 
