#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 09:27:06 2019

@author: MASTER
"""
#Indexing Tuples and Lists that contain Tuples and Lists as elements

###
list1 = [["house1", ["house2", "house3"], "house4"],"house5"]

print("house3" in list1[0][1])
print(list1[0][1][1])

#how do you rich "dog5" in dog Tuple?
#What item will return True for the expression <item> in dog Tuple?
#how do you reach "dog2" in dogs Tuple?

dogTuple = (("dog1",("dog2",)),(("dog3",), ("dog4", "dog5")))

print("dog5" in dogTuple[1][1])
print(dogTuple[1][1][1])
print("dog5" in dogTuple)
print("dog2" in dogTuple[0][1][0])
print(dogTuple[0][1][0])

