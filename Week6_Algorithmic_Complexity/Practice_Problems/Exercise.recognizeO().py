#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 13:30:07 2019

@author: MASTER
"""
# Assume n has been previously bound to some value
i = 0
while i < 5:
   n *= 2
   i += 1

print(n)

#answer = O(1) no matter the size of n the time execution is the same

def iterPower(a, b):
   result = 1
   while b > 0:
      result *= a
      b -= 1
   return result

#answer = O(b)

def recurPower(a, b):
   print(a, b)
   if b == 0:
      return 1
   else:
      return a * recurPower(a, b-1)

#answer = O(b) its the same above problem but in recursive

def recurPowerNew(a, b):
   print(a, b)
   if b == 0:
      return 1
  #b is even
   elif b%2 == 0:
      return recurPowerNew(a*a, b/2) #O(log(b))
  #b is odd
   else:                                # O(log(b) + (b)) = O(log(b)) winner
      return a * recurPowerNew(a, b-1) #O(n)


recurPowerNew(5, 5) 
print()
recurPowerNew(5, 50) 
print()
recurPowerNew(5, 500)

'''
Consider:

in case b is even, only return recurPowerNew(...) will be executed, because 
b/2 is still even, and so on, so O(log(b));
in case of b odd: 1st return will be return a * recurPowerNew(a, b-1), 
but the next b-1 will be even, getting the previous case, and obtaining, 
again, O(log(b)).'''