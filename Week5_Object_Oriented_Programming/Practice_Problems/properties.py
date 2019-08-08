#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 13:12:03 2019

@author: MASTER
"""

#class P:
#    '''public attributes '''
#
#    def __init__(self,x):
#        self.x = x

class X:
    '''the property method x is used to check the limits of the values'''

    def __init__(self, x):
        self.x = x

    @property
    def X(self):
        return self.__x

    @X.setter
    def X(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
            
p1 = X(1001)
print(p1.x)
p1.X = -12
print(p1.X)

#class P:
    
#    '''Alternatively, we could have used a different syntax without decorators
#    to define the property. As you can see, the code is definitely less elegant 
#    and we have to make sure that we use the getter function in the __init__ method again''' 
#    def __init__(self,x):
#        self.set_x(x)
#
#    def get_x(self):
#        return self.__x
#
#    def set_x(self, x):
#        if x < 0:
#            self.__x = 0
#        elif x > 1000:
#            self.__x = 1000
#        else:
#            self.__x = x
#
#    x = property(get_x, set_x)