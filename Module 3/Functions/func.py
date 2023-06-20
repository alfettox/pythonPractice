# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 17:01:57 2023

@author: Giovanni De Franceschi
"""
num1 = 2;
num2 = 5;


def sumFunction(num1, num2):
        return num1 +num1;
        
    
print("the sum is: ", sumFunction(num1,num2));


nums = [1,5,5,7,8,10,1]

def findMax(nums):
    big = 0;
    for i in nums:
        if(big<i):
            big = i;
    return big;

print(nums)
print("Max value is: ", findMax(nums))  