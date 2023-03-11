'''week 8 files
lab exercise 3
Author: Eilis Donohue
'''
import json
FILENAME = "testdict.json"
sample = dict(name='fred', age=31, grades=[1,34,35])

def write_dict(obj):
    with open(FILENAME, 'w') as f:
        json.dump(obj, f)


write_dict(sample)


 
