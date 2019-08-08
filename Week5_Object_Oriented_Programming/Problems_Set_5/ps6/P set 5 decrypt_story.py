#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 21:20:10 2019

@author: MASTER
"""

from ps6 import *

#def decrypt_story():
#    
#    story = get_story_string()
#    cipher = CiphertextMessage(story)
#    
#    return cipher.decrypt_message()
#
#print(decrypt_story())


def decrypt_story():
    
    return CiphertextMessage(get_story_string()).decrypt_message()

print(decrypt_story())