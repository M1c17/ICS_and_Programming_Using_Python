#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 09:38:48 2019

@author: MASTER
"""
from Lecture_5.Person import *

class Grades(object):
    '''A mapping from students to a list of grades'''
    def __init__(self):
        '''Create empty grade book'''
        self.students = [] # empty list
        self.grades = {} # maps idNum -> list of grades
        self.isSorted = True # True if self.student is sorted
        
    def addStudent(self, student):
        '''Assumes: student is of type Student
        Add student to the grade book'''
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        #create a spot in the dictionary 
        self.grades[student.getIdNum()] = []
        self.isSorted = False
        
    def addGrade(self, student, grade):
        '''Assumes: grade is a float
        add grade to the list of grades for student'''
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in gradebook')
            
    def getGrades(self, student):
        '''Return a list of grades for student'''
        try:
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError('Students not in gradebook')
            
    #get list of all students in the grade book
#    def allStudents(self):
#        '''Return a list of the students in the grade book'''
#        if not self.isSorted:
#            self.students.sort()
#            self.isSorted = True
#        #make a copy 
#        return self.students[:]
    #using generator 
    def allStudents(self):
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        for s in self.students:
            yield s 
        #yield them up one at the time as i ask for them 
        # it will give me the next one without generating the entire list 
    #get a report
def gradeReport(course):
    """Assumes: course if of type grades"""
    report = []
    #use method to get data; preserves information hiding
    for s in course.allStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1 
        try:
            average = tot/numGrades
            report.append(str(s) + '\'s mean grade is '
                          + str(average))
        except ZeroDivisionError:
            report.append(str(s) + ' has no grades')
    #return as str,with return between each student
    return '\n'.join(report)

   
#create a database students
ug1 = UG('Matt Damon', 2018)
ug2 = UG('Ben Affleck', 2019)
ug3 = UG('Drew Houston ', 2018)
ug4 = Grad('Mark Zuckerberg', 2017)
g1 = Grad('Bill Gates')
g2 = Grad('Steve Wozniak')

six00 = Grades()
six00.addStudent(g1)
six00.addStudent(ug2)
six00.addStudent(ug1)
six00.addStudent(g2)
six00.addStudent(ug4)
six00.addStudent(ug3)

six00.addGrade(g1, 100)
six00.addGrade(g2, 25)
six00.addGrade(ug1, 95)
six00.addGrade(ug2, 85)
six00.addGrade(ug3, 75)

#print()
#
#print(gradeReport(six00))
#
#print()
    
six00.addGrade(g1, 90)
six00.addGrade(g2, 45)
six00.addGrade(ug1, 80)
six00.addGrade(ug2, 75)               
            
print()

print(gradeReport(six00))

print()
#get out all students in a class 

for s in six00.allStudents():
    print(s)         
print()
    
for s in six00.students:
    print(s) 
#this violate the data hiding aspect of an object,
#and exposes internal representation
#   -if i were to change how i want to represent a grade book 
#    i should only need to change the methods within that object,
#   not external procedures that use it        

print(six00.getGrades(ug1))


    