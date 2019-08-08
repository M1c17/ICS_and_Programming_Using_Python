#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 17:20:40 2019

@author: MASTER
"""

#LAMBDA FUCNTION 

#COMBINE FIRST NAME & LAST NAME INTO A SINGLE "FULL NAME"

full_name =  lambda fn, ln: fn.strip().title() + ' ' + ln.strip().title()
print(full_name("  leonhard", "EULER"))
