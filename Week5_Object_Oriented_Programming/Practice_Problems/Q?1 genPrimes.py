#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 10:00:30 2019

@author: MASTER
"""

#DIFERENTS PROBLEM WITH PRIMES
'''
Explanation:

We could write a function that does any of the choices. However a generator is
 nice because we can ask the generator for the next item, one at a time, and 
 we don't waste time computing values that we don't ultimately want 
 (or won't want for a long time).

Here are some examples of how one might code a function for each of the above
 options without a generator:'''
    
def genPrimesFn():
    '''Return 17 primes numbers '''
    primesList = []
    guess = 1
    while guess < 17:
        guess += 1
        for p in primesList:
            if guess % p == 0:
                break
        else:
            primesList.append(guess)
    return primesList

p = genPrimesFn()
print(p)
print()


def genPrimes():
    '''print every 10 th prime numbers, until you have
    print 20 th of them'''
    primes = []
    last = 1
    counter = 1
    while True:
        last +=1
        for p in primes:
            if last % p == 0:
                break 
        else:
            primes.append(last)
            counter += 1
            if counter % 10 == 0 :
                 # Print every 10th prime
                print(last)
            if counter % (20*10) == 0:
                # Quit when we've printed the 10th prime 20 times (ie we've
                # printed the 200th prime)
#                print(primes)
                return 
            
p = genPrimes()
print(p)
print()



def genPrimesuser():
    '''Function to keep printing the prime number until the user stops the program.
    This way uses user input; you can also just run an infinite loop (while True)
    that the user can quit out of by hitting control-c'''
    primes = []
    guess = 1
    usrin = 'y'
    while usrin != 'n':
        guess += 1
        for p in primes:
            if guess % p == 0:
                break
        else:
            primes.append(guess)
            print(guess)
            usrin = input('Do you want print the next prime? [y/n] ')
            while usrin != 'y' and usrin != 'n':
                print('I dont understand your input. Please enter y for yes, or n for no.')
                usrin = input('Do you want print the next prime? [y/n] ')
                
p = genPrimesuser()
print(p)
                    
                
            
            
