#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Recap:
# Redefine the variable to change an individual character in string 
s = 'hello'
s = 'y' + s[1:len(s)]
print(s)

# I can loop over string 
# Im looping for an index over all the indices into string 
s = 'abcdefgh'

for i in range(len(s)):
    if 'i' == s[i] or 'u' == s[i]:
        print("There is an i or u")
        
# Same :
# s is iterable. lets character start with the first element of s 
# im looping over all the characters into string
for char in s:
    if 'i' == char or 'u' == char:
        print("There is an i or u")

