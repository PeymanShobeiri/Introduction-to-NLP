#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Word Nagation Tracking : 
    Nagation  -> not 
    so we know that not happy means unhappy but with our models we cannot detect this kind of words.
    in order to make it possible we can do one of the following:
        1) adding the _ between not and the adj         ex) not happy -> not_happy or sad
        2) changing the not happy to unhappy

@author: Peyman 
"""

import nltk

sentence = " I was not happy with my math results"


''' the first solution'''

words = nltk.wordpunct_tokenize(sentence)

new_words = []

tmp_words = ""

for word in words:
    if word == 'not':
        tmp_words = "not_"
    elif tmp_words == "not_":
        word = tmp_words + word  # creating not_happy
        tmp_words = ""  
    # so if the word is not_happy it would append it to the list
    if word != "not":
        new_words.append(word)
    
sentence = ' '.join(new_words)
print(sentence)
    

''' the second solution'''
import nltk
from nltk.corpus import wordnet

sentence = " I was not happy with my math results"

words = nltk.wordpunct_tokenize(sentence)

new_words = []

tmp_words = ""

for word in words:
    antonyms = []
    if word == 'not':
        tmp_words = "not_"
        
    elif tmp_words == "not_":
        for sys in wordnet.synsets(word): 
            # lemmas gets all the diffrent words in the synsets
            for s in sys.lemmas():
                # antonyms function see if there is any antonyms for that word or not
                for n in s.antonyms():
                    antonyms.append(n.name())
        # check to see if the word have any antonyms
        if len(antonyms) >= 1 :
            word = antonyms[0]
        # if not we use the first approach
        else:
            word = tmp_words + word
            
        tmp_words = ""  
    # so if the word is not_happy it would append it to the list
    if word != "not":
        new_words.append(word)
    
sentence = ' '.join(new_words)
print(sentence)