#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:48:47 2019

@author: MASTER
"""

class Animal(object):
    '''Everything is an object: implements basic operations 
    in Py'''
    def __init__(self, age):
        self.age = age
        #define data attributes internally not pass in 
        self.name = None
    
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self,newname = ""):
        self.name = newname
    def __str__(self):
        return "animal: " + str(self.name) + ": " + str(self.age)
    
class Rabbit(Animal):
    #create a unique ID
    tag = 1
    def __init__(self, age, parent1 = None, parent2 = None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1
    
    def get_id(self):
        #method of a str to pad the beginning with zeros ex: 001
        # technique to make sure that everything prints out to the same size 
        return str(self.rid).zfill(3)
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    #inherent add method override a built in method
    def __add__(self, other):
        #return a new rabbit. returning obj of same type as this class
        return Rabbit(0, self, other)
    #compare two rabbits - override a built in method 
    def __eq__(self, other):
        # two rabbits are equal if they have same parents 
        parents_same = self.parent1.rid == other.parent1.rid \
                        and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent1.rid == other.parent2.rid \
                        and self.parent2.rid == other.parent1.rid
        return parents_same or parents_opposite
        
        
    def speak(self):
        print("meep")
    def __str__(self):
        return "rabbit: " + str(self.name) + ":" + str(self.age)
    
peter = Rabbit(2)
peter.set_name('Peter')
hopsy = Rabbit(3)
hopsy.set_name('Hopsy')
cotton = Rabbit(1, peter, hopsy)
cotton.set_name('Cottontail')
print(cotton)
print(cotton.get_parent1())
#addition of that instances
mopsy = peter + hopsy
mopsy.set_name('Mopsy')
print(mopsy.get_parent1())
print(mopsy.get_parent2())
print(mopsy == cotton)
print(cotton.__eq__(mopsy))


