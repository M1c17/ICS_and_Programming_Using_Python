#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 22:50:14 2019

@author: MASTER
"""

s = 'azcbobobegghakl' 
best = tempstr = s[0]


for c in range (len(s)-1):
    if s[c] <= s[c+1]:
        tempstr += s[c+1]
        
        if len(best) < len(tempstr):
            best = tempstr

    else:
        print('tempstr is: ' + str(tempstr))
        tempstr = s[c+1]     
    
print ('current is: ' +  str(tempstr))
print ('Longest substring in alphabetical order is: '+ str(best))