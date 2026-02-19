#!/usr/bin/env python
# coding: utf-8

# In[ ]:


F = [1, 2]

for f in range(98):
    F.append(F[-1] + F[-2])

print(F)
print(f"The length of my Fibonacci sequence is: {len(F)}")

