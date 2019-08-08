#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 22:24:08 2019

@author: MASTER
"""
#make a list of two numbers get a ratio of those lists
#that is each list i'm going assume is equal length 
# im going to get the ratio of the first element of the first list 
# the first element of the second list and so on 

def get_ratios(L1, L2):
    '''Assumes: L1 & L2 are lists of equal length of numbers 
        Returns: a list containing L1[i]/L2[i]'''
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/float(L2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN')) #NaN = Not a Number
        except:
            raise ValueError('get_ratios called with bad arg')
    return ratios

L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8] 

get_ratios(L1,L2) 

L3 = [5, 6, 7] 

get_ratios(L1,L3)  

L4 = [5, 6, 7, 0] 

get_ratios(L1,L4)   