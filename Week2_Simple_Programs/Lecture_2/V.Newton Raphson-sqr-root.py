#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 16:16:51 2019

@author: MASTER
"""

# Newton Raphson 
# finding the square root
# Find x such that x ** 2 - 24 is within epsilon of 0 

epsilon = 0.01
k = 24.0
guess = k/2.0
iteration = 0

while abs(guess * guess - k) >= epsilon:
    guess = guess - (((guess ** 2)-k) / (2 * guess))
    iteration +=1
print('Square root of ', k,' is about', guess, ' iterarion = ', iteration)