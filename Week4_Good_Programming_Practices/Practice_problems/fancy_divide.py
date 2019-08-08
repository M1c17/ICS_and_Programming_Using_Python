#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 19:32:31 2019

@author: MASTER
"""
#1.
def fancy_divide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        print("-1")
    else:
        print("1")
    finally:
        print("0")
        
fancy_divide([0, 2, 4], 1)
#1, 0
fancy_divide([0, 2, 4], 4)
#-1, 0
fancy_divide([0, 2, 4], 0)
#0, error (ZeroDivisionError)
#Now, for problem 1 part 3 (one of the trickier ones), we attempt to
# divide by zero in the 'try' block, leading to a ZeroDivisionError and
# breaking out of that block early.... So the program moves along to the
# next block, carrying the error with it. The 'except' block is for 
#IndexError, so we skip that. The 'else' block only runs when no errors 
#were generated in 'try', so we skip that, too. Now 'finally' executes 
#(since this happens no matter what) and we print '0' to the console... 
#Okay, the function returns, but wait! The ZeroDivisionError still remains.
# So python raises it and the answer is '0, error'.

#2.
def fancy_divide(numbers, index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        fancy_divide(numbers, len(numbers) - 1)
    except ZeroDivisionError:
        print("-2")
    else:
        print("1")
    finally:
        print("0")
fancy_divide([0, 2, 4], 1)
#1, 0
fancy_divide([0, 2, 4], 4) 
#1, 0 , 0
#For problem 2 part 3, the approach is very similar and yields '-2, 0'.
# Part 2 of problem 2 is a bit trickier because it makes a recursive call,
# so you have to think of what the 'inner' stack frame produces before the
# original caller ('outer' stack frame) continues. The result is 1, 0, 0.
fancy_divide([0, 2, 4], 0)
#-2, 0

#3.    
def fancy_divide(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError:
            fancy_divide(numbers, len(numbers) - 1)
        else:
            print("1")
        finally:
            print("0")
    except ZeroDivisionError:
        print("-2")
        
fancy_divide([0, 2, 4], 1)
#1, 0
fancy_divide([0, 2, 4], 4)
#1, 0 , 0
fancy_divide([0, 2, 4], 0)
#0,-2
#Problem 3 part 3 is the trickiest one yet... nested 'try' blocks. Let's go through programmatically and it'll work itself out:
#
#Enter try block 1:
#
#    Enter try block 2:
#
#        oops, we divided by zero! generate ZeroDivision error and break from 'try'
#
#    check against 'except' block... nope, not IndexError, continue
#
#    check against 'else' block... nope, an error is present, should not run 'else'
#
#    execute finally block because it always executes.
#
#        print '0'
#
#check results of outer try attempt (which here is whatever resulted from inner try attempt) against ZeroDivisionError... Ah! We have one!
#
#    print '-2'
#4.

def fancy_divide(list_of_numbers, index):
    try:
        try:
            raise Exception("0")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    except Exception as ex:
        print(ex)
        
fancy_divide([0, 2, 4], 0)


#5.

def fancy_divide(list_of_numbers, index):
    try:
        try:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
        finally:
            raise Exception("0")
    except Exception as ex:
        print(ex)
        
fancy_divide([0, 2, 4], 0)
        
        
        