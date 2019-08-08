#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the
string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example if s = 'azcbobobegghakl', your program should print: 
    Number of vowels: 5

"""

s = str(input('phrase: '))

vowel="aeiou"
count= 0
for letters in s:
    if letters in vowel:
        count+=1
print ("Number of vowels:",count) 