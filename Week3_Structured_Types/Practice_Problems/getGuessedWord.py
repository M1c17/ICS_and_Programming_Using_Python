#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 13:27:16 2019

@author: MASTER
"""
# that takes in two parameters - a string, secretWord, and a list of 
#letters, lettersGuessed. This function returns a string that is comprised
# of letters and underscores, based on what letters in lettersGuessed are 
#in secretWord. This shouldn't be too different from isWordGuessed!

#When inserting underscores into your string, it's a good idea to add at
# least a space after each one, so it's clear to the user how many unguessed
# letters are left in the string

secretWord = 'apple'

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#lettersGuessed = ["a", "p", "l", "e"]
#lettersGuessed = ["a", "p", "l", "e", "p"]



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    ans = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            ans += letter 
        else:
            ans += ' _ '
    return ans
  
print(getGuessedWord(secretWord, lettersGuessed))  


##one line
def getGuessedWord(secretWord, lettersGuessed):
    word = ''
    for e in secretWord:
        word += e if e in lettersGuessed else "_"
    return word
print(getGuessedWord(secretWord, lettersGuessed))

####

def getGuessedWord(secretWord, lettersGuessed):
    return ''.join(c if c in lettersGuessed else '_' for c in secretWord)

print(getGuessedWord(secretWord, lettersGuessed))

#### with list 
def getGuessedWord(secretWord, lettersGuessed):
    guessedWord = list(secretWord)
    
    for i in range(len(guessedWord)):
        if guessedWord[i] not in lettersGuessed:
            guessedWord[i] = ' _ '
    return ''.join(guessedWord)

print(getGuessedWord(secretWord, lettersGuessed))
        
### empty list & append

def getGuessedWord(secretWord, lettersGuessed):
    guessedLetter = []
    
    for letter in secretWord:
        if letter in lettersGuessed:
            guessedLetter.append(letter)
        else:
            guessedLetter.append(' _ ')
    return ''.join(guessedLetter)

print(getGuessedWord(secretWord, lettersGuessed))           
