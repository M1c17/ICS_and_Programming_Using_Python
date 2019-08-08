#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 09:07:49 2019

@author: MASTER
"""
#We want to write some simple procedures that work on dictionaries 
#to return information.

#This time, write a procedure, called biggest, which returns the key
# corresponding to the entry with the largest number of values associated
# with it. If there is more than one such entry, return any one of the
# matching keys
 
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = None
    biggest_value = 0
    for k in aDict.keys():
        if len(aDict[k]) >= biggest_value:
            result = k
            biggest_value = len(aDict[k])
    return result 
        
print(biggest(animals))        
        
##

def biggest(aDict):
    biggest_key = 0
    temp = 0
    for key, values in aDict.items():
        if len(values) > temp:
            temp = len(values)
            biggest_key = key
    return biggest_key
print(biggest(animals))

###

aDict_len ={}
def biggest(aDict):
    for k in aDict:
        aDict_len[k] = len(aDict[k])
    return max(aDict_len, key = lambda k: aDict_len[k])

print(biggest(animals))


### one line 
def biggest(aDict):
    return max(aDict.items(), key = lambda x: len(x[1]))[0]
print(biggest(animals))

###
def biggest(aDict):
     return max((len(v), k) for k, v in aDict.items())[1]
print(biggest(animals))
###
def biggest(aDict):
    return max(aDict.keys(), key = lambda x: len(aDict[x]))
print(biggest(animals))

##The max() function takes a list of items to compare followed by an 
#optional function used to make the comparison. In this case, aDict.keys()
# is the list of items we want to compare... and we need to compare them 
#by the length of their corresponding dictionary value. Use an anonymous 
#function via keyword lambda to measure the length of the dictionary value
# given a key