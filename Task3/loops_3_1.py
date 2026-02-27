#!/usr/bin/env python
# coding: utf-8

# ### 3.1

# In[21]:


masses = [1.9891e+30, 1.8986e+27, 
          5.6846e+26, 1.0243e+26, 8.6810e+25,
          5.9736e+24, 4.8685e+24, 6.4185e+23, 
          3.3022e+23, 7.349e+22, 1.25e22]

new_masses = []

# Loops over all values in the list and adds the masses that are big than the moons mass to a new list
for m in masses:
    if m > masses[9]:
        new_masses.append(m)

print(f"The Masses bigger than the mass of the moon: {new_masses}")

print()

# Slicing the original list to get only the last 5 masses
slc = slice(-6, None)
masses_slc = masses[slc]
print(f"The last 5 of the masses list: {masses_slc}")

print()
    
# Calculating sum of masses in masses_slc
s = sum(masses_slc)
l = len(masses_slc)
avg = s/l
print(f"The average of the 5 masses is: {avg}")



# In[ ]:




