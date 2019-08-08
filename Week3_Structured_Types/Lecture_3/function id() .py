#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:24:49 2019

@author: MASTER
"""

cList = [6, 5, 4, 3, 2]
dList = []
for num in cList:
    dList.append(num)

print('cList has object id =', id(cList), 'and contains', cList)
print('dList has object id =', id(dList), 'and contains', dList)

print("'cList == dList' yields the result", cList==dList)
print("'cList is dList' yields the result", cList is dList)