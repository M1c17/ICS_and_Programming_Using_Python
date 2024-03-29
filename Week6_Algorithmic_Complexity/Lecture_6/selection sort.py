#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 16:38:06 2019

@author: MASTER
"""
'''
find the rigth pointer and then insert in the rigth spot'''

def selection_sort(L):
    suffixSt = 0
    while suffixSt != len(L): #O(len(L))
        for i in range(suffixSt, len(L)): #O(len(L)) - suffixSt times
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
        print(L)
        
test = [1, 5, 3, 8, 4, 9, 6, 2]
print(selection_sort(test))        

#outer loop executes len(L) times
#inner loop executes len(L) - i times 
# complexity of selection sort is O(n^2) where n is len(L) 
    
def selSort(L):
    for i in range(len(L) - 1): #O(len(L))
        print(L)
        mindIndx = i
        minVal = L[i]
        j = i + 1
        while j < len(L): #O(len(L))
            if minVal > L[j]:
                mindIndx = j
                minVal = L[j]
            j += 1
            
        if mindIndx != i:
            temp = L[i]
            L[i] = L[mindIndx]
            L[mindIndx] = temp
    print(L)
    
test = [1, 5, 3, 8, 4, 9, 6, 2]
print(selSort(test))

'''Do these two functions result in the same sorted lists?'''

def newSort(L):
    for i in range(len(L) - 1): #O(len(L))
        j=i+1
        while j < len(L):   #O(len(L))
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1
            
test = [1, 5, 3, 8, 4, 9, 6, 2]
print(newSort(test))   

'''
Yes, both selSort and newSort correctly sort a list.

selSort:

You can sort a list by always moving the smallest element from the unsorted
 list to a new list. That procedure would add the elements to the new list in
 increasing order, and when every element from the old list has been moved over,
 we end up with a new sorted list. This type of sorting algorithm is often
 called Selection Sort.

selSort implements this without explicitly creating a new list, by maintaining 
sorted (from position 0 to i-1) and unsorted (from position i to the end) parts
 of the list. All elements in positions before the iterating variable i are 
 sorted, and unsorted for those positions at i or below. In each iteration,
 it selects the smallest element in the unsorted part of the list, and swaps
 it with the element at the ith position. That essentially adds the next
 smallest element from the old list and appends it to the new. It keeps doing
 that until the old list is empty (i.e., i reaches the end of the list).

newSort:

newSort is basically a slight variant of Selection Sort. In each iteration,
 newSort also tries to find the smallest element in the unsorted part of the
 list and appends it to the sorted part of the list. The only difference here
 is that instead of finding the smallest value in the unsorted part of the list
 with minVal and minIndx, newSort maintains that the element at the ith position
 is the smallest element between the ith and jth positions. So, when j reaches
 the end of the list, the ith position must have been the smallest element in
 the unsorted portion (from position i to the end) of the list 

Do these two functions execute the same number of assignments of values into 
entries of the lists?        

selSort only does one "swap" each iteration of i, but newSort may use up
 to (n-i) "swaps" for each iteration of i.
 
 
Is the worst-case order of growth of these functions the same?
Yes.

In selSort, i iterates over each element of the list, and j checks between 1
 and up to n-i elements. That's n iterations for i, and for each i, we are 
 looking for the smallest element by checking about n/2 elements on average.
 That's kind of like n * n/2 checks, which is O(n^2). newSort does the same thing as
 selSort, except that selSort just updates temporary variables minIndx and
 minVal, but newSort updates the ith element instead. So, it also ends up with
  complexity.'''