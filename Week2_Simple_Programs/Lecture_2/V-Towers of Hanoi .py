#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 16:46:43 2019

@author: MASTER
"""

# TOWER OF HANOI 

# print an individual move from the from stack to the to stack 
def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n <= 0:
        raise NameError("no 0 or negative allowed") 
    if n == 1:          #test for a base case 
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)  # moving a smaller from to from the spare swap
        Towers(1, fr, to, spare)    # moving to move the simple case to the place im trying to go to 
        Towers(n-1, spare, to, fr)  # then i got to move the small size stack from the spare over to to  
        
print(Towers(4, 'P1', 'P2', 'P3'))      