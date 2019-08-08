#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 14:32:07 2019

@author: MASTER
"""
#that takes in one parameter - a list of letters, lettersGuessed.
# This function returns a string that is comprised of lowercase English
# letters - all lowercase English letters that are not in lettersGuessed.

import string

alphabet_in_lower_case = string.ascii_lowercase

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    ans = ''
    for letter in alphabet_in_lower_case:
        if letter not in lettersGuessed:
            ans += letter
    return ans

    
print(getAvailableLetters(lettersGuessed))

####one line 
def getAvailableLetters(lettersGuessed):
    ans = ''.join([c for c in alphabet_in_lower_case if c not in lettersGuessed ])
    return ans
print(getAvailableLetters(lettersGuessed))


####
def getAvailableLetters(lettersGuessed):
    ans = []
    
    for letter in alphabet_in_lower_case:
        if letter not in lettersGuessed:
            ans.append(letter)
    return ''.join(ans) 
print(getAvailableLetters(lettersGuessed))


###
alpha = list(alphabet_in_lower_case)

def getAvailableLetters(lettersGuessed):
    for letter in lettersGuessed:
        if letter in alpha:
            alpha.remove(letter)
    return ''.join(alpha)
print(getAvailableLetters(lettersGuessed))

###

def getAvailableLetters(lettersGuessed):
    import string

    alphabet_in_lower_case = string.ascii_lowercase
    #alphabetic = 'abcdefghijklmnopqrstuvwxyz'
    for letter in lettersGuessed:
        if letter in alphabet_in_lower_case:
            alphabet_in_lower_case = alphabet_in_lower_case.replace(letter, '')
    return alphabet_in_lower_case
print(getAvailableLetters(lettersGuessed))

###one line
from string import ascii_lowercase

def getAvailableLetters(lettersGuessed):
    return "".join(sorted(set(ascii_lowercase) - set(lettersGuessed)))
print(getAvailableLetters(lettersGuessed))


#### INTERESTING PROBLEM USING DEL & INDEXING

#Problem 3 -

def getAvailableLetters(lettersGuessed):

    import string
    l = list(string.ascii_lowercase)
    for c in lettersGuessed:
        temp = l.index(c)
        del(l[temp])
    return "".join(l)

# Delete any letter that's been guessed
# using list and indexing   