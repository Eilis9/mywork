# -*- coding: utf-8 -*-
"""
Week 5 lab exercise 3
@author: Eilis.Donohue
"""

student = {"name" : "Mary", 
           "modules": [
               {
                   "courseName": "Programming",
                   "grade":45},
               
               {
                   "courseName": "History",
                   "grade": 99
                  }
               ]}

print("student: {}".format(student["name"]))

for module in student["modules"]:
    print("Module:{}, Grade:{}".format(module["courseName"], module["grade"]))