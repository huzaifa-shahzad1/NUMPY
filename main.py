import string
import random

import numpy as np

# 1-D NUMPY ARRAY  -- vector
a = np.array([1, 2, 3])
print(a)

# 2-D NUMPY ARRAY  -- matrix
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

# 3-D NUMPY ARRAY  -- tenser
c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(c)

# ARRAY OF DESIRED DATA-TYPE
d = np.array([1, 2, 3], dtype=float)
print(d)

# A-RANGE FUNCTION  -- takes 2 parameters -> first one is included, other is excluded
f = np.arange(1, 11, 2)  # third parameter is to take jump between numbers
print(f)

# RESHAPE AN EXISTING ARRAY
g = np.arange(1, 11).reshape(5, 2)  # product of row-column should be equal to the number of items
print(g)

# initialize an array with one or zero
h = np.ones((3, 2))
print(h)
h = np.zeros((3, 2))
print(h)

# initialize an array with random numbers between one and zero
i = np.random.random((2, 3))
print(i)

# initialize an array in a given range with equally spaced points
j = np.linspace(-20, 20, 10)  # first para -> lower-range | second para -> upper-range | third para -> num of points
print(j)

# create an array of identity matrix
k = np.identity(3)  # parameter -> num of rows * columns
print(k)
