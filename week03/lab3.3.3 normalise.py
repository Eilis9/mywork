# normalise.py
# Author: Eilis Donohue
# lab 3.3.3 exercise
# stripping spaces and converting to lower case 


input_string = input("Please enter a string:")

output_string = input_string.strip().lower()

print("That string normalised is {}:".format(output_string))
print("we reduced the input string from {} to {} characters".format(len(input_string), len(output_string)))
