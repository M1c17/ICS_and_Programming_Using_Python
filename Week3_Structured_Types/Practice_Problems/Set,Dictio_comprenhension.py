#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 18:58:54 2019

@author: MASTER
"""
#SET COMPREHENSION & DICTIONARY COMPREHENSION 

# create a set of all the first letters in a sequence of words
words = ['apple', 'banana', 'cauliflower']
first_letters = set()
for w in words:
    first_letters.add (w[-1])
print(first_letters)
### set comprehension 
    
first_letter = {w[0] for w in words}
print(first_letters)

#code that makes a a new dictionary 
#by swapping the keys and values of the original one
original = {1:'a', 2:'b', 3:'c'}
flipped = {}
for key, value in original.items():
    flipped[value] = key 
print(flipped)


#listcomprenhension 
original = {1:'a', 2:'b', 3:'c'}
flipped = {value: key for key, value in original.items()}
print(flipped) 

