# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 20:33:35 2023

@author: dottd
"""

#Indefinite number of parameters

def display(*argv):
    for arg in argv:
        print(arg);
        
display("Hello World!", "My name is Giovanni");
display("salut!", "learning also python", "java domina!")
display("hi")

display();



#Compute sum with indefinite number of integers

def compute_sum(nums):
    summation = 0
    for i in nums:
        summation += i
    return summation
    
nums = [1,5,5,7,10,1];
summation = compute_sum(nums);

print(summation);