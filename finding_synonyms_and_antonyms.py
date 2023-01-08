#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Finding synonyms and antonyms of words 

@author: Peyman
"""
from nltk.corpus import wordnet

synonyms = []
antonyms = []

# The wordnet.synsets return all the synsets of declared word
for sys in wordnet.synsets("hurt"): 
    # lemmas gets all the diffrent words in the synsets
    for s in sys.lemmas():
        # s.name gets the words and do not append the ',' tags, etc.
        synonyms.append(s.name())
        # antonyms function see if there is any antonyms for that word or not
        for n in s.antonyms():
            antonyms.append(n.name())
    
# due to the fact that we have redundant words in the list we use set to provide repetition
print(set(synonyms))
print(set(antonyms))