# convert.py
# Author: Eilis Donohue
# lab 3.2.4 exercise
# read in a number and convert it



float_number = float(input("Please enter an amount:"))
value_cent = round(abs(float_number)*100)

print("That amount in cent is: {} ".format(value_cent))