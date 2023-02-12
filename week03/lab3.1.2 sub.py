# sub.py
# Author: Eilis Donohue
# lab 3.2 exercise

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

answer = first_number - second_number

# f string
print(f'{first_number} minus {second_number} is {answer}')

# using non f string method
print("{} minus {} is {}".format(first_number, second_number, answer))