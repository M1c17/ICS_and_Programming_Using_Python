#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 13:31:49 2019

@author: MASTER
"""

class Robot:
    def __init__(self, name, build_year, lk = 0.5, lp = 0.5):
        self.name = name
        self.build_year = build_year 
        self.__potencial_physical = lk
        self.__potencial_psychic = lp
        
    @property
    def condition(self):
        s = self.__potencial_physical + self.__potencial_psychic
        if s <= -1:
            return "I feel miserable"
        elif s <= 0:
            return "I feel bad"
        elif s <= 0.5:
            return "could be worse!"
        elif s <= 1:
            return "Seems to be okay"
        else:
            return " Great"
        
if __name__ == "__main__":
    x = Robot("Marvin", 1979, 0.2, 0.4)
    y = Robot("Caliban", 1993, -0.4, 0.3)
    print(x.condition)
    print(y.condition)
    
        