# -*- coding: utf-8 -*-
"""
Week 5 lab
@author: Eilis.Donohue
"""

# create a tuple

months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 
         'August', 'September', 'October', 'November', 'December')


summer_months1 = months[4], months[5], months[6]
summer_months = months[4:7]

for month in summer_months:
    print(month)