#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Bisection search - square root

guess = 0 
low = 1.0
high = x
ans = (high + low)/2.0      #Initialize a guess 

while abs(ans**2 -x) >= epsilon:
    print('low =' + str(low) +'high =' + str(high) +'ans=' + str(ans))
    guess +=1
    if ans**2 < x:
        low = ans 
    else:
        high = ans
    ans = (high  + low)/2.0
print('guesses=' + str(guess))
print(str(ans) + 'is close square root of:' + str(x))











