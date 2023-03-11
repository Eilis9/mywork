# -*- coding: utf-8 -*-
"""
Week 6 lab
Exercise 4 

"""
import json




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

def doSave(students):
  # print ("do save")
  save_dict(students)

  #  with open(FILENAME, 'w') as f:
  #      f.write(students)
  #  return

def save_dict(some_dict):
    with open(FILENAME, 'w') as f:
        json.dump(some_dict, f)


def doLoad():
    students = read_dict()
    return students


def read_dict():
    with open(FILENAME, 'r') as f:
        return json.load(f)
    

def displayMenu():
    print("what would you like to do?")
    print("\t (a) add new student")
    print("\t (b) view students")
    print("\t (q) Quit")
    print("\t (s) Save to file")
    print("\t (l) Load student from file")
    choice = input("Type one letter (a/v/q/s/l): ")
    
    return choice
FILENAME = "studentData.json"
choice = displayMenu()

while choice != 'q':
#    choice = displayMenu()
    if choice == "a":
        doAdd(students)
    elif  choice == "v":
        doView(students)
    elif choice == 's':
        doSave(students)
    elif choice == 'l':
        students = doLoad()
    elif choice != "q":
        print("\n\n please select either a,v,q,s,l")
       
    choice = displayMenu()
       
        
        



