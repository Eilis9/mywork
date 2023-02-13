# randomfruit.py
# Author: Eilis Donohue
# lab 3.5 exercise
# random selection

import random

fruits = ['Apple', 'Orange', 'Banana', 'Pear']

index = random.randint(0, len(fruits)-1)

fruit = fruits[index]

print("A random fruit: {}".format(fruit))
