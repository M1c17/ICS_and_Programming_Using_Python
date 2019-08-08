#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 22:42:26 2019

@author: MASTER
"""

#one line (Elizabeth)
s = 'azcbobobegghaklbob'
print('Number of times bob occurs is:', len([index for index in range(len(s))\
                                             if s[index: index+3] == 'bob']))