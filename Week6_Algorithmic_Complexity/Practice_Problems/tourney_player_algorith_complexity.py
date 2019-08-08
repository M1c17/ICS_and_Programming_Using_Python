#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 17:46:26 2019

@author: MASTER
"""

#6.00.1x staff decide to hold an online chess tournament, and n 6.00.1x students
# respond to participate in it. If the tournament is a single-elimination tournament
# (this means you are eliminated when you lose once), how many games do we need to
# decide the winner, in terms of n? Assume there will be no draws or byes

#HOW MANY GAMES DO WE NEED?

games = 0 
players = 2 ** 5 
gamesInRound = 0
print(str(players) + " players left after " + str(gamesInRound) + " games. " + "Total games played: " + str(games))

while players > 1:
    games += players / 2
    gamesInRound = players / 2
    players = players / 2
    print(str(players) + "player left after" + str(gamesInRound) + " games. " + "Total games played: " + str(games))


