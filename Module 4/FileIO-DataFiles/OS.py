# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 09:42:06 2023

@author: dottd
"""

#OS

import os
 
if os.path.exists("data/flatland01.txt"):
   print("The file exists.")
else:
   print("The file doesn't exist.")
   
if os.path.exists("data/not_existing.txt"):
   print("The file exists.")
else:
   print("The file doesn't exist.")
   



#