#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 17:51:18 2019

@author: MASTER
"""

# create a list of the squares of the first 100  positives int 

# first iterate without list comprenhension 

squares = []

for i in range(1, 101):
    squares.append(i ** 2)
print(squares)

## now list comprehension

squares2 =  [i ** 2 for i in range(1, 101)]

print(squares2)

# CREATE A LIST OF REMAINDERS WHEN YOU THE DIVIDE DE FIRST 100 SQUARES BY 5

remainders5 = [x ** 2 % 5 for x in range(1, 101)]
print(remainders5)

remainders11 = [x ** 2 % 11 for x in range(1, 101)]
print(remainders11)

# find the movie with the letter G

movies = ["Stars Wars", "Gandhi", "Casablanca", "Shawshank Redenption",
          "Toy Story", "Gone with the wind", "Citizen Kane", "Its is a wonderful life",
          "The wizard of oz", "Gattaca", "Rear Window", "Ghostbusters", "To kill a Mockingbird",
          "Good Wi 11 Hunting", "2001: A Space Odyssey", "Raiders of the lost Ark", "Grondhog Day",
          "Close Encounters of the third Kind"]

gmovies = []
for title in movies:
    if title.startswith("G"):
        gmovies.append(title)
print(gmovies)

gmovies = [title for title in movies if title.startswith("G")]
print(gmovies)

#HOW WOULD YOU PERFORM SCALAR MULTIPLICATION 
# WHAT IF WE WANT MULTIPLY EACH NUMBER BY FOURT

v =[2, -3, 1]
w = [4 * x for x in v]
print(w)

#compute the cartesian product of sets 
# if A and B are sets
# then the cartesian product is the set of pairs (a, b)
# where 'a' is in A and 'b' is in B

# A x B = {(a, b) | a e A, b e B}

#A = {1, 3}
#B = {x, y}
#A x B = {(1, x), (1, y), (3, x), (3, x) }

A = [1, 3, 5, 7]
B = [2, 4, 6, 8]

cartesian_product = [(a, b) for a in A for b in B]

print(cartesian_product)

#et A and B be two sets, the cross product (or Cartesian product) of A and B, written A×B, is the set of all pairs wherein the first element is a member of the set A and the second element is a member of the set B. 

#Mathematical definition: 
#A×B = {(a, b) : a belongs to A, b belongs to B}. 
#It's easy to be accomplished in Python:

colours = ['red', 'green','yellow', 'blue']
things = ['house','car', 'tree']

coloured_things = [(x, y) for x in colours for y in things]
print(coloured_things)
















        






