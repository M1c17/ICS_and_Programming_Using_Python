#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 11:28:21 2019

@author: MASTER
"""

#map & filter

my_list = [5, 6, 17, 11]

[x if x < 10 else x * 2 for x in my_list]

[x for x in my_list if x % 2]