'''
lab 2 loops
'''
import random

the_number = random.randint(0,100)
user_guess = int(input("Please guess the number:"))


while user_guess != the_number:
    if user_guess < the_number:
      print("Too low!")
      user_guess = int(input("Please guess again:"))
    else:
       print("Too high")  
       user_guess = int(input("Please guess again:"))



print("Correct!")
