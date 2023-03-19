# lab 8 extra 

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
norm_dist = np.random.normal(loc=5, scale=2, size=100)

print(norm_dist)

plt.hist(norm_dist)
plt.show()