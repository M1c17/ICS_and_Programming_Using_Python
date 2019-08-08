#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 20:33:37 2019

@author: MASTER
"""

# REMOVE A LETTER ONCE IT HAS been guessed by the user
 
s = 'bob'
choiceletter = 'abcdefgjklmnopqrstuvwxyz'
ans = ''
for c in choiceletter:
    if c not in s:
        ans += c
print(s, choiceletter, ans)

##listcomp version 
ans = ''.join([c for c in choiceletter if c not in s])

print(ans)

#CREATE A STRING OF THE LOWER CASE ALPHABET 

import string

alphabet_in_lower_case = string.ascii_lowercase

print(alphabet_in_lower_case)

