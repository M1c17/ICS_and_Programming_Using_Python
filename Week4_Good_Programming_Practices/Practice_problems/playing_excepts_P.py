#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 20:20:14 2019

@author: MASTER
"""

def fd():
    try:
        try:
            print(0)
            raise NameError
            print(1)
        finally:
            print(2)
            raise ValueError
            print(3)
    except ValueError:
        print(4)
        raise ZeroDivisionError
        print(5)
fd()       
        
###
def exception_demo():
    try:
        try:
            return 0
        finally:
            raise Exception()
            return 2
    except:
        return 1

print(exception_demo())


        
###
def fancy_divide(list_of_numbers, index):
    try:
        try:
            raise Exception("0")
        finally:
            denom = list_of_numbers[index]
            try:
                for i in range(len(list_of_numbers)):
                    list_of_numbers[i] /= denom
            except ZeroDivisionError:
                print('division by zero')
    except Exception as ex:
        print(ex)
        
fancy_divide([0, 2, 4], 0)