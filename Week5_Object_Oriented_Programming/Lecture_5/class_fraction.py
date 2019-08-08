#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 17:15:01 2019

@author: MASTER
"""

class Fraction(object):

    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __str__(self):
        return str(self.numer) + ' / ' + str(self.denom)

    def getNumer(self):
        return self.numer

    def getDenom(self):
        return self.denom

    def __add__(self, other):
        newNumer = self.numer * other.denom + self.denom * other.numer
        newDenom = self.denom * other.denom
        return Fraction(newNumer, newDenom)

    def __sub__(self, other):
        newNumer = self.numer * other.denom - self.denom * other.numer
        newDenom = self.denom * other.denom
        return Fraction(newNumer, newDenom)

numer = 2
denom = 2

print(numer)
print(denom)

add = numer + denom
print(add)

sub = numer - denom
print(sub)

