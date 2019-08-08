#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 13:20:32 2019

@author: MASTER
"""

class Customer(object):
#     """A customer of ABC Bank with a checking account. Customers have the
#    following properties:
#
#    Attributes:
#        name: A string representing the customer's name.
#        balance: A float tracking the current balance of the customer's account.
#    """
    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.name = name
        self.balance = balance
        
    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than avalible balance')
        self.balance -= amount
        return self.balance 
    
    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        return self.balance 
    
    
jeff = Customer('Jeff Knupp', 1000.0)
jeff.withdraw(500)
print(jeff.name)
print(jeff.balance)
print(jeff.deposit(300))