#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TF-IDF model: This is an improved model of BOW in which the importance of each word is Distinguishable.
TF: Term Frequency
IDF: Inverse Document frecuency

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

for i in range(len(dataset)):
    dataset[i] = dataset[i].lower()
    dataset[i] = re.sub(r"\W", " ", dataset[i])
    dataset[i] = re.sub(r"\s+", " ", dataset[i])
    
# Creating the histogram
word2count = {}
for data in dataset:
    words = nltk.word_tokenize(data)
    for word in words:
        if word not in word2count.keys():
            word2count[word] = 1
        else: 
            word2count[word] += 1
            
# Finding the most frequent words
frequent_words = heapq.nlargest(80, word2count, key=word2count.get)

# Creating the IDF matrix
# Formula:
#    IDF = log ((Number of documents) / (Number of documents containing word))
# Note that in standard form we put a +1 in the log so it look like this :
#    IDF = log (((Number of documents) / (Number of documents containing word))+1)
words_IDFS = {}
for word in frequent_words:
    doc_count = 0
    for data in dataset:
        if word in nltk.word_tokenize(data):
            doc_count += 1
    words_IDFS[word] = np.log((len(dataset)/doc_count) + 1)

# creating the TF Martrix 
# Formula:
#    TF = (Number of occurences of a word in a document) / (Number of the words in that document)
# EX)
# " to be or not to be " --> TF for 'to' is = (1+1)/(6)
tf_matrix = {}
for word in frequent_words:
    # each word of frequent words is going to be checked in all sentences so :
    # doc_tf contained the tf of that word in all the sentences
    doc_tf = []
    for data in dataset:
        frequency = 0
        for w in nltk.word_tokenize(data):
            if w == word:
                frequency += 1
        tf_word = frequency/len(nltk.word_tokenize(data))
        doc_tf.append(tf_word)
    tf_matrix[word] = doc_tf

# TF_IDF calculation
# We need to multiple tf_matrix to IDF_matrix 
tfidf_matrix = []
for word in tf_matrix.keys():
    # tfidf is a vector that contain tfidf values of that word on each sentence
    tfidf = []
    for value in tf_matrix[word]:
        score = value * words_IDFS[word]
        tfidf.append(score)
    tfidf_matrix.append(tfidf)

# Now in order to convert tfidf_matrix to 2D array we use the following command
X = np.asarray(tfidf_matrix)

# The problem here is that the words are the rows and the columns are the sentences 
# so in order to make it more understandable we transport this matrix -> rows = sentences, columns = words
X = np.transpose(X)



