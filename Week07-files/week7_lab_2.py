'''week 8 files
lab exercise 2
Author: Eilis Donohue
'''
FILENAME = "count.txt"

def read_Number():
   with open(FILENAME, 'r') as f:
       number = int(f.read())
   return number




def write_number(input_number):
    with open(FILENAME, 'w') as f:
        f.write(str(input_number))


num = read_Number()
num = num + 1
write_number(num)
