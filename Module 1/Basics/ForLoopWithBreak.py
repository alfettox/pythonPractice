# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 08:46:59 2023

@author: dottd
"""

#Simple for loop

num = 1
for i in range (5,20):
    num +=1
    print("My number is: ", num)
    
    
#Simple for loop2

num=5
sum =0;

for i in range (10,20):
    sum = sum + num;
    print(sum);
    if(sum >= 40):
        break;