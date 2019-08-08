#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 13:47:43 2019

@author: MASTER
"""
import datetime
#build a sys that organize information about people 
# start with a person object
class Person(object):
    def __init__(self, name):
        '''Create a person called name'''
        self.name = name
        self.lastname = name.split(' ')[-1]
        self.birthday = None
    
    #how can we get ot the last name
    def get_lastname(self):
        return self.lastname
    
    #how do we get the age 
    def get_age(self):
        '''return self's current age in days'''
        if self.birthday == None:
            raise ValueError
            # give the number of days since the person was born
        return (datetime.date.today() - self.birthday).days 
    
    #give this person a birthday 
    def set_birthday(self, month, day, year):
        '''sets self's birthday to birthDate
        when i gave a date of birthday to a person
        datetime convert that into a internal representation'''
        self.birthday = datetime.date(year, month, day)
        
    def __str__(self):
        '''return self's name'''
        return self.name
    
    #can we sort list of people
    def __lt__(self, other):
        '''return True if self's name is lexicographically less
        than other's name, and False otherwise'''
        if self.lastname == other.lastname:
            return self.name < other.name # compare full name 
        return self.lastname < other.lastname
 

#p1 = Person('Mark Zuckerberg')
#p1.set_birthday(5,14,84)
#p2 = Person('Drew Houston')
#p2.set_birthday(3,4,83)
#p3 = Person('Bill Gates')
#p3.set_birthday(10,28,55)
#p4 = Person('Andrew Gates')
#p5 = Person('Steve Wozniak')
#
#personList = [p1, p2, p3, p4, p5]
#print(p1)
#print()
##for everyperson in the personList 
#for e in personList:
#    print(e)
#print()
##sort the personList (mutate the list)
#personList.sort()
#for e in personList:
#    print(e)
#print()


class MITPerson(Person):
    nexIdNum = 0 # next Id Number to assign 
    #create instances for this class as well 
    def __init__ (self, name):
        Person.__init__(self, name) # initialize Person attributes
        self.IdNum = MITPerson.nexIdNum
        MITPerson.nexIdNum +=1
        
    def getIdNum(self):
        return self.IdNum
    #sorting MIT people use their IdNum no name!
    def __lt__(self, other):
        return self.IdNum < other.IdNum
    
    def speak(self, utterance):
        return self.name + " says: " + utterance #change behavior for subclasses
#       return (self.get_lastname()) + " says: " + utterance 

#m3 = MITPerson('Mark Zuckerberg')
#Person.set_birthday(m3,5,14,84)
#m2 = MITPerson('Drew Houston')
#Person.set_birthday(m2,3,4,83)
#m1 = MITPerson('Bill Gates')
#Person.set_birthday(m1,10,28,55) 
#
#MITPersonList = [m1, m2, m3]  
#    
#print(m1)
#print(m3)
#print(m1.speak("hi there"))
#
#for e in MITPersonList:
#    print(e)
#
#MITPersonList.sort()
#print()
#
#for e in MITPersonList:
#    print(e)
#    
#p1 = MITPerson('Eric')
#p2 = MITPerson('John')
#p3 = MITPerson('John')
#p4 = Person('John')
#print(p1 < p2)
##print(p1 < p4)
##AttributeError
#print(p4 < p1)

#create a class that covers all students 
class Students(MITPerson):
    '''create a class that captures common behaviors of subclasses;
    concentrate methods in one place, think of subclasses as a coherente whole'''
    pass

class UG(Students):
    '''Use the inherited MITPerson method to create an instance, which
    in turn will use the Person method'''
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
        
    def getClass(self):
        return self.year
    
    def speak(self, utterance):
        return MITPerson.speak(self, "Dude" + utterance)
    
class Grad(Students):
    
    def __init__(self, name, classYear = None):
        MITPerson.__init__(self, name)
        self.year = classYear
            
    def getClass(self):
        return self.year   

class TransferStudent(Students):
    #there is no expression in the body 
    pass

def isStudent(obj):
    return isinstance(obj, Students)

class Profesor(MITPerson):
    def __init__(self, name, department):
        MITPerson.__init__(self, name)
        self.department = department
        
    def speak(self, utterance):
        new = "In course " + self.department + " we say "
        return MITPerson.speak(self, new + utterance)
    
    def lecture(self, topic):
        return self.speak(' it is obvious that ' + topic)

#s1 = UG('Matt Damon', 2017)
#s2 = UG('Ben Affleck', 2017)
#s3 = UG('Lin Manuel Miranda', 2018)
#s4 = Grad('Leonardo Dicaprio')
#s5 = TransferStudent('Robert Deniro')
#faculty = Profesor('Dr. Arrogant', 'six')

#
#print(s1)
#print(s1.getClass())
#print(s1.speak('where is the quiz'))
#print(s2.speak('idk'))
#print(isStudent(s5))
#print(m3.speak('hi there'))
#print(s1.speak('hi there'))
#print(faculty.speak('hi there'))
#print(faculty.lecture('hi there'))
