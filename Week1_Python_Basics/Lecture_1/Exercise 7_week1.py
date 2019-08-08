#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#Exercises 7 
#nested loop a for loop inside a while loop 
iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1
    
#2 exercise a while loop inside a for loop 
#infinite loop while True / dont break 
for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        
#3 exercise 
#this exercise return the same than exercise 1 
count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    
    
#4 
#len(phrase) = 12
#Gives the same result the first one 
count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    
    
#5 
#Gives the same result the first one 
count = 0
phrase = "hello, world"
for iteration in range(5):
    count += len(phrase)
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    
    
    
    