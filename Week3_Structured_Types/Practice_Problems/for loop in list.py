#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 12:17:13 2019

@author: MASTER
"""

ls = [1,2,3,4]

for e in ls:
    print(e)
    ls.pop(0)
print(ls)
'''
ls = [1,2,3,4]

for i in range(len(ls)):
    print(ls[i])
    ls.pop(0)
print(ls)
'''
ls = [1,2,3,4]

for i in range(len(ls)-2):
    print(ls[i])
    ls.pop(0)
print(ls)
    