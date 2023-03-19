# lab 8.1_6_7 plotting



import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

min_s = 20000
max_s = 80000
size_s = 100

salaries = np.random.randint(min_s, max_s, size_s)

print(salaries)

# https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.integers.html
rng = np.random.default_rng(3)
salaries_seeded1 = rng.integers(min_s, max_s, size_s)
# Andrew's way
np.random.seed(1)
salaries_seeded = np.random.randint(min_s, max_s, size_s)
#print("seeded", salaries_seeded)
#print("seeded1", salaries_seeded1)
salaries_plus = salaries + 5000
salaries_seeded_plus = salaries_seeded + 5000
#print(salaries_plus)
#print(salaries_seeded_plus)

salaries_seeded_5pc = salaries_seeded * 1.05
#print(salaries_seeded_5pc)
new_salaries = salaries_seeded_5pc.astype(int)
#print(new_salaries)

#plt.hist(new_salaries)

age_lower = 21
age_higher = 65

ages = np.random.randint(age_lower, age_higher, size_s)
#print(ages)
plt.scatter(ages, salaries_seeded_5pc, label='salaries v ages')

#x = np.arange(0,10)
x = np.array(range(1,100))
#print(x, type(x)) 
y = x ** 2

norm_dist = np.random.normal(loc=5000, scale=200, size=1000)

plt.plot(x, y, color='red', label='y=x^2')
plt.title("salaries and function y=x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.savefig('prettier plot.png')
#plt.show()

salaries_ages = np.concatenate((ages, new_salaries), axis=0)
print(salaries_ages)
# do seaborn plots
#seaborn_data = sns.load_dataset(salaries_ages)
sns.relplot(data=salaries_ages)
sns.displot(norm_dist, kind="kde")
