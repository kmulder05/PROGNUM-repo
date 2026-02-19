#!/usr/bin/env python
# coding: utf-8

# In[9]:


# User can input their values for a, b and c.
a = float(input(f"Input your value for a:"))
b = float(input(f"Input your value for b:"))
c = float(input(f"Input your value for c:"))

# Using inputted values to calculate the discriminant
D = b**2 - 4 * a * c

print(f"The calculated value for the discriminant (D) is: {D}")

x_1 = (-b + D**0.5) / (2 * a)
x_2 = (-b - D**0.5) / (2 * a)

# Gives the x values if there is one, otherwise it tells you that there are no real solutions
if D > 0:
    print(f"The calculated D is bigger then 0, which gives us the x values: x1 = {x_1} and x2 = {x_2}")
elif D == 0:
    print(f"The calculated D is equal to 0, which gives us one x value: x1 = {x_1}")
else:
    print(f"Your calculated D is smaller than 0, which gives no real solutions.")


# In[ ]:





# In[ ]:




