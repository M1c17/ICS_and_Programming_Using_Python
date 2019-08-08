#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 16:35:47 2019

@author: MASTER
"""

# ODDTUPLES
# Write a procedure called oddTuples, which takes a tuple as input, 
#and returns a new tuple as output, where every other element of the 
#input tuple is copied, starting with the first one. So if test is the 
#tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on 
#this input would return the tuple ('I', 'a', 'tuple')

def oddTuples(*aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    
    newTuple = ()
    for i, a in enumerate(aTup):
        if (i+1) % 2 == 1:
            newTuple += (a,)
    return newTuple
        
print(oddTuples('I', 'am', 'a', 'test', 'tuple')) 

####
def oddTuples(*aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    
    newTuple = ()
    for i, a in enumerate(aTup):
        if (i+1) % 2 == 1:
            newTuple += (a,)
    return newTuple
        
print(oddTuples('I', 'have', 2, 'medals', 'and', 1, 'Toy')) 

###
def oddTuples(*aTup):
    t = aTup[0: :2]
    return t
print(oddTuples('I', 'am', 'a', 'test', 'tuple'))

###EXERCISES FOR THE GRADER 

def oddTuples(aTup):
    nT = ()
    index = 0 
    while len(aTup) > index:
        nT += (aTup[index],)
        index += 2
    return nT

print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))

##3

def oddTuples(aTup):
    return aTup[::2]
print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))


