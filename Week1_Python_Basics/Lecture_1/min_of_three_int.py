#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
write a program to find the minimun of three int

"""

x, y, z = map(str(input('Enter three space separeted int: ')).split())

if x < y and x < z:
    print('Minimun among' + str(x) + ',' + str(y) + ',' + str(z) + 'is' + str(x))
if y < z:
    print('Minimun among' + str(x) + ',' + str(y) + ',' + str (z) + 'is' + str(y))
else:
    print('Minimun among' + str(x) + ',' + str(y) + ',' + str(z) + 'is' + str(z))