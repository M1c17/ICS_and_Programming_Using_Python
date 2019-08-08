#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 17:59:49 2019

@author: MASTER
"""


#secretword is gonna be choosen by a random method 
#letters guessed: all the letters the user has guessed 
#if all of the letter in secretword are in letterguessed 
#the user guessed the word return True 
#otherwise if the letter in secretword isnt in the word the letterguessed 
# return False 
#lettersGuessed is a list of whats letter having guessed so far 
#function hangman(secret word)

#1) go walkdown all letter in secretword 
#if there in letterguessed

secretWord = 'apple'
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
lettersGuessed = ["a", "p", "l", "e"]

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


###
secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
def isWordGuessed(secretWord, lettersGuessed):
    L = []
    for x in lettersGuessed:
        if x in secretWord:
            L += x
    return set(L) == set(secretWord)
print(isWordGuessed(secretWord, lettersGuessed))

###one line 
secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
def isWordGuessed(secretWord, lettersGuessed):
    return set(secretWord).issubset(lettersGuessed)
print(isWordGuessed(secretWord, lettersGuessed))

####
def isWordGuessed(secretWord, lettersGuessed):
    
    if list(secretWord) == lettersGuessed:
        return True
    return False 

####
secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
def isWordGuessed(secretWord, lettersGuessed):
    return all(c in lettersGuessed for c in secretWord)
print(isWordGuessed(secretWord, lettersGuessed))

###
secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
def isWordGuessed(secretWord, lettersGuessed):
    return not(set(secretWord) - set(lettersGuessed))
print(isWordGuessed(secretWord, lettersGuessed))


