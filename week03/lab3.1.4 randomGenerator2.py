# randomGenerator2.py
# Author: Eilis Donohue
# lab 3.4 exercise
# user inputs the range

import random

lower_bound = int(input(f"Generate a random number between (enter lower bound): "))
upper_bound = int(input(f"..and (enter upper bound): "))

number = random.randint(lower_bound, upper_bound)

print("{} is a randomly generated number between {} and {}".format(number, lower_bound, upper_bound))