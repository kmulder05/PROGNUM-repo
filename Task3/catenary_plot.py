#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from matplotlib import pyplot as plt
import numpy as np

# Plotting catenary with NumPy array
y = []
r = np.arange(-5, 6)
x = [i for i in r]

for i in r:
    a = np.cosh(i)
    y.append(a)

plt.plot(x, y, color = 'red', label = r"$\cosh{x}$")
plt.grid()
plt.title("Catenary")
plt.ylabel("Weight", fontsize = 13)
plt.xlabel("Location", fontsize = 13)
plt.legend(fontsize = 13)
plt.show()

