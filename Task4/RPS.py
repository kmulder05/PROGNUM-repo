#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

I = input(f"Please type 'R' for Rock, 'P' for paper or 'S' for Scissors:")

# Assigning numbers to input
if I == 'R':
    I = 1
elif I == 'P':
    I = 2
elif I == 'S':
    I = 3
else:
    print("Incorrect input")

# Creating random R, P, or S
C = np.random.randint(1, 3+1)

# Finding who wins
if I == C:
    print("Draw")
elif I == 1 and C == 2:
    print("Computer won")
elif I == 1 and C == 3:
    print("You won")
elif I == 2 and C == 1:
    print("Computer won")
elif I == 2 and C == 3:
    print("You won")
elif I == 3 and C == 1:
    print("Computer won")
elif I == 3 and C == 2:
    print("You won")

