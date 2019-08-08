#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 18:09:18 2019

@author: MASTER
"""

def textToWords(lyrics):
    lwords = []
    build = ''
    for letter in lyrics:
        if (letter != ' ') and (letter != ','):
            build = build + letter
            
        elif len(build) > 0:
            lwords.append(str(build))
            print(lwords)
            build = ''
    return lwords

beatles_wmggw=["I", "look", "at", "you", "all", "see", "the", "love",
               "there", "that's", "sleeping", "While", "my", "guitar",
               "gently", "weeps", "I", "look", "at", "the", "floor",
               "and", "I", "see", "it", "needs", "sweeping", "Still",
               "my", "guitar", "gently", "weeps", "I", "don't", "know",
               "why", "nobody", "told", "you", "How", "to", "unfold",
               "your", "love", "I", "don't", "know", "how", "someone",
               "controlled", "you", "They", "bought", "and", "sold",
               "you", "I", "look", "at", "the", "world", "and", "I",
               "notice", "it's", "turning", "While", "my", "guitar",
               "gently", "weeps", "With", "every", "mistake", "we",
               "must", "surely", "be", "learning", "Still", "my",
               "guitar", "gently", "weeps", "I", "don't", "know",
               "how", "you", "were", "diverted" "You", "were",
               "perverted", "too", "I", "don't", "know", "how", "you",
               "were", "inverted", "No", "one", "alerted", "you", "I",
               "look", "at", "you", "all", "see", "the", "love", "there",
               "that's", "sleeping", "While", "my", "guitar", "gently",
               "weeps", "Look", "at", "you", "all", "Still", "my",
               "guitar", "gently", "weeps"]

print(textToWords(beatles_wmggw))