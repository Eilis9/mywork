# round.py
# Author: Eilis Donohue
# lab 3.2.1 exercise
# read in a float and output an int

float_number = float(input("Enter a float number:"))

int_number = round(float_number)

print("{} rounded is {}".format(float_number, int_number))