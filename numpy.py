#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The introduction of numpy library

@author: Peyman
"""

import numpy as np

# arange() -> np.arange([start], stop, [step], [dtype=None])
# arange generate array as requested
np.arange(10)
# declare starting point
np.arange(1,10)
# declare steps
np.arange(1,10,2)
np.arange(1,10,0.5)

np.arange(1,10,dtype='float64')

# Examining the np.array
arr = np.arange(1,10)

# return the number of dimentions in array -> it is not callable
arr.ndim

# Number of elements in the array
arr.shape

# return the size of array
arr.size

# return the type of elements in the array
arr.dtype

# return the size of each element in the array
arr.itemsize

# calculate the memory usage
arr.itemsize * arr.size

# %timeit is used to calculate the time
# comparing the np vs normal
# %timeit list1 = range(1,1000)
# %timeit list2 = np.arange(1,1000)

# Important functions in numpy
# List to array
np.asarray([1,2,3,4,5])

# The same goes for 2D arrays
list2d = [[1,2,3],[4,5,6]]
arr2d = np.asarray(list2d)

# Generating zeros -> np.zeros(shape, dtype=float)
listzeros = np.zeros((3,4), dtype='int32')

# linspace function generate num number of items in range of start to stop
# num is the number of items that we want to generate
# If endpoint is false it means that the stop itself is excluded 
# np.linspace (start, stop, num=50, [endpoint=True])
np.linspace(1,4,num=4)
np.linspace(1,4,num=8)
np.linspace(1,4,num=8,endpoint=False)

# np.random.random(size) -> generate a matrix with a required size
# For size -> (rows, columns)
np.random.random((3,4))

# min, max, median in np.arrays
rarr = np.random.random((3,4))

# np.max(array_name, axis=None)
# If axis is 0 -> finding the max on columns
np.max(rarr, axis=0)

# If axis is 1 -> finding the max on rows
np.max(rarr, axis=1)

# If you do not declare the axis it would found the max of hole matrix
np.max(rarr)

# If axis was not declared -> it would find the max of hole matrix
# The same goes for min, median, mean, sum
np.min(rarr, axis=0)
np.min(rarr, axis=1)
np.min(rarr)

np.median(rarr, axis=0)
np.median(rarr, axis=1)
np.median(rarr)

# Slicing
rarr = np.random.random((4,5))

# : means all rows and all columns
rarr[:,:]

# rows 1 and 2 + all columns
rarr[1:3,:]

# all rows + all columns first one excluded
rarr[:,1:]
rarr[:,1:3]
rarr[1:3,1:3]

# rows 0 and 3 + all columns and vise versa
rarr[[0,3],:]
rarr[:,[0,3]]

# all rows except last one + all columns
rarr[:-1,:]
rarr[:,:-1]

# this means from last one to end of the matrix + all columns
rarr[-1:,:]
rarr[-2:,:]









