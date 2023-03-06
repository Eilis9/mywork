# -*- coding: utf-8 -*-
"""
Week 6 assignment
A function which calculates the root of an inputted number
Uses Newton-Raphson method: 
https://en.wikipedia.org/wiki/Newton%27s_method
Author: Eilis Donohue
"""






def nr(a, tol = 0.01):
    tol_check = 100
    x1 = a/2
    while abs(tol_check) > tol:     
            x1, tol_check = nr_iter(x1, a)
    return x1
    
        
def nr_iter(x0, a):
    f = x0 ** 2
    # f_dash is derivative of f
    f_dash = 2 * x0
    # newton raphson method
    x1 = x0 - ((f - a) / f_dash)
    # calculated the error
    tol_check = (x1 - x0) / x0
    return x1, tol_check               


the_answer = nr(50)