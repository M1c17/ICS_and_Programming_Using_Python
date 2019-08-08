#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 12:35:21 2019

@author: MASTER
"""

from currency import Ccy
x = Ccy(10.00, "EUR")
y = Ccy(10.00, "GBP")
x + y
Ccy(21.215104685942173, "EUR")
print(x + y)
#21.22 EUR
print(2*x + y*0.9)
#330.09 EUR