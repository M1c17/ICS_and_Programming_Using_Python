#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 21:00:50 2019

@author: MASTER
"""

#PLANNING FOR RETIREMENT
#intent to save an amount m each time 
#expect to earn a percentege r of income on investment each month 
#wanto to explore how big a retirement fund will be compound by time 
#ready to retire 
#compute compound interest
import pylab as plt

def retire(montly, rate, terms): #terms=months i want to compute over 
    savings = [0] #axis y
    base = [0]  #axis x
    mRate = rate/12
    for i in range(terms):
        base += [i]
        savings += [savings[-1]*(1 + mRate) + montly]
    return base, savings 

#how i visualize that?

def displayRetireWMonthlies(monthlies, rate, terms): #monthlies = list of amounts to set aside each month
    '''Display the different growths in retirement account
    as i change how much i put aside each month '''
    plt.figure('retireMonth')
    plt.clf() #clear frame so can reuse
    for montly in monthlies: #
        xvals, yvals = retire(montly, rate, terms)
        plt.plot(xvals, yvals,
                 label = 'retire:' + str(montly)) #informative label on each
        plt.legend(loc = 'upper left')
    
displayRetireWMonthlies([500, 600, 700, 800, 900, 1000, 1100], .05, 40*12) 

#what is the effect of rate of growth of investments?

def displayRetireWRates(month, rates, terms):
    plt.figure('retireRate')
    plt.clf() #clear frame so can reuse
    for rate in rates: #
        xvals, yvals = retire(month, rate, terms)
        plt.plot(xvals, yvals,
                 label = 'retire:' + str(month) + ':' + \
                 str(int(rate*100))) #informative label on each
        plt.legend(loc = 'upper left')
        
displayRetireWRates(800,[.03, .05, .07], 40*12)

#what if we look at both effect together?

def displayRetireWMonthsAndRate(monthlies, rates, terms):
    plt.figure('retireBoth')
    plt.clf()
    plt.xlim(30*12, 40*12)
    plt.xlabel('base')
    plt.ylabel('savings')
    for monthly in monthlies: #focus last stage of the fund
        for rate in rates:
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals,
                     label = 'retire:' + str(monthly) + ':' \
                     + str(int(rate*100)))
            plt.legend(loc = 'upper left')
            
#displayRetireWMonthsAndRate([500, 600, 700, 800, 900, 1000, 1100], [.03, .05, .07], 40*12)

#I cant distinguish because pf the overlap of the graphs

def displayRetireWMonthsAndRates(monthlies, rates, terms):
    plt.figure('retireBoth')
    plt.clf()
    plt.xlim(30*12, 40*12)
    monthLabels = ['r', 'b', 'g', 'k'] #create set of labels
    rateLabels = ['--', 'o', '-']
    for i in range(len(monthlies)):
        monthly = monthlies[i]
        monthLabel = monthLabels[i % len(monthLabels)] #pick new label for each month choice
        for j in range(len(rates)):
            rate = rates[j]
            rateLabel = rateLabels[j%len(rateLabels)] #pick new label for each rate choice
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals,
                     monthLabel+rateLabel,
                     label = 'retire:' + str(monthly) + ':' \
                             + str(int(rate*100)))
            plt.legend(loc = 'upper left')
            
displayRetireWMonthsAndRates([500, 600, 700, 800, 900, 1000, 1100], [.03, .05, .07], 40*12)
    
        