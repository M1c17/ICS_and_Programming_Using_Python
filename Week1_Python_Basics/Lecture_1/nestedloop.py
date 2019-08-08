#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#nested loop 
#a for loop inside another for loop 

for i in range(5):
    #code for the outer loop
    print('----> Outer loop: i', i)
    for j in range(3):
        #code for the inner loop
        print('----> Inner loop j', j)
    #code for the outer loop 
    print('out of inner loop, back to the outer loop')