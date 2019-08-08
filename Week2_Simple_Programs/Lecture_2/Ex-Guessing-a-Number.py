#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 15:52:28 2019

@author: MASTER
"""

#end = '.'\n for input
#hlc = input("Enter 'h' to indicate the guess is too high. " +
#            "Enter 'l' to indicate the guess is too low. " +
#           "Enter 'c' to indicate I guessed correctly. ")



# In this program you create a program that guess a secret number
# The program works as follows: you (the user) thinks of an integer 
#between 0 (inclusive) and 100 (not inclusive). 
#The computer makes guesses, and you give it input - 
#is its guess too high or too low? Using bisection search, 
#the computer will guess the user's secret number!
#*********NOTE:f you use 0 to 100 and use floor division as is expected (//)
# then it must be exclusive because the average of two numbers can never
# reach 100.


low = 0
high = 100
ans = (high + low)//2
guesses = 0
print('Please think of a number between 0 and 100: ')

while True:
    ans = (high + low)//2
    guesses +=1 
    print('Is your secret number : ' + str(ans) + '?')

    request = input("Enter 'h' to indicate the guess is too high.\
                Enter 'l' to indicate the guess is too low.\
                Enter 'c' to indicate I guessed correctly: ")
    if request == 'c':
        print("Game over.Your secret number was: " + str(ans))
        break
    elif request == 'h':
        high = ans
        
    elif request == 'l':
        low = ans
    
    else:
        print('Sorry, I did not understand your input')        
print('number of guesses: ', guesses)