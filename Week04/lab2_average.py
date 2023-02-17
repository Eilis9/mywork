'''
lab 2 loops
'''

user_inputs = []

user_inp = int(input("enter number (0 to quit)"))


while user_inp != 0:
   user_inputs.append(user_inp)
   user_inp = int(input("enter another (0 to quit)"))    
 
for value in user_inputs:
   print(value)

inp_average = float(sum(user_inputs)) / len(user_inputs)

print(inp_average)
