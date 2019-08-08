    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 12:02:14 2019

@author: MASTER
"""
# DETERMINE IF A CHAR IS IN A STR 
# use bisection search 
# string is sorted in alphabetical order
 
# base case: empty str
# base case: len 1
# Base case: test the midcha of aStr against the cha you're looking 
# for same = True
# slice string to have the midcha before recursive
# recursive case: elif test cha < midcha if so consider the lower half 
#of the str
# recursive case: else otherwise consider the upper half of the str 



def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Base case when the str is empty
    if aStr == '':
        return False
    # Base case when len is of length 1
    if len(aStr) == 1 :
        return aStr == char 
    # Base case when the test cha = midchar 
    midIndex = len(aStr)//2
    midchar = aStr[midIndex]
    if char == midchar:
        return True 
   # Recursive case: If the test character is smaller than the middle 
   #  character, recursively search on the first half of aStr
    elif char < midchar:
        return isIn(char, aStr[:midIndex -1])
    #Recursive case: else consider the last half of aStr
    else:
        return isIn(char, aStr[midIndex + 1:])
    
    
print(isIn('c','abc'))




 
    