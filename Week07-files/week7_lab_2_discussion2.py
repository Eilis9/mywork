'''week 8 files
lab exercise 2
Author: Eilis Donohue
'''
import os.path
FILENAME = "count2.txt"



def read_Number():
    try:
        with open(FILENAME, 'r') as f:
            number = int(f.read())
            return number
    except IOError:
        return 0

     

def write_number(input_number):
    with open(FILENAME, 'w') as f:
        f.write(str(input_number))



num = read_Number()
num = num + 1
write_number(num)
