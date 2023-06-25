# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 18:30:41 2023

@author: dottd
"""

def myFunc(n):
    return lambda a : a * n;

doubler = myFunc(3);

print(doubler(2))


def pow_n(n):
    return lambda a:a;

pow_2 = pow_n(2);
print(pow_2(6))