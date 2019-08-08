#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = int(input('Enter an integer: '))
ans = 0

while ans ** 3 < abs(x):        #loop generate gueses  
    ans += 1 
if ans ** 3 != abs(x):     #test and check
    print(str(x) , 'is not a perfect cube root')
else:
    if x < 0:
        ans -= ans
        print('cube root of ', x, 'is', ans)
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    