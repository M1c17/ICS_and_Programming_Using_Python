#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 14:50:48 2019

@author: MASTER
"""

#This game is a lot like Scrabble or Words With Friends
#Each valid word receives a score, based on the length of the word
# and the letters in that word.

#These are the provided test functions:

#test_getWordScore()
#Test the getWordScore() implementation.
#
#test_updateHand()
#Test the updateHand() implementation.
#
#test_isValidWord()
#Test the isValidWord() implementation.
'''
Loading word list from file...
   83667 words loaded.
Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: p z u t t t o
Enter word, or a "." to indicate that you are finished: tot
"tot" earned 9 points. Total: 9 points
Current Hand: p z u t
Enter word, or a "." to indicate that you are finished: .
Total score: 9 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: r
Current Hand: p z u t t t o
Enter word, or a "." to indicate that you are finished: top
"top" earned 15 points. Total: 15 points
Current Hand: z u t t
Enter word, or a "." to indicate that you are finished: tu
Invalid word, please try again.
Current Hand: z u t t
Enter word, or a "." to indicate that you are finished: .
Total score: 15 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: a q w f f i p
Enter word, or a "." to indicate that you are finished: paw
"paw" earned 24 points. Total: 24 points
Current Hand: q f f i
Enter word, or a "." to indicate that you are finished: qi
"qi" earned 22 points. Total: 46 points
Current Hand: f f
Enter word, or a "." to indicate that you are finished: .
Total score: 46 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: a r e t i i n
Enter word, or a "." to indicate that you are finished: inertia
"inertia" earned 99 points. Total: 99 points
Run out of letters. Total score: 99 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: e
'''


#In our program, a hand will be represented as a dictionary: the keys are 
#(lowercase) letters and the values are the number of times the particular 
#letter is repeated in that hand


try:
    if k in Hand:
        hand[x] = hand.get(key,default)
    return Hand
except KeyError as ex:
    print(Hand)
    
dic.keys()
if the key is in the dictionary:
     returns the value for key if key is in the dictionary d
otherwise, we get a KeyError
except KeyError as ex:
    hand[x]