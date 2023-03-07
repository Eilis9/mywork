''' bank.py
Week 2 PANDS task assignment 
Author: Eilis Donohue
Prompts the user for 2 integer inputs 
Adds these and outputs the answer in euro and cent
'''


# Prompt user for input
input1 = int(input("Enter amount1(in cent): "))
input2 = int(input("Enter amount2(in cent): "))

# Add the inputs
total_cent = input1 + input2

# Convert total to a string type so that slicing can be applied
total_cent = str(total_cent)
# Last 2 digits of the string is the cent amount and everything else is euro.
# This avoids float types and need for leading zeroes when using // and % 
euro_amount = total_cent[:-2]
cent_amount = total_cent[-2:]

# Output the amount 
print(f"The sum of these is €{euro_amount}.{cent_amount}")