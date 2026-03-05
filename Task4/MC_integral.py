#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

# User can put values and functions in
function = input(f"Input a function for which you want to calculate the integral: ")
a = float(input(f"Give a lower bound: "))
b = float(input(f"Give a upper bound: "))
n = int(input(f"Give amount of random numbers: "))

# Generates random numbers uniformly        
x_random = np.random.uniform(a, b, n)

# Evaluates the function for every random generated value and sums them after
p = [eval(function) for x in x_random]
sum_ = sum(p)

# Calculates the integral
integral = ((b - a) / n) * sum_
print(f"The answer of the integral is: {integral}")

