'''
grade.py

'''

grade = float(input("Enter the percentage:"))

grade = round(grade, 0)
print(grade)
if grade < 0 or grade > 100:
    print("invalid grade")
elif grade < 40:
    print("Fail")
elif grade < 50:
    print("Pass")
elif grade < 60:
    print("Merit 2")
elif grade < 70:
    print("Merit 1") 
else: 
    print("Distinction")
           