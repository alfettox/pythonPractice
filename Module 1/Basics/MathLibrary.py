# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 08:51:16 2023

@author: dottd
"""

#Using functions and packages

import math as mt


def function_square(a):
        c = a * a;
        return c;
    
def function_remainder(x,y):
        z = x%y;
        return z;
        
print(function_remainder(33,5))

print (function_square(4))

print(mt.sqrt(256))

logged = mt.log(9)
print (logged)

exponential = mt.exp(50);
print(exponential)