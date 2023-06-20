# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 20:12:59 2023

@author: dottd
"""


#default values for functions as overloading



#def display(message = "Hello World!"):
 #   print(str(message));
    
    
display("something");

display();


#example 2
#Fix the code below so that the find_greater function uses the default value 0 as the threshold value if we don't specify a different value.
def find_greater(numbers,threshold = 0):
    for num in numbers:
        # we only display the numbers that are above the input threshold
        if (num > threshold):
            print(num)
 
numbers = [1,5,5,7,10,1]
find_greater(numbers) # find all numbers greater than 0
find_greater(numbers,5) # find all numbers greater than 5