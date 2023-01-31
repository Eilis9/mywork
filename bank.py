# bank.py
import math

# ask user for input
input1 = int(input("Enter amount1(in cent): "))
input2 = int(input("Enter amount2(in cent): "))

# add the inputs
total_cent = input1 + input2

# convert to euro
total_euro = total_cent / 100

# print total
print("The sum of these is €", total_euro, sep="")