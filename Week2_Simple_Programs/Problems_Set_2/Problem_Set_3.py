#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 16:57:12 2019

@author: MASTER
"""
# How can we calculate a more accurate fixed monthly payment than we did
# in Problem 2 without running into the problem of slow code? We can make
# this program run faster using a technique introduced in lecture - bisection search!
 
 
balance = 320000
Annual_InterestRate = 0.2
Monthly_interest_rate = Annual_InterestRate / 12.0

lowerbound = balance / 12.0
upperbound = (balance * (1 + Monthly_interest_rate)**12) / 12.0
epsilon = 0.01

testbalance = balance


while abs(testbalance) > epsilon:
    testbalance =  balance
    ans = (lowerbound + upperbound) / 2.0 
    
    for month in range(13):
        testbalance -= ans
        Interest = testbalance * Monthly_interest_rate 
        testbalance += Interest
        
    if testbalance > epsilon:
        lowerbound = ans 
        
    elif testbalance < epsilon:
        upperbound = ans
           
print('Lowest Payment: ', round(ans,2))
    

    
    
      
    
        