# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 12:44:29 2023

@author: dottd
"""

import json
# we use pprint to display json/dictionary objects in a human readable format
from pprint import pprint 
 
with open('data/prizes.json','r') as jsonfile: # use open to read the file
    # use the json module with the load function 
    # to read the content of the json file into a dictionary
    data = json.load(jsonfile) # load the json content and serialize it. 
print(type(data)) #dict
pprint(data) # print the entire file content. 