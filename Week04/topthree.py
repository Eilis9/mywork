'''
lab 2 loops
'''

import random
the_list = []
how_many = 10
top_how_many = 3
range_from = 0
range_to = 100


for i in range(0, how_many):
    the_list.append(random.randint(range_from, range_to))

the_list.sort()
print(f'{how_many} random numbers are {the_list}')

the_list.sort(reverse = True)

print(f'top {top_how_many} are {the_list[:top_how_many]}')
