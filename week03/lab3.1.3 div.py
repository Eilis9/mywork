# div.py
# Author: Eilis Donohue
# lab 3.3 exercise

x = int(input("Enter first number: "))
divider = int(input("Enter the number you want to divide by: "))

answer = int(x // divider)
remainder_answer = x % divider 

print(f'{x} divided by {divider} is {answer} with remainder {remainder_answer}')

print('{} divided by {} is {} with remainder {}'.format(x, answer, remainder_answer))