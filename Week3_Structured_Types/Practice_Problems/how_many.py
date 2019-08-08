#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 22:00:41 2019

@author: MASTER
"""
#We want to write some simple procedures that work on dictionaries 
#to return information.

#First, write a procedure, called how_many, which returns the sum 
#of the number of values associated with a dictionary.

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0 
    values = aDict.values()
    for value in values:
    #Since all the values of aDict are lists, aDict.values() will 
    #be a list of lists     
            count += len(value)
    return count 

#animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
#
#animals['d'] = ['donkey']
#animals['d'].append('dog')
#animals['d'].append('dingo')

animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 
           'd': ['donkey', 'dog', 'dingo']}
        
print(how_many(animals))   


##### 

def how_many(aDict):
    '''
    Another way to solve the problem.

    aDict: A dictionary, where all the values are lists.

    returns: int, how many individual values are in the dictionary.
    '''
    result = 0
    for key in aDict.keys():
        result += len(aDict[key])
    return result


animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 
           'd': ['donkey', 'dog', 'dingo']}
        
print(how_many(animals)) 

###
#one liner code
def how_many(aDict):
    return sum(map(len, aDict.values()))

animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 
           'd': ['donkey', 'dog', 'dingo']}
        
print(how_many(animals)) 

###
def how_many(aDict):
    return sum(len(aDict[k]) for k in aDict)

animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 
           'd': ['donkey', 'dog', 'dingo']}
        
print(how_many(animals)) 
