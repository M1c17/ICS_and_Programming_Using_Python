#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 10:40:49 2019

@author: MASTER
"""

class House(object):
    def __init__(self, street, rooms, bathrooms):
        self.street = 35
        self.rooms = 15
        self.bathrooms = 16
        #Not provide has an input
        self.clean = True
        
    def cleanHouse(self):
        if not self.clean:
            self.clean = True
            print("This House is now clean")
        else:
            print("This House is already clean")
    
    def unCleanHouse(self):
        if self.clean:
            self.clean = False
            print("This House is now Dirty")
        else:
            print("This House was Dirty already")
            
    def talk(self, phrase):
        print(phrase)
        
house1 = House(35, 15, 16)
house2 = House(50, 25, 86)
house1.street 
house1. rooms
house1.bathrooms
house1
house1.clean
house1.cleanHouse()
house1.unCleanHouse()
house1.cleanHouse()
house1.talk("Hi, I'm a talking House")
house2.clean  