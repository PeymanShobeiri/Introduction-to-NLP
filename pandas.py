#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
introduction to pandas

@author: Peyman
"""

import numpy as np
import pandas as ps

# Series -> core of pandas structure -> like lists but stronger
x = ps.Series([1,2,3,4,5])

# all elements operate with the specific operation
x + 100
(x ** 2) + 100

# we can use > or < or etc operations on series -> works on all items 
x > 2

# any , all
larger_than_2 = x >2

# any return true if there is at lest one true in the series
larger_than_2.any()
# all return true if all elements are true 
larger_than_2.all()

# apply -> apply a function on all elements of a series
def f(x):
    if x % 2 == 0:
        return x ** 2
    else:
        return x ** 3

x.apply(f)

# converting types -> astype(type_name) -> types are in np libarary
x.astype(np.float64)

# copy method 
x
y = x
# because x and y point to the same series, by changing x, y get chanded too 
y[0] = 100
# in order to avode this problem we can use copy method
x = ps.Series([1,2,3,4,5])
y = x.copy()
y[0] = 100


# DataFrame -> it is mainly like sql tables
data = [1,2,3,4,5]
# Here we create a dataframe and we named the column x
df = ps.DataFrame(data, columns=["x"])

# each column is a series
data_series = df["x"]

# Adding columns to dataframe
df["x_plus_2"] = df["x"] + 2
df["x_square"] = df["x"] ** 2
df["x_factorial"] = df["x"].apply(np.math.factorial)
df["is_even"] = df["x"] % 2

# Dropping/Deleting a columns -> drop(name_of_column, axis)
df = df.drop("is_even", 1)

# Selecting ,ultiple columns
df[["x","x_factorial"]]

# Describing -> show a lot of info about each columns such as count, mean, min, max, ...
df.describe()

# Reading database -> import a dataset in pandas -> your csv file must be in the same file
dataset = pd.read_csv("score.csv")

