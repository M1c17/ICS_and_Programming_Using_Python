#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 11:10:13 2019

@author: MASTER
"""

# what are the data attributes
# <for animal: name, age>

# what are the procedural attributes?
# what kind of thing can you do with the obj?
#<for animal: make a sound>

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
    
#myanimal = Animal(3)
#print(myanimal)
#myanimal.set_name('foobar')
#print(myanimal)

class Cat(Animal):
    def speak(self):
        print("meow")
    def __str__(self):
        return "cat: " + str(self.name) + ":" + str(self.age) 
    
jelly  = Cat(1)
print(jelly.get_name())
jelly.set_name("jelly belly")
print(jelly)
print(Animal.__str__(jelly))
blob = Animal(1)
blob.set_name()
print(blob)

class Rabbit(Animal):
    def speak(self):
        print("meep")
    def __str__(self):
        return "rabbit: " + str(self.name) + ":" + str(self.age)
    
peter = Rabbit(5)
print(jelly.speak())
print(peter.speak())

class Person(Animal):
    #add a new functionality
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []
    def get_friends (self):
        return self.friends
    def add_friends(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("hello")
    def age_diff(self, other):
        #alternate way: diff =  selfage - other.age
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(self.name, "is", diff, "years older than", other.name)
        else:
            print(self.name, "is", -diff, "years younger than", other.name)
    def __str__(self):
        return "person: " + str(self.name) + ":" + str(self.age)
        
eric = Person("eric", 45)
john = Person("john", 55)
print(eric.speak)
print(eric.age_diff(john))
print(Person.age_diff(eric, john))
eric.add_friends("cocoa")
print(eric.friends)


import random 

class Student(Person):
    #add a new functionality 
    def __init__(self, name, age, major=None):
        '''create a constructor '''
        Person.__init__(self, name, age)
        #define a new data attribute 
        self.major = major
    def change_major(self, major):
        self.major = major 
    def speak(self):
        #random() method gives back float in [0,1]
        #from random class
        r = random.random()
        if r < 0.25:
            print("i have homework")
        if 0.25 <=  r < 0.5:
            print("i need sleep")
        elif 0.5 <= r < 0.75:
            print("i should eat")
        else:
            print("i am wathing tv")
    def __str__(self):
        return "student: " + str(self.name) + ":" + str(self.age) + ":" + str(self.major)
            
fred = Student("fred", 19, "Course VI")
print(fred)
print(fred.speak())
fred.change_major('cv')
print(fred)