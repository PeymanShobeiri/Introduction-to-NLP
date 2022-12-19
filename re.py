#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
the basics of regular expresions
@author: Peyman
"""

import re 

sen = "I was born in 2001"

# match check only the first portion of the sentence
# this return any or 0 charectures
print(re.match(r".*", sen))

# this return one or more than 1 charectures
print(re.match(r".+", sen))

# matches the charectures from a to z and A to Z 
print(re.match(r"[a-zA-Z]*", sen))

# matches the sequens that start with a and contain 0 or 1 b (abb -> ab) 
print(re.match(r"ab?", sen))

# starts with -> use match because it cheack the first part 
sen2 = "2001 was the year that I was born"
print(re.match(r"^2001", sen2))

# re.search -> search globaly and return the first match 
# Ends with -> use search method + $ sign
print(re.search(r"born$", sen2))

# We can use this syntaxs in IF statements
if re.search(r"born$", sen2):
    print("matched")
else:
    print("not matched")
    
# re.sub search globaly and replace globaly -> replace more than one in the sentence
sen3 = "my name is peyman peyman"
print(re.sub(r"peyman", "behnam", sen3))

# We can identify flags for re.sub -> re.I means case insensetive
sen4 = "I love Batman"
print(re.sub(r"[a-z]", "0", sen4, flags=re.I))

# We can simply declare the number of charectures that we want to change
print(re.sub(r"[a-z]", "0", sen4, 3, flags=re.I))

# More examples for re.sub
sentence1 = "Wellcome to the year 2023"
sentence2 = "Just ++--%%  ~@...@@ --- arrived at NY airport. We stay in jack's place #fun"
sentence3 = "I                  Love                    you"

# Note that \d means any digits
sen1_modified = re.sub(r"\d", "", sentence1)
# Keep in mind that '-' have a special meaning which means range +-# means that Ascci codes from + to # 
# In order to evade this we need to use \-
sen2_modified = re.sub(r"[@#%~+\-\.\'']", "", sentence2)

# \w means : a-z + A-Z + 0-9
sen2_modified = re.sub(r"\w", "", sentence2) # so only wired charecters remain

# \W means : all this wired charecters -> @#$%...(note it gets ride of spaces too!)
sen2_modified = re.sub(r"\W", " ", sentence2)
# Now, in order to remove redondant spaces we use the following command next
# Keep in mind that, \s means spaces \s+ means a sequence of spaces more than 1 
sen2_modified = re.sub(r"\s+", " ", sen2_modified)

# In order to eliminate the sigle charecters such as s in jack s place we use the following command:
# Template : space + charecter + space
# We use \s+ in order to eliminate all spaces in case of situations that we want to summerize the two commands together
sen2_modified = re.sub(r"\s+[a-zA-Z]\s+", " ", sen2_modified)

# In order to remove all spaces from both sides we use a sigle \s+
sen3_modified = re.sub(r"\s+", " ", sentence3)

# Example:
X = ["This is a wolf #scary",
     "Wellcome to the jungle #missing",
     "11322 the nimber to know",
     "Remmeber the name s - John",
     "I      love          you "]

for i in range(len(X)):
    X[i] = re.sub(r"\W", " ", X[i])
    X[i] = re.sub(r"\d", " ", X[i])
    X[i] = re.sub(r"\s+[a-zA-Z]\s+", " ", X[i])
    # Now we have a lot of spaces so:
    X[i] = re.sub(r"\s+", " ", X[i])
    # If a sentence is started or ended by space we need to remove those too
    X[i] = re.sub(r"^\s", "", X[i])
    X[i] = re.sub(r"\s$" ,"", X[i])









