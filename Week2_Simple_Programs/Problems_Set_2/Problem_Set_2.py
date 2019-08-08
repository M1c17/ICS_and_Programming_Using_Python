#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 11:14:37 2019

@author: MASTER
"""
# Now write a program that calculates the minimum fixed monthly payment needed
# in order pay off a credit card balance within 12 months. By a fixed monthly
# payment, we mean a single number which does not change each month, but instead
# is a constant amount that will be paid each month.

# Assume that the interest is compounded monthly according to the balance at the
# end of the month (after the payment for that month is made).
# The monthly payment must be a multiple of $10 and is the same for all months.
# Notice that it is possible for the balance to become negative using this payment
# scheme, which is okay.

balance = 4773
annualInterestRate = 0.2
Monthly_interest_rate = annualInterestRate / 12
lowest_monthly_payment = 0
Minimum_fixed_monthly_payment = 10.0
# Copy balance into myBalance
initial_balance = balance


# Loop through to determine minimum fixed payment to pay off in one Year
# Start with $10 payments, increase by $10 each iteration
# Loop through calculating if monthly payment will pay off in 12 months
while initial_balance >  0.0:    
    lowest_monthly_payment += Minimum_fixed_monthly_payment
# Apply payments and interest for each of twelve months
# Once balance at end is less then 0 will have
# calculated min fixed payment   
    for month in range(1,13):   
        Moontly_Unpaid_Balance = initial_balance - lowest_monthly_payment
        Interest = Monthly_interest_rate * Moontly_Unpaid_Balance
        initial_balance = round((Moontly_Unpaid_Balance + Interest),2)
        #print(initial_balance)
    if initial_balance > 0.0:
        initial_balance = balance
    
    
print('Lowest Payment: ' + str(lowest_monthly_payment) + ' balance ' \
      + str(balance) )
#print("Lowest: {:d}".format(payment))
#At the end of 12 months, the balance needs to be zero or less, 
#or you need to change the payment and try again





        






















