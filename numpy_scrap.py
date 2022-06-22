"""
NumPy tutorial

https://www.youtube.com/watch?v=8JfDAm9y_7s
"""

from tkinter import _XYScrollCommand
import numpy as np

import time, sys


# Numpy vs List

SIZE = 1000000

L1 = range(SIZE)
L2 = range(SIZE)

A1 = np.arange(SIZE)
A2 = np.arange(SIZE)

start = time.time()

result = [(x,y) for x,y in zip(L1, L2)]

print((time.time()-start)* 1000)

start = time.time()

result = A1 + A2

print((time.time()-start)* 1000)    # numpy array takes less time than lists 

# Numpy operations 

# find the dimension of the array
# find the byte size of each element
# fin the data types of the elements

a = np.array([(1,2,3), (2,3,4)])

print(a.ndim)   # two dimensional array | a = np.array([(1,2,3), (2,3,4)])

a = np.array([1,2,3])

print(a.itemsize)
print(a.dtype)

# find the size of an array
# find the shape of an array

a = np.array([1,2,3,4,5])

print(a.size)   # size of 5

a = np.array([(1,2,3), 
              (4,5,6),
              (9,8,7)])

print(a.shape)

# Reshape
# Slicing

a = np.array([(1,2,3), (3,4,5)])

a = a.reshape(3,2)

print(a)

a = np.array([(1,2,3), (3,4,5)])

print(a[0, 2])  # from the zero element, i want the index 2

print(a[0:,2])  # all the rows but just the index 2 -> which is 3 and 5.

a = np.array([(1,2,3), (4,5,6), (7,8,9)])

print(a[0:2, 2])

a = np.linspace(1,3,1000)  # pretty cool, 1000 values evenly spaced between 1 and 3

print(a)    # how you perform linespacing 


# min, max, sum

a = np.array([1,2,3])

print(a.max())
print(a.min())
print(a.sum())

# axis concept

# axis 0 is the columns, axis 1 is rows

a = np.array([(1,2,3), (4,5,6)])

print(a.sum(axis=0))    # you have done this by HAND in linear algebra
print(a.sum(axis=1))

# Math functions 

# find the sq root 
# find the standard deviation 

a = np.array([(1,2,3), (4,5,6)])

print(np.sqrt(a))
print(np.std(a))

# Matrix add, sub, mult, div

a = np.array([(1,2,3), (3,4,5)])
b = np.array([(1,2,3), (3,4,5)])

print(a+b)  # when you are using lists, it concatenates the items. NumPy uses matrix add <3
print(a-b)

print(a/b)
print(a*b)

# Stacking

# vertical

print(np.vstack((a,b)))

# horizontal

print(np.hstack((a,b)))

# single column

print(a.ravel()) # single line

# NumPy special functions! 

# cosine function
# sine function

import matplotlib.pyplot as plt

x = np.arange(0,3*np.pi, 0.1)

y = np.sin(x)
# y = np.cos(x)
# y = np.tan(x)

plt.plot(x,y)

plt.show()

# exponential
# logarithmic

ar = np.array([1,2,3])

print(np.exp(ar))
print(np.log(ar))    # natural log or log base e
print(np.log10(ar))