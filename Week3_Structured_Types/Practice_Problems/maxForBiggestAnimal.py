#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 11:38:31 2019

@author: MASTER
"""
#### this exercise its incorrect ITS WRONG!!!!! ANSWER
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'e': ['elephant']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
animals['b'].append('dingo')
animals['b'].append('dingo1')
animals['b'].append('dingo2')


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''

    return max(aDict)

print(biggest(animals))