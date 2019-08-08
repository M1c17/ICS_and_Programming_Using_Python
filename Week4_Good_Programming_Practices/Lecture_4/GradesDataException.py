#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 17:42:50 2019

@author: MASTER
"""

# suposse that we want to restructure this into a list of names 
# and a list of grades for each entry in the overall list 
# i can use the exception idea to make this happend 

data = []
file_name = input('Provide a name of a file of data: ')

try:
    fh = open(file_name, 'r')
except IOError:
    print('cannot open', file_name)
else:
    for new in fh:
        if new != '\n':
            addIt = new[:-1].split(',') # remove trailing \n
            data.append(addIt)
finally:
    fh.close() # close file even if fail 
    
#create a new data structure 
# handle case of no grade; Now allows for multiple names or no name 
gradesData = []

if data:
    for student in data:
        try:
            name = student[0:-1] # pull out the student names but the grades
            grades = int(student [-1]) # the last element 
            gradesData.append([name, [grades]])
#            gradesData.append([student[0:2], [student[2]]])
        except ValueError:
            gradesData.append([student[:], []]) # insert a empty list in that 
                                                # case with all the elem students
#            except IndexError:
#            gradesData.append([student[0:2], [  ]])
            
# when i run the code the answer its no what i expect 
# i make a assumpition that all the student have register the last name
# so the answer no cover what i need in response 
# go back and fix this 

            