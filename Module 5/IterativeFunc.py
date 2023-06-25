# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 18:34:32 2023

@author: dottd
"""

#TRANSFORM ALL THE ELEMENTS IN THE ARRAY TO BE UPPERCASE
def toUpperCase(s):
    return str(s).upper();

names=['giovanni', 'paola', 'eva'];

print(names)

names_upper = map(toUpperCase, names)

names_upper_list = list(names_upper)

print(names_upper_list)
print(type(names_upper_list))


#REMOVE FIRST CHARACTER
def remove_first_char(s):
    return str(s)[1:]

def remove_last_char(s):
    return str(s)[:-1]

names = ['giovanni', 'paola', 'eva']
print(names)

names_new = map(remove_first_char, names)
names_new_list = list(names_new)
print(names_new_list)


names_new = map(remove_last_char, names)
names_new_list = list(names_new);
print(names_new_list)