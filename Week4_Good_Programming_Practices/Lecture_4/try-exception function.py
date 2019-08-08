#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 15:56:32 2019

@author: MASTER
"""

try:
    a = int(input("Tell me one number: "))
    b = int(input("Tell me another number: "))
    print(a/b)
    print("Okay")
    
except:
    print("Bug in user input. ")
print("Outside")

###
try:
    a = int(input("Tell me one number: "))
    b = int(input("Tell me another number: "))
    print('a/b = ', a/b)
    print('a+b = ', a+b)
    
except ValueError:
    print("Could not convert to a number")
except ZeroDivisionError:
    print("Can't divide by zero")
except:
    print("Something went very wrong.")   
    
       
print("Outside")
