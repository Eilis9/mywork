# lab 8.1_6_7 plotting



import numpy as np
import matplotlib.pyplot as plt

min_s = 20000
max_s = 80000
size_s = 10

salaries = np.random.randint(min_s, max_s, size_s)

print(salaries)

# https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.integers.html
rng = np.random.default_rng(3)
salaries_seeded1 = rng.integers(min_s, max_s, size_s)
# Andrew's way
np.random.seed(3)
salaries_seeded = np.random.randint(min_s, max_s, size_s)
print("seeded", salaries_seeded)
print("seeded1", salaries_seeded1)
salaries_plus = salaries + 5000
salaries_seeded_plus = salaries_seeded + 5000
print(salaries_plus)
print(salaries_seeded_plus)

salaries_seeded_5pc = salaries_seeded * 1.05
print(salaries_seeded_5pc)
new_salaries = salaries_seeded_5pc.astype(int)
print(new_salaries)

plt.hist(new_salaries)
#plt.show()