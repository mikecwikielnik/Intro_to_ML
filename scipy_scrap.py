"""
SciPy

https://www.youtube.com/watch?v=k8s-R3csOt0
"""

# Basic functions

# help(): returns info about any function, keyword, class, etc
# info(): returns info about any function, keyword, class, etc
# source(): returns the source code only for objects written in Python

from scipy import cluster

help(cluster)

help()

import scipy 
scipy.info(cluster)

scipy.source(cluster)   # remember you have to import these subpackages directly

# Special functions 

# exponential functions
# trig functions 

from scipy import special

a = special.exp10(2)
print(a)

b = special.exp2(3)
print(b)

c = special.sindg(90)
print(c)

d = special.cosdg(35)
print(d)

# Integration functions 

# general integration 
# double integraton 

# quad function calculates the integral of a function which has one variable
# dblquad function calculates double integral of a function which has two variables 

from scipy import integrate

help(integrate.quad)

i = scipy.integrate.quad(lambda x: special.exp10(x), 0,1)
print(i)


e = lambda x,y: x*y**2
f = lambda x: 1
g = lambda x: -1
integrate.dblquad(e,0,2,f,g)

# Fourier Transformations 

from scipy.fftpack import fft, ifft
import numpy as np

x = np.array([1,2,3,4])
y = fft(x)
print(y)

# inverse 

x = np.array([1,2,3,4])
y = ifft(x)
print(y)

# Linear Algebra

from scipy import linalg

a= np.array([[1,2], [3,4]])
b = linalg.inv(a)
print(b)    # this is the best. You calculated the inverse of a matrix 

# Interpolation functions 

import matplotlib.pyplot as plt
from scipy import interpolate

x = np.arange(5, 20)
y = np.exp(x/3.0)
f = interpolate.interp1d(x, y)
x1 = np.arange(6, 12)
y1 = f(x1)
plt.plot(x, y, 'o', x1, y1, '--')
plt.show()