#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 12:11:19 2019

@author: MASTER
"""

class Test:
    def speak(self, x = 0):
        if x == 0:
            return 'Hello'
        else:
            return 'Hello for another class'
    def inht_mtd(self):
        return 'This function is called via inheritance from class instance'
    
class Test2:
    def speak(self):
        return Test.speak(self, 1)
    
class Test3(Test):
    pass

a = Test()
b = Test2()
c =Test3()

print('Test speak: ', a.speak())
print('Test2 speak: ', b.speak())
print('Test3 method: ', c.inht_mtd())
#print('test2 inht_mtd: ', b.inht_mtd())  