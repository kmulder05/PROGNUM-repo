#!/usr/bin/env python
# coding: utf-8

# In[1]:


from numpy import sin, cos, exp, pi
import numpy as np
from scipy.integrate import quad

while True:
    try:
        input_function = input(f"Input any function here")
        a = eval(input(f"Input a lower bound "))
        b = eval(input(f"Input a upper bound "))
    
        def f(x): 
            """Evaluates the user inputted function"""
            return eval(input_function)
        
        # The integral calculated with quad
        area, error = quad(f, a, b)

        # The Monte Carlo integral
        length = 10000000
        n = np.random.uniform(a, b, length)
        ev = np.array(f(n))
        part_1 = (b - a)/length
        part_2 = np.sum(ev)
        MC = part_1 * part_2
        
        break
    except (SyntaxError, NameError, TypeError):  # If there is a wrong input, the except part lets you try again
        print(f"Your input didn't work, try again")

print(f"The integral taken of your function gave the answer: {area}")
print(f"The integral calculated with the Monte Carlo integral gave the answer: {MC}")

