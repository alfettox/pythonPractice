# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 18:50:04 2023

@author: dottd
"""

def initial_h(dataset):
    for x in dataset:
        if str.lower(x[0]) == "h":
            return True
        else:
            return False
 
names=['Haythem','Mike','James','Helen','Mary']
print(names)
 
names_filtered = filter(initial_h,names) 
print(type(names_filtered))
 
names_filtered_list = list(names_filtered)
print(type(names_filtered_list))
 
print(names_filtered_list)