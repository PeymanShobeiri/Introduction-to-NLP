#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Latent Semantic Analysis  (LSA)

@author: Peyman
"""

# importing the librarys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
import nltk

# A simple dataset 
dataset = ["the amount of polution is increasing day by day ",
           "the concert was just great",
           "I love to see Gordon Ramsay cook",
           "Apple is introducing a new technologhy",
           "AI Robats are examples of great technology present today",
           "All of us were singing in the concert",
           "We have launch companigns to stop polution and global warming"
           ]

# lowering all the charecters in the dataset
dataset = [line.lower() for line in dataset]

# Creating an instanse of TfidfVectorizer in order to convert the dataset into TF_IDF model
vectorizer = TfidfVectorizer()
x = vectorizer.fit_transform(dataset)

# Here x[0] means the first sentence
# Note that you will see something such as:   (0,6) 0.34112  
# 0 here declare the document number, 6 indicate the place of the word in the tf_idf model 
# and finally the float number indicates the TF_IDF value
print(x[0])

# In order to decompose the x matrix to the 3 matrix of LSA we use the TruncatedSVD library
# Here n_components  is the components number that you desire to have
# n_iter is the number of iterations that make our model more accurate when it gets higher but here 100 seems ok
lsa = TruncatedSVD(n_components=4, n_iter=100)
lsa.fit(x)

# row1 contain values for first document
# in this matrix rows are the words and columns are the documents number 
row1 = lsa.components_[0]

# getting the names which are in the tf-idf model (the 42 words that are the rows in the lsa matrix)
terms = vectorizer.get_feature_names()

concept_words = {}

# i is the document number and the comp is the values of tf-idf model for that particular document
for i,comp in enumerate(lsa.components_):
    # The zip function create tuples that the first one of them is the word and the second one is the value for that word in the tf-idf model
    componentTerms = zip(terms,comp)
    # The sort function sort the list base on their values in tf-idf model becuase its dcs we reverse it 
    sortedTerms = sorted(componentTerms, key=lambda x : x[1], reverse=True)
    # due to the fact that we do not need all of the words we reduce them to top 10
    sortedTerms = sortedTerms[:10]
    # if we print the results we can determine the consepts :) 
    # print("\n Concept", i, ":")
    # for term in sortedTerms:
    #     print(term)
    # but in order to mechanize even this job we do the following strategy: 
    concept_words["concept"+str(i)] = sortedTerms
        
# Now, concept_word contain 4 concepts and each concept contain the words relating to them
# So now in order to check it we check this concept with our dataset
# in order to do that we tokenize the words in the sentences and then assign a score base on the relativity of them to each concept

for key in concept_words.keys():
    sentence_scores = []
    for sentence in dataset:
        words = nltk.word_tokenize(sentence)
        score = 0
        for word in words:
            for word_with_score in concept_words[key]:
                if word == word_with_score[0]:
                    score += word_with_score[1]
        sentence_scores.append(score)
    print("\n" + key + ":")
    for snt in sentence_scores:
        print(snt)

# if the accuracy is low it is becuase our dataset contain few sentences if we 
# increase the sentence numbers our accuracy will gets better 



















