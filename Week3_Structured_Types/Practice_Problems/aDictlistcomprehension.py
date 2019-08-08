#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 10:01:32 2019

@author: MASTER
"""

#list comprehension

aDict ={1: [1,2,3], 2: [2], 3:[4]}
[(v, k) for k, v in aDict.items()]
#[([1, 2, 3], 1), ([2], 2), ([4], 3)]
[(len(v), k) for k, v in aDict.items ()]
#[(3, 1), (1, 2), (1, 3)]
max ([(len(v), k) for k, v in aDict.items ()])[0]
#3
max ([(len(v), k) for k, v in aDict.items ()])[1]
#1
#but, u dont need which initiate the list,as the generator expression 
#form can be evaluated by the function max so this is enough 

max ((len(v), k) for k, v in aDict.items ())[1]

