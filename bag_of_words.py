#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bulding the bag of word (BOW) model -> shows each word appears how many times in the paragraph 

@author: Peyman
"""

import nltk
import re
import heapq
import numpy as np

paragraph = """I know to do what we do, you gotta be able to take abuse, and you gotta be able to have people talk crazy about you. In this business, you gotta be able to have people disrespecting you and you gotta smile and you gotta pretend like that‘s OK.

But Richard Williams, and what I loved, thank you D. Denzel (Washington) said to me a few minutes ago, he said, “At your highest moment, be careful. That’s when the devil comes for you.”

It’s like I want to be a vessel for love. I want to say thank you to Venus and Serena.

I just spit, I hope they didn’t see that.

I want to say thank you to Venus and Serena and the entire Williams family for entrusting me with your story. That’s what I want to do. I want to be an ambassador of that kind of love and care and concern.

I want to apologize to the Academy, I want to apologize to all my fellow nominees.

This is a beautiful moment and I’m not crying for winning an award. It’s not about winning an award for me. It’s about being able to shine a light on all of the people. Tim and Trevor and Zach and Saniyya and Demi and Aunjunue and the entire cast and crew of “King Richard” and Venus and Serena and the entire Williams family.

Art imitates life. I look like the crazy father, just like they said. I look like the crazy father just like they said about Richard Williams. But love will make you do crazy things.

To my mother. Um, a lot of this moment is really complicated for me, but to my mother. She didn’t want to come out. She had her knitting friends, she has a knitting crew watching with her. Being able to love and care for my mother, my family, my wife.

I’m taking up too much time. Thank you for this honor, thank you for this moment. I thank you on behalf of Richard and Oracene, the entire Williams family. Thank you. I’m hoping the Academy invites me back. Thank you."""


dataset = nltk.sent_tokenize(paragraph)

# pre_prossesing 
for i in range(len(dataset)):
    # we change all character to lower as a first alteration
    dataset[i] = dataset[i].lower()
    # we change the non_character items to space
    dataset[i] = re.sub(r"\W", ' ', dataset[i])
    # Now we most diminish all the redundant spaces
    dataset[i] = re.sub(r"\s+", " ", dataset[i])
    
# Creating the Histogram
# Historgram shows the number of appearance of words in paragraph
word2count = {}
for data in dataset:
    words = nltk.word_tokenize(data)
    for word in words:
        if word not in word2count.keys():
            word2count[word] = 1
        else:
            word2count[word] += 1
            
# Filtering the most frequent once
# In order to find the n largest items we use nlargest method in which the first
# parameter is the n, the second one is the dictionary and the last one is a function
# tthat will be use in order to make the comparison

# EX)
# Define a function that returns a comparison key for city objects

# def sortkey(city):
#     return city.population
# mostPopulated = heapq.nlargest(3, cities, key = sortkey)

# The get() method returns the value of the item with the specified key.
frequent_words = heapq.nlargest(70, word2count, key=word2count.get)

# Now in order to create the BOW we need to check which of the frequent words is present
# in each sentence. We do this by createing a 2D matrix in which rows are sentences_NO and 
# the columns are the frequent words. Note that 1 means the word is present in the sentence and 0 
# means that word is not present there.
X = []
for data in dataset:
    vector = []
    for word in frequent_words:
        if word in nltk.word_tokenize(data):
            vector.append(1)
        else:
            vector.append(0)
    # Now we need to append a vector like [0,1,0,0,1] to our main array which is X
    X.append(vector)
# Right now, X is a list of list so in order to convert it to a array we use numpy library
X = np.asarray(X)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    