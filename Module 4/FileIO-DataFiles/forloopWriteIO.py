# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 09:34:01 2023

@author: dottd
"""

f = open("flatland.txt", "w") 
 
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", 
         "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
         "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
         "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
         "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
 
for state in states:
    f.write(state) 
    f.write(";\n")
f.close()