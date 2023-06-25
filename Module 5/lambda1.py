# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 18:23:26 2023

@author: dottd
"""

#Lambda function


x = lambda a : a + 10;

print(x(5))

inputUser = int(input("Insert a digit: "))

y = lambda r: r + 10

print(y(inputUser))



e = lambda z,o : z * o;
print(e(3,4))


w = lambda u,i,p : u + i + p;

print("Print that: ", w(1,2,3))