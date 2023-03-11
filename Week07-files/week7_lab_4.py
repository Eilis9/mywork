'''week 8 files
lab exercise 4
Author: Eilis Donohue
'''
import json
FILENAME = "testdict.json"
#sample = dict(name='fred', age=31, grades=[1,34,35])

def read_dict():
    with open(FILENAME, 'r') as f:
      #  cont = json.load(f)
        return json.load(f)

cont = read_dict()

print(cont) 
