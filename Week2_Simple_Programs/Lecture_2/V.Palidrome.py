#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 17:50:57 2019

@author: MASTER
"""

# How to check if a string of characters is a palindrome?
# 1. first, convert the string to cha by stripping out puntuation &
# converting upper case to lower case 
# 2 base case: a str of length 0 or 1 is palindrome
# 3 recursive case: if first cha matches last cha then is a palindrome
# check everything in between to see if a palindrome 
def isPalindrome(s):
    '''Assumes s is a str
    Return True if s is a Palindrome False otherwise.
    Punctuaction marks, blanks and capitalization are ignored'''
    
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c 
        return ans 
    
    def isPal(s):
        print(' isPal called with ', s )
        if len(s) <=1:
            print('About to return True from base case')
            return True
        else:
            answer = s[0] == s[-1] and isPal(s[1:-1])
            print(' About to return ', answer, ' for ', s)
            return answer
        
    return isPal(toChars(s))

def testPalindrome():
    print('Try dogGod')
    print(isPalindrome('dogGod'))
    print('Try doGood')
    print(isPalindrome('doGood'))

print(testPalindrome())

#print("")
#print('Is s a palindrome?')
#print(isPalindrome('az'))
#
#print('')
#print('Is s a palindrome?')
#print(isPalindrome('Able was I, ere I saw Elba'))