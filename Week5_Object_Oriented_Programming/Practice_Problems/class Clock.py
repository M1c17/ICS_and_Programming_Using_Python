#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 17:21:37 2019

@author: MASTER
"""

#1.Consider the following code:
    
class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        time = '6:30'
        print(self.time)
#5:30
clock = Clock('5:30')
clock.print_time()

#2.Consider the following code:
    
class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self, time):
        print(time)

clock = Clock('5:30')
clock.print_time('10:30')
#10:30
#3.Consider the following code:
    
class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        print(self.time)
        
boston_clock = Clock('5:30')
paris_clock = boston_clock
paris_clock.time = '10:30'
boston_clock.print_time()
#10:30
