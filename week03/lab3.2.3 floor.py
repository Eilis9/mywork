# floor.py
# Author: Eilis Donohue
# lab 3.2.3 exercise
# read in a number and round down

#from math import floor

import math

float_number = float(input("Enter a number:"))
rd_number = math.floor(float_number)

print("{} floored is {}".format(float_number, rd_number))