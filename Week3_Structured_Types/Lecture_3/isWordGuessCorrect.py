#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 12:07:39 2019

@author: MASTER
"""

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#lettersGuessed = ["a", "p", "l", "e"]
#lettersGuessed = ["a", "p", "l", "e", "p"]

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
        
        return True
               
print(isWordGuessed(secretWord, lettersGuessed))

###one line 
secretWord = 'apple'
lettersGuessed = ["a", "p", "l", "e", "p"]
def isWordGuessed(secretWord, lettersGuessed):
    
    return set(secretWord).issubset(lettersGuessed)

print(isWordGuessed(secretWord, lettersGuessed))