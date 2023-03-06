# -*- coding: utf-8 -*-
"""
Week 6 lab
Exercise 3 

"""




def displayMenu():
    print("what would you like to do?")
    print("\t (a) add new student")
    print("\t (b) view students")
    print("\t (q) Quit")
    choice = input("Type one letter (a/v/q): ")
    
    return choice



def doAdd():
    print("in adding")
    
def doView():
    print("in viewing")    
    
    
#choice = None    
choice = displayMenu()

while choice != 'q':
#    choice = displayMenu()
    if choice == "a":
        doAdd()
    elif  choice == "v":
        doView()
    elif choice != "q":
        print("\n\n please select either a,v,q")
    choice = displayMenu()
       
        
        
        
        

#print(f"You chose {choice}")

        