#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

ask the user to enter an integer and prints two integer,root & pwr
such that 0 <pwr< 6 and root**pwr is == to the integer entered 
by the user . if no pair of integer exist shoul be print a message to
that effect 

"""

x = int(input('Enter a int: '))
root = 0
while root < abs(x):
    root +=1
    for pwr in range(1,6):
        if root ** pwr == abs(x):
            if x < 0:
                print(str(-root)+ '**' + str(pwr) + ' = ' + str(x))
            else:
                print(str(root)+ '**' + str(pwr) + ' = ' + str(x))
            
print('no such pair of integer exist')