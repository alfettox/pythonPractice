# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 09:28:36 2023

@author: dottd
"""

#Add Content to a file

file = open("The rise of meritocracy.txt", "a")

file.write("\n This is an added line");
file.write("ADDED");

file.close();


#Overwrite the contents of a file

file = open("The rise of meritocracy.txt", "w")

file.write("\n This line override");
file.write("\n Overridden");

file.close();