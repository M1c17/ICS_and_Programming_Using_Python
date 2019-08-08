#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 11:26:36 2019

@author: MASTER
"""

#HOW CAN WE DISPLAY THE VALUES RETURNED?
#What if we want to store the values returned 
#by the function call?
#there is a new syntax that will allow you to store 
#each element in the tuple into its corresponding variable.


def returnStringLength(*stringLenghtsTuple):
        stringLenghtsTuple(map(lambda x: len(x),tringLenghtsTuple))
        return stringLenghtsTuple

print(returnStringLength("Hi", "Hello", "Bye"))
#To store values in variable 

#StringOneLength = stringLenghtsTuple[0]
#StringTwoLength = stringLenghtsTuple[1]
#StringThreeLength = stringLenghtsTuple[2]

   
#StringOneLength, StringTwoLength, StringThreeLength = returnStringLength("Hi", "Hello", "Bye")
#print(StringOneLength)
#print(StringTwoLength)
#print(StringThreeLength)










