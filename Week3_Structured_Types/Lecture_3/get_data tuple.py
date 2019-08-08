#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 09:51:49 2019

@author: MASTER
"""

#Give a tuple to a givedata
#that its going to ilself consist in tuples
# each element inside that tuple is itself a collection of things 
#nums & string

# i want to get the number out so im going indexing then add it into nums
# if the word part its not inside things i've already gathered together 
# gethering up the unique words as well as all the int 
#return the smallest the largest number and the numer the unique words that
# i've found 

def get_data(*aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    print(nums)
    print(words)
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    
    return (min_nums, max_nums, unique_words)

print(get_data((1, 'mine'),(3, 'yours'),(5,'ours'),(7, 'mine')))
  
