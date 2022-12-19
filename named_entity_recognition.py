#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
named entity recognition with nltk
    - organization
    - person
    - location
    - date
    - time
    - money
    - percent
    - facility such as Washington Monument
    - GPE such as South East Asia

@author: Peyman
"""

import nltk

paragraph = " The Taj Mahal was built by Emperor Shah Jahan"

# Seprate the words in the paragraph 
words = nltk.word_tokenize(paragraph)

# Tagged the words with pos_tag
tagged_words = nltk.pos_tag(words)

# Recognition of named entities
namedEnt = nltk.ne_chunk(tagged_words)

# Due to the fact that variable explorer cannot show this tree, we use draw method
namedEnt.draw()