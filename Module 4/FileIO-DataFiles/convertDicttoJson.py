# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 12:45:58 2023

@author: dottd
"""

import json
# we use pprint to display json/dictionary objects in a human-readable format.
from pprint import pprint  
 
with open('data/prizes.json','r') as jsonfile: # use open to read the file
    # use the json module with the load function 
    # to read the entire content of the json file in a dictionary
    data = json.load(jsonfile) 
 
# convert the  data dict into a string json encoded object. 
data_str = json.dumps(data) 
print(type(data)) # dict
print(type(data_str)) # str