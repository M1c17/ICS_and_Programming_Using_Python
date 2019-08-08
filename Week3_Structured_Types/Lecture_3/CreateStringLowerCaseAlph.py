#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 20:42:37 2019

@author: MASTER
"""

#CREATE A STRING OF THE LOWER CASE ALPHABET 

import string

alphabet_in_lower_case = string.ascii_lowercase

print(alphabet_in_lower_case)

####

''.join(chr(i) for i in (range(ord('a'), 26 + ord('a'))))

''.join(list(map(chr, list(range(ord('a'), 26 + ord ('a'))))))

''.join(chr(i + ord('a')) for i in range(26))

