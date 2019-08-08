#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 14:52:33 2019

@author: MASTER
"""

# Write a program to calculate the credit card balance after one year
# if a person only pays the minimum monthly payment required by the credit card
# company each month.
# 
# Write a program to calculate the credit card balance after one year
# if a person only pays the minimum monthly payment required by the credit card
# company each month.
 
 
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04    
interest = annualInterestRate / 12
for i in range(12):
    balance *= (1 - monthlyPaymentRate) * (1 + interest) 
print("Remaining balance: {:0.2f}".format(balance))

