# -*- coding: utf-8 -*-
"""
Week 5 lab extra (no.6)
@author: Eilis.Donohue
"""

#structure - list of dictionaries
students = [
            
            {"name":"student1name", "modules":
                 [{"coursename" : "english", "grade" : 50}]
            },
                
            
            {"name":"student2name",      "modules" : 
                 [{"coursename" : "english", "grade" : 60}]
            }

          ]      
# initialise students as a list    
students = []
# initialise student_name to start loop
student_name = " "

while len(student_name) != 0:
    #initialise module input list for new student
    module_input = []
    course_name = " "
    student_name = input("Enter student name: ")
    if len(student_name) == 0:
        break      
    
    while len(course_name) != 0:
        course_name = input("Enter a course: ")    
        if len(course_name) == 0:
            break               
        course_grade = input("Enter the grade: ")           
        the_module_input = dict(coursename = course_name, grade = course_grade)   
        # append each module input to the module list
        module_input.append(the_module_input)
    
      
    student_input = dict(studentname = student_name, modules = module_input) 
    students.append(student_input)
        
