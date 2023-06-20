# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 20:18:32 2023

@author: dottd
"""

#Concept 5

def find_greater(numbers,threshold):
    greater = list()
    for num in numbers:
        if (num > threshold):
            greater.append(num)
    return greater
    
numbers = [1,5,5,7,10,1]


result1 = find_greater(numbers,0) 
print(result1) 

result2 = find_greater(numbers,5) 
print(result2)


#convert set to a list

def set2list(input_set):
    list = [];
    for i in input_set:
        list.append(i);
    return list;


s = {"paola","stella", "serena"};

print(2);
print(type(1));


#
def set2listV2(input_set2):
    return list2(input_set2)

s2 = {"paola", "stella", "serena"}
converted_list2 = set2list(s)
print(converted_list2)