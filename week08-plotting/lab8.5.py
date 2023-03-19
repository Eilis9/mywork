# lab 8.5 plotting

import numpy as np
import matplotlib.pyplot as plt

#x = np.arange(0,10)
x = np.array(range(1,101))
print(x, type(x)) 
y = x ** 2

plt.plot(x,y)
plt.show()
