#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
N-Gram modeling word version : (auto text generator)
    This is a model that can predict the next word of a input sentence. 
    In this model we construct the word grams model. Keep in mind that n-grams model uses a window and shift 
    this window by one in order to create the list of possibilities.

@author: Peyman
"""
import random 
import nltk

text = """Dinosaurs are a group of reptiles that have lived on Earth for about 245 million years.
 Modern birds are a kind of dinosaur because they share a common ancestor with non-avian dinosaurs."""
 
n = 3

words = nltk.word_tokenize(text)

n_grams = {}

# Creating the n-grams model
for i in range(len(words)-n):
    # Here instead of charecters we have words so we need to join them in order to create the n_grams dictionary
    gram = ' '.join(words[i:i+n])
    if gram not in n_grams.keys():
        n_grams[gram] = []
    n_grams[gram].append(words[i+n])

# Testing the n_grams model 
currentgram = ' '.join(words[0:n])
result = currentgram
# the number in the range shows the maximum number of words in the sentence
for i in range(40):
    if currentgram not in n_grams.keys():
        break
    possibilities = n_grams[currentgram]
    NextItem = possibilities[random.randrange(len(possibilities))]
    # We need to put a ' ' because it is what seperates the words from each other 
    result += ' '+NextItem
    rwords = nltk.word_tokenize(result)
    currentgram = ' '.join(rwords[len(rwords)-n:len(rwords)])

print(result)