#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 13:57:24 2019

@author: MASTER
"""
#some attributes of a class hold for all instances in all cases. 

class Car(object):

    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

mustang = Car('Ford', 'Mustang')
print(mustang.wheels)
# 4
print(Car.wheels)
# 4