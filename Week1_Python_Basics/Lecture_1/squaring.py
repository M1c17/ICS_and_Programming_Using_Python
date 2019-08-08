#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# squaring by repetitive addition

x = 3  
ans = 0   
itersleft = x  
while (itersleft != 0): 
    ans += x        
    itersleft -=1
print(str(x) + '*' + str(x) + '=' + str(ans))