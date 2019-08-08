#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 18:01:32 2019

@author: MASTER
"""
def timesFive(a):
    return a * 5

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
testList = [1, -4, 8, -9]
applyToEach(testList, timesFive)
print(testList)

#####
def plusOne(a):
    return a + 1


def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
testList = [1, -4, 8, -9]
applyToEach(testList, plusOne)
print(testList)
#####

def Timesitself(a):
    return a * a

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
testList = [1, -4, 8, -9]
applyToEach(testList, Timesitself)
print(testList)