'''
lab 2 loops
'''

the_number = 50
user_guess = int(input("Please guess the number:"))


while user_guess != the_number:
    print("Wrong")
    user_guess = int(input("Please guess again:"))

print("Correct!")
