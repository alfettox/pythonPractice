# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 09:45:57 2023

@author: dottd
"""

import os;

file = open("temp.txt", "w");
for i in range(10):
    file.write(str(i));
    file.write("\n")
file.close()

os.remove("data")