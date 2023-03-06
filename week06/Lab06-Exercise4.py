# -*- coding: utf-8 -*-
"""
Week 6 lab
Exercise 4 

"""





students = []

def readModules():
    modules = []

    module_name = input("Enter the first Module name (blank to quit):").strip()
    while module_name != "":
        the_module = {}
        the_module["moduleName"] = module_name
        the_module["moduleGrade"] = input("Enter the grade: ")
        modules.append(the_module)
        module_name = input("Enter next module name: ")
        
    return modules



def doView(students):
    for student in students:
        print(student['name'])
        displayModules(student['modules'])
    return

def displayModules(modules):
    for module in modules:
        print(f"\t Module: {module['moduleName']}, \t Grade:{module['moduleGrade']}")
        
    return


def doAdd(students):

    current_student = {}
    current_student["name"] = input("enter name: ")
    current_student["modules"] = readModules()
    students.append(current_student)
    
    return 

def displayMenu():
    print("what would you like to do?")
    print("\t (a) add new student")
    print("\t (b) view students")
    print("\t (q) Quit")
    choice = input("Type one letter (a/v/q): ")
    
    return choice

choice = displayMenu()

while choice != 'q':
#    choice = displayMenu()
    if choice == "a":
        doAdd(students)
    elif  choice == "v":
        doView(students)
    elif choice != "q":
        print("\n\n please select either a,v,q")
    choice = displayMenu()
       
        
        



