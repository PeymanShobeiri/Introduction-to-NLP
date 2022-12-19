#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extracting Parts-Of-Speech tags from a paragraph words

Meanings of the Parts-Of-Speech tags used in NLTK

CC     Coordinating conjunction

CD     Cardinal number

DT     Determiner

EX     Existential there

FW     Foreign word

IN     Preposition or subordinating conjunction

JJ     Adjective

JJR    Adjective, comparative

JJS    Adjective, superlative

LS     List item marker

MD     Modal

NN     Noun, singular or mass

NNS    Noun, plural

NNP    Proper noun, singular

NNPS   Proper noun, plural

PDT    Predeterminer

POS    Possessive ending

PRP    Personal pronoun

PRP$   Possessive pronoun

RB     Adverb

RBR    Adverb, comparative

RBS    Adverb, superlative

RP     Particle

SYM    Symbol

TO     to

UH     Interjection

VB     Verb, base form

VBD    Verb, past tense

VBG    Verb, gerund or present participle

VBN    Verb, past participle

VBP    Verb, non-3rd person singular present

VBZ    Verb, 3rd person singular present

WDT    Wh-determiner

WP     Wh-pronoun

WP$    Possessive wh-pronoun

WRB    Wh-adverb


@author: Peyman
"""

import nltk
 
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

words = nltk.word_tokenize(paragraph)

# nltk.pos_tag(list_of_words) -> extract each part of speech of a word in paragraph
tagged_words = nltk.pos_tag(words)

# Now in oreder to connect all two parts of the tuples into a one list and turn the list into a paragraph we use the following commands
word_tagged = []
for tu in tagged_words:
   word_tagged.append(tu[0] + "_" + tu[1]) 

# concating the words into a new paragraph
tagged_paragraph = " ".join(word_tagged)
    


