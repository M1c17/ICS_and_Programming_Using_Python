#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = 'azcbobobegghakl'

print("Number of vowels:", sum(vowel in "aeiou" for vowel in s))

#one line example (ELIZABETH)
print(len([letter for letter in s if letter in ['a', 'e', 'i', 'o', 'u']]))