# -*- coding: utf-8 -*-
"""
Week 5 lab extra (no.5)
@author: Eilis.Donohue
"""


student_name = input("Enter student name: ")

student = {"name": student_name, "modules" : []}
course_name = " "

while len(course_name) != 0:
    course_name = input("Enter a course: ") 
    if len(course_name) == 0:
        break
    course_grade = input("Enter the grade: ")  
    module_input = dict(coursename = course_name, grade = course_grade)   
    student["modules"].append(module_input) 

