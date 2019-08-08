#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = 'azcbobobegghakl' 

#one line Elizabeth

print('Longest substring in alphabetical order is:',
    max([s[i:j] for i in range(len(s)-1) for j in range(i+1, len(s)+1) if s[i:j] == ''.join(sorted(s[i:j]))], key=len))