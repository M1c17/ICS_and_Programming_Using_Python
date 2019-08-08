#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 18:39:17 2019

@author: MASTER
"""

# assume were given a class list for a subject: each entry is a list of two 
# parts
# a list of first and last name for a student 
# a list of grades on assigments
# create a new class list, with name,grades, and an average 

def get_stats(class_list):
    new_stats = []
    for elt in class_list:
        new_stats.append([elt[0], elt[1], avg(elt[1])])
    return new_stats 

def avg(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError: # when no grade data 
        print('no grades data') # return None
        return 0.00
        

test_grades = [[['peter', 'parker'], [10.0, 5.0, 85.0]],
               [['bruce','wayne'], [10.0, 8.0, 74.0]],
               [['captain', 'america'], [8.0, 10.0, 96.0]],
               [['deadepool'],[]]]
