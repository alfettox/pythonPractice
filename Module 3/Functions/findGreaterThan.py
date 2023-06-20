# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 17:12:03 2023

@author: Giovanni De Franceschi
"""
print("findGreaterThan: ")
def findGreaterThan(nums, threshold):
    for n in nums:
        if(n > threshold):
            print(n, end=", ")
            
nums = [1,2,6,45,7,8,9,0]
threshold = 5;

findGreaterThan(nums, threshold);

print("\n")
print("findDiv: ")

def findDiv(nums, factor):
    for n in nums:
        if(n%factor==0):
            print(n, end=", ")



findDiv(nums, 2);
findDiv(nums,3)