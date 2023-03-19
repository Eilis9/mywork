# lab 8.11 

import numpy as np
import matplotlib.pyplot as plt


possible_counties = np.array(["Galway", "Leitrim", "Mayo", "Roscommon", "Sligo"])
counties = np.random.choice(possible_counties, p=[0.7, 0.01, 0.1, 0.09, 0.1], size=100)

#print(counties)
unique, count_of = np.unique(counties, return_counts=True)

print(unique)
print(count_of)

#plt.pie(count_of, labels=unique)
plt.bar(unique, count_of)

plt.show()