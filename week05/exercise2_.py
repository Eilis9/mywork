# -*- coding: utf-8 -*-
"""
Week 5 lab exercise 2
@author: Eilis.Donohue
"""

import random

no_of = 11
queue_list = []



for i in range(1,no_of):
    queue_list.append(random.randint(0,100))
   
print("queue is ", queue_list)
 

while len(queue_list) != 0:
    current_number = queue_list.pop(0)
    print(f'current number is {current_number} and the queue is {queue_list}')

print('the queue is now empty')    
    
# dont do like this
#for i in range(1,no_of):
#    current_number = queue_list[0]
#    queue_list_amended = queue_list[1:]
#    queue_list.pop(0)
#    print(f'current Number is {current_number} and the queue is {queue_list_amended}')
#print('the queue is now empty')    

