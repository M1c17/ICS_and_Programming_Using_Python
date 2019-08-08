#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 13:55:47 2019

@author: MASTER
"""

aList = [0, 1, 2, 3, 4, 5]
bList = aList
aList[2] = 'hello'
aList == bList
aList is bList

cList = [6, 5, 4, 3, 2]
dList = []
for num in cList:
    dList.append(num)
cList == dList
cList is dList
cList[2] = 20
cList
dList
