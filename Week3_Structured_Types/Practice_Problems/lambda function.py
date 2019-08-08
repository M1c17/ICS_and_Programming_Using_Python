#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 10:26:35 2019

@author: MASTER
"""
## lambda function
animals ={'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo']}

def biggest(aDict):
    return max(aDict.keys(), key = lambda x: len(aDict[x]))
print(biggest(animals))

##The max() function takes a list of items to compare followed by an 
#optional function used to make the comparison. In this case, aDict.keys()
# is the list of items we want to compare... and we need to compare them 
#by the length of their corresponding dictionary value. Use an anonymous 
#function via keyword lambda to measure the length of the dictionary value
# given a key

'''anonymous functions, they are functions defined inline with their use
 case. For clarity, the above could be re-written as follows:
def len_list(key):
    return len(aDict[key])

return max(aDict.keys(), key=len_list)'''



