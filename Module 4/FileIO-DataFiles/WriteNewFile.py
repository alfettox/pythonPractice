# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 09:36:15 2023

@author: dottd
"""

try:
    f = open("flatland2.txt", "w")
    f.write("Ciao")    
    f.close()
except FileExistsError:
    # File already exists, handle the error here
    print("File already exists: flatland.txt")
