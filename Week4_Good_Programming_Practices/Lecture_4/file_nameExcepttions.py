#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 17:03:52 2019

@author: MASTER
"""

#open up a file 
#read data in from it 

data = []
file_name = input('Provide a name of a file of data: ')

try:
    fh = open(file_name, 'r')
except IOError:
    print('cannot open', file_name)
else:
    for new in fh:
        if new != '\n':
            addIt = new[:-1].split(',') # remove trailing \n
            data.append(addIt)
finally:
    fh.close() # close file even if fail 