#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 12:09:48 2019

@author: MASTER
"""

from Practice_Problems.currencies import Ccy
v1 = Ccy(23.43, "EUR")
v2 = Ccy(19.97, "USD")
print(v1 + v2)
#32.89 EUR
print(v2 + v1)
#31.07 USD
print(v1 + 3) # an int or a float is considered to be a EUR value
#27.43 EUR
print(3 + v1)
#27.43 EUR