'''week 8 files
lab exercise 2
Author: Eilis Donohue
'''
FILENAME = "count2.txt"
import os.path


def read_Number():
   with open(FILENAME, 'r') as f:
       number = int(f.read())
   return number


def write_number(input_number):
    with open(FILENAME, 'w') as f:
        f.write(str(input_number))


if os.path.isfile(FILENAME) == False:
#if not os.path.isfile(FILENAME):
    write_number(0)

num = read_Number()
num = num + 1
write_number(num)
