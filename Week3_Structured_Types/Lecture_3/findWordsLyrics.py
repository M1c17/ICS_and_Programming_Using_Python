#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 14:24:51 2019

@author: MASTER
"""

# ANALYZE SONG LYRICS
# I WANT TO SEE HOW OFTEN DOES A WORD APPEAR IN A LYRIC 

# 1) CREATE A FREQUENCY DICTIONARY  MAPPING STR : INT
#GIVING SET OF LYRICS FOR A SONG COUNT 
#HOW MANY TIMES APPEAR INSIDE OF THAT LYRICS 
# 2)  FIND THE WORD THAT OCCURS THE MOST OFTEN & HOW MANY TIMES IT DOES THAT
# USE LIST, IN CASE THERE IS MORE THAN ONE WORD THAT OCCURS THE SAME NUMBERS
#OF TIMES
# RETURN A TUPLE THAT HAS INSIDE OF IT A LIST FOR THE SET OF WORDS 
#& AN INTEGER FOR HOW OFTEN DID THAT SET OF WORDS, EACH ONE OF THEM, APPEAR 
#INSIDE THE LYRICS 
# 3) FIND THE WORDS THAT OCCURS AT LEAST SOME NUMBERS OF TIMES 
#LET USER CHOOSE MINUMUN AMOUNT, SO IT WILL BE A PARAMETER 
# RETURN A LIST OF TUPLES, EACH TUPLE IS A (LIST, INT)
#CONTAINING THE LIST OF WORDS ORDERED BY THEIR FREQUENCY 

#IDEA: FROM SONG DICTIONARY: FIND THE MOST FREQUENT WORD, DELETE MOST COMMON
# WORD.REPEAT. IT WORKS BECAUSE YOU ARE MUTATING THE SONG DICTIONARY 


'''1) CREATE A FREQUENCY DICTIONARY  MAPPING STR : INT'''
def lyrics_to_frequencies(lyrics): #lyrics string of words 
    myDict = {}
    for word in lyrics: #iterate over the list getting each word out as i do it 
        if word in myDict: #can iterate over keys in dictionary 
            myDict[word] += 1 # update value associated with key 
            #count word if the word already in myDict 
        else:
            myDict[word] = 1 # set the value in myDict if i found the word for first time
    return myDict 


she_loves_you = ['she','loves','you','yeah','yeah','yeah',
                 'she','loves','you','yeah','yeah','yeah',
                 'she','loves','you','yeah','yeah','yeah',
                 
                 'you','think',"you've",'lost','your','love',
                 'well','i','saw','her','yesterday-yi-yay',
                 "it's",'you',"she's",'thinking','of',
                 'and','she','told','me','what','to','say-yi-yay',
                 
                 'she','says','she','loves','you',
                 'and','you','know','that',"can't",'be','bad',
                 'yes','she','loves','you',
                 'and','you','know','you','should','be','glad',
                 
                 'she','said','you','hurt','her','so',
                 'she','almost','lost','her','mind',
                 'and','now','she','says','she','knows',
                 "you're",'not','the','hurting','kind',
                 
                 'she','says','she','loves','you',
                 'and','you','know','that',"can't",'be','bad',
                 'yes','she','loves','you',
                 'and','you','know','you','should','be','glad',
                 
                 'oo','she','loves','you','yeah','yeah','yeah',
                 'she','loves','you','yeah','yeah','yeah',
                 'with','a','love','like','that',
                 'you','know','you','should','be','glad',
                 
                 'you','know',"it's",'up','to','you',
                 'i','think',"it's",'only','fair',
                 'pride','can','hurt','you','too',
                 'pologize','to','her',
                 
                 'Because','she','loves','you',
                 'and','you','know','that',"can't",'be','bad',
                 'Yes','she','loves','you',
                 'and','you','know','you','should','be','glad',
                 
                 'oo','she','loves','you','yeah','yeah','yeah',
                 'she','loves','you','yeah','yeah','yeah',
                 'with','a','love','like','that',
                 'you','know','you','should','be','glad',
                 'with','a','love','like','that',
                 'you','know','you','should','be','glad',
                 'with','a','love','like','that',
                 'you','know','you','should','be','glad',
                 'yeah','yeah','yeah',
                 'yeah','yeah','yeah','yeah'
                 ]


beatles = lyrics_to_frequencies(she_loves_you)
'''2)  FIND THE WORD THAT OCCURS THE MOST OFTEN & HOW MANY TIMES IT DOES THAT'''
   
def most_common_words(freqs):
    values = freqs.values() #gives me back a set of values all ints 
    best = max(values) # now that i know the best 
    words = [] # find al the words that have that value 
    for k in freqs:# for element in the dictionary iterate over keys in dictionary
        if freqs[k] == best:
            words.append(k)
    return(words, best)
    
(w, b) = most_common_words(beatles)

'''# 3) FIND THE WORDS THAT OCCURS AT LEAST SOME NUMBERS OF TIMES'''

def words_often(freqs, minTimes):
    result = []
    done = False # create flag 
    while not done:
        temp = most_common_words(freqs)#find the most common words in the dictionary
        if temp[1] >= minTimes: #if they occur more than the minimum number of times
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
#        if len(freqs) == 0:
#            done = True
        else:
            done = True
    return result 
    

print(words_often(beatles, 5))
            







        