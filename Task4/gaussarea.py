#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
from math import pi

# User input
A = float(input(f"Input your value for A: "))
x0 = float(input(f"Input your value for x0: "))
sig = float(input(f"Input your value for sigma: "))
z0 = float(input(f"Input your value for z0: "))
upper_b = eval(input(f"Input a upper bound ('inf'for infinity):"))
lower_b = eval(input(f"Input a lower bound (-inf for negative infinity):"))

# Definition of formula
def integral(x, A, x0, sig, z0):
    """Can be used to calculate the integral for given parameters and given bounds"""
    a = -1 * ((x - x0)**2)
    b = (2*(sig**2))
    function = A * np.exp(a/b)
    return function

# Calculating integral
parameters = (A, x0, sig, z0)
area, error = quad(integral, lower_b, upper_b, parameters)
print(area)

# Plotting
x = np.linspace(lower_b - 2*sig, upper_b + 2*sig, 200)
y = integral(x, A, x0, sig, z0)

plt.plot(x, y, 'b-', label=f'Gaussian')
plt.fill_between(x, y, where=(x >= lower_b) & (x <= upper_b), alpha=0.3, color='red', label=f'Area = {area:.4f}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(f'Gaussian: A={A}, x0={x0}, σ={sig}, z0={z0}')
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()


# In[ ]:




