#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 13:16:26 2019

@author: MASTER
"""

#basic function plots two lists as x and y values
import pylab as plt

#first generate some example data

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

#generate some samples 
for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)
    
#to generate a plot, call 
#list need to be the same legth
#plt.figure('lin')
#plt.title('Linear')
#plt.xlabel('sample points')
#plt.ylabel('linear function')
#plt.clf()
#plt.ylim(0,1000)
#plt.plot(mySamples, myLinear)
#plt.figure('quad')
#plt.title('Quadratic')
#plt.clf()
#plt.ylim(0,1000)
#plt.xlabel('sample points')
#plt.plot(mySamples, myQuadratic)
#plt.figure('cube')
#plt.title('Cubic')
#plt.xlabel('sample points')
#plt.ylabel('cubic function')
#plt.plot(mySamples, myCubic)
#plt.figure('expo')
#plt.title('Exponential')
#plt.xlabel('sample points')
#plt.ylabel('expo function')
#plt.plot(mySamples, myExponential)
#plt.figure('quad')
#plt.ylabel('quad function')

'''OVERLAYING PLOTS'''
#plt.figure('lin quad')
#plt.clf()
#plt.subplot(211) #arg = #row, #colum & location to use
#plt.ylim(0,900)
#plt.plot(mySamples, myLinear, 'b-', label = 'linear', linewidth = 2.0)
#plt.subplot(212)
#plt.ylim(0,900) 
#plt.plot(mySamples, myQuadratic, 'ro', label = 'Quadratic', linewidth = 3.0)
#plt.legend(loc = 'upper left')
#plt.title('Linear  vs Quadratic')

plt.figure('cube exp log')
plt.clf()
plt.subplot(121)
plt.ylim(0, 140000)
plt.plot(mySamples, myCubic, 'g^', label = 'Cubic', linewidth = 4.0)
plt.subplot(122)
plt.ylim(0, 140000)
plt.plot(mySamples, myExponential, 'r--', label = 'Exponential', linewidth = 5.0)
#plt.yscale('log') # argument specifies type of scaling
plt.legend(loc = 10)
plt.suptitle('Cubic vs Exponential')


plt.figure('cube exp linear')
plt.clf()
plt.subplot(121)
plt.ylim(0, 140000)
plt.plot(mySamples, myCubic, 'g--', label = 'Cubic', linewidth = 4.0)
plt.subplot(122)
plt.ylim(0, 140000)
plt.plot(mySamples, myExponential, 'r--', label = 'Exponential', linewidth = 5.0)
#plt.yscale('log') # argument specifies type of scaling
plt.legend(loc = 10)
plt.suptitle('Cubic vs Exponential')


    
