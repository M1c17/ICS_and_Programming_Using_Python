#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 21:32:46 2019

@author: MASTER
"""

#Exception Handling Demo:

"""
Shane Ryan
10/3/2018

Explain exception handling!!!
"""

def doSomething(foo, bar):
    try:    # attempt a block of code. Break on error.
        if (foo):
            print("In try block pt. 1")
        if (foo / bar):
            print("In try block pt. 2")
    except ZeroDivisionError:    # 'except' handles the specified error type.
        print("Received ZeroDivisionError in try block")
    else:
        print("Else executes when no errors are encountered in try block")
    finally:
        print("Finally will execute no matter what")

    # now if any errors remain after 'finally' that were not
    # handled by an appropriate 'except' statement, they are raised.


print("Calling w/ no errors:\n")
try:
    doSomething(1, 2)       # should not raise any errors
except Exception as ex:     # excepting ANY error of type exception!
    print("An unhandled exception is still present!")
    print(ex)
else:
    print("Looks like no unhandled errors were encountered!\n")



print("Calling w/ ZeroDivisionError:\n")
try:
    doSomething(1, 0)       # division by zero! no problem, handled that
except Exception as ex:
    print("An unhandled exception is still present!")
    print(ex)
else:
    print("Looks like no unhandled errors were encountered!\n")



print("Calling w/ unhandled ValueError:\n")
try:
    doSomething('1', '2')   # uh-oh, can't divide strings!
except Exception as ex:
    print("An unhandled exception is still present!")
    print(ex)
else:
    print("Looks like no unhandled errors were encountered!\n")