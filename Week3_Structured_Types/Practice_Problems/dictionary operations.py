#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 12:32:40 2019

@author: MASTER
"""

animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}

animals['d'] = 'donkey'
animals
animals['c']
animals['donkey']
len(animals)
animals['a'] = 'anteater'
animals['a']
len(animals['a'])
'baboon' in animals
'donkey' in animals.values()
'b' in animals
animals.keys()
del animals['b']
len(animals)
animals.values()