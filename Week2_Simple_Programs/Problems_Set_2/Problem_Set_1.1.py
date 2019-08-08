#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 20:15:55 2019

@author: MASTER
"""
#calculate statements on the monthly payment and remaining balance
#For each month:
#
#Compute the monthly payment, based on the previous month’s balance.
#
#Update the outstanding balance by removing the payment, then charging 
#interest on the result.
#
#Output the month, the minimum monthly payment and the remaining balance.
#
#Keep track of the total amount of paid over all the past months so far.
#
#Print out the result statement with the total amount paid and the 
#remaining balance.
#
#Use these ideas to guide the creation of your code.

month = 12
balance = 0
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for n in range(1, 13):
    Minimum_Payment = round(balance * monthlyPaymentRate, 2)
    Unpaid_Balance = balance - Minimum_Payment
    Monthly_interest_rate = annualInterestRate / month
    Interest = Monthly_interest_rate * Unpaid_Balance
    balance = round((Unpaid_Balance + Interest),2)
    
    print('Month ' + str(n) + ' Minimun montly payment ' + str(Minimum_Payment) + \
     ' Remaining balance: ' + str(balance))
    