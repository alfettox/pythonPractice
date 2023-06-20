# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 20:51:25 2023

@author: dottd
"""

# kwargs:  These are  keyword arguments. That means each argument has a variable name and a value. 
def display(**kwargs): # kwargs: a dictionary that contains the keyword/argument pairs.
    # we use a for loop to iterate through the list and display each argument. 
    for keyword,value in kwargs.items():  
        print(keyword + ": " + value) 
 
display(first_name = 'Robert', last_name = 'Johnson')
display(first_name = 'Mary', age = "32", location = "Dallas")



#keyword argument order

def display(first_name, middle_name, last_name):
    print(first_name + " " + middle_name + " " + last_name)
 
# if you use keyword argument then order does not matter
display(first_name ='Susan', middle_name ='Marie', last_name='Howard') 
display(middle_name ='Marie', last_name ='Howard', first_name='Susan')



#

def concat_numbers(number_1, number_2, number_3):
    concatenated = str(number_1) + str(number_2) + str(number_3)
    return int(concatenated)

concat_number = concat_numbers(number_2=5, number_3=14, number_1=5)
print(concat_number)
