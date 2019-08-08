#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 12:46:32 2018

@author: MASTER
"""

#NEWTON RAPHSON 
#Gives us another way of generating guesses, which we can check; 
#is very efficient 

epsilon = 0.01  # how close I'm to the answer 
y = 24.0        # looking for 
guess = y/2.0   # Initial guess 
numGuesses = 0

while abs(guess * guess - y)  >= epsilon:
    numGuesses += 1 
    guess = guess - (((guess ** 2) - y)/(2 * guess)) #the equation for newton - raphson
print('numGuesses = ' + str(numGuesses))
print('Square root of ' + str(y) + ' is about ' + str(guess))
