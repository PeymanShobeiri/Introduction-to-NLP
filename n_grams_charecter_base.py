#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
N-Gram modeling :
    This is a model that can predict the next charecter of a input sentence. 
    In this model we construct the charecter grams model. Keep in mind that n-grams model uses a window and shift 
    this window by one in order to create the list of possibilities.

@author: Peyman
"""

import random 

text = """Dinosaurs are a group of reptiles that have lived on Earth for about 245 million years.
 Modern birds are a kind of dinosaur because they share a common ancestor with non-avian dinosaurs."""
 
# Declaring the size of n (the window)
n = 6

# Creating the n-grams model 
n_grams = {}

# due to the fact that we use a window with length of n, the stop condition for our loop need to be length of sentence - n
for i in range(len(text)-n):
    gram = text[i:i+n]  # text[0:3] -> the 3 itself is exclusive 
    # If gram is not in the dictionary create a list for it 
    if gram not in n_grams.keys():
        n_grams[gram] = []
    # In order to append the desirable charecter we use the index of i + length(window) 
    # text[0+3]-> o 
    n_grams[gram].append(text[i+n])

# Testing the n-grama model:
#   in order to do this we give the model a small part of sentence and it would create the hole sentence itself
CurrentGram = text[0:n]  # This is our initial sentence
result = CurrentGram
# Here 200 means that our maximum sentence length is 200 
for i in range(200):
    # If our sequence is not in the n_grams anymore we break and show the result
    if CurrentGram not in n_grams.keys():
        break
    # We choose a random charecter from the n_gram model
    possibilities = n_grams[CurrentGram]
    # randrange is a function that generate a random number within the specific scale 
    NextItem = possibilities[random.randrange(len(possibilities))]
    result += NextItem
    # We update the currentgram to the last three charecters
    CurrentGram = result[len(result)-n:len(result)]

print(result)