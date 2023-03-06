# -*- coding: utf-8 -*-
"""
Week 6 lab
Exercise 2 

"""

def displayMenu():
    print("what would you like to do?")
    print("\t (a) add new student")
    print("\t (b) view students")
    print("\t (q) Quit")
    choice = input("Type one letter (a/v/q): ")
    
    return choice

choice = displayMenu()
print(f"You chose {choice}")