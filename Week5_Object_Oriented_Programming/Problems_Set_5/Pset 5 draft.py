#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 08:59:37 2019

@author: MASTER
"""
'''Problem 1 - Build the Shift Dictionary and Apply Shift'''

import string 

shift = 25
lower_keys = list(string.ascii_lowercase)
lower_values = list(string.ascii_lowercase)
shift_lower_values = lower_values[shift:] + lower_values[:shift]
        
upper_keys = list(string.ascii_uppercase)                 
upper_values = list(string.ascii_uppercase)
upper_shift_values = upper_values[shift:] + upper_values[:shift]

full_keys = lower_keys + upper_keys
full_values = shift_lower_values + upper_shift_values

shift_dict = dict(zip(full_keys, full_values))

        
print(shift_dict)

#ONE LINE 

#from string import ascii_lowercase as a
#s = 3
##a = 'abcdefghijklmnopqrstuvwxyz'
#A = a.upper()
#print(dict(zip(a + A, a[s:]+ a[:s] + A[s:]+ A[:s])))

message = 'banana90?.!'
new_string = []
for c in message:
    if c in shift_dict:
        message = shift_dict[c]
        new_string.append(message)
    else:
        new_string.append(c)
        
print(''.join(new_string))
   
#message = 'banana,9'
#new_str = []
#
#for c in message:
#    if c not in shift_dict:
#        new_str.append(c)
#        #the loop start next iteration without executing the remaining
#        continue
#    else:
#        new_str.append(shift_dict[c])
#print(''.join(new_str))    

'''
Problem 2 - PlaintextMessage'''

#Our class will always create an encoded version of the message, 
#and will have methods for changing the encoding
#input shift 
#class PlaintextMessage(Message):
#    def __init__(self, text, shift):
#        Message.__init__(self, text)
#        self.shift = shift
#        self.encrypting_dict = Message.build_shift_dict(self, self.shift)
#        self.message_text_encrypted = Message.apply_shift(self, self.shift)
#        
#    def change_shift(self, new_shift):
#
#        self.shift = new_shift
#        #update other attributes
#        self.encrypting_dict = (Message.build_shift_dict(self, self.shift)).copy()
#        self.message_text_encrypted = Message.apply_shift(self, self.shift)
#        
##        return self.message_text_encrypted #Test
#
##p2 = PlaintextMessage("9,?banana", 2) #Test
##print(p2.change_shift(4))         #Test


'''Problem 3 - CiphertextMessage'''

#write a program that tries each shift and maximizes the number of English 
#words in the decoded message, we can decrypt their cipher!

#if most of the words obtained after a shift are valid words
