# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 12:44:09 2023

@author: dottd
"""

import json
json_dict = {
    "first_name": "Robert",
    "last_name": "Balti",
    "hobbies": ["traveling", "music"],
    "age": 34
}
 
# convert a dictionary into a string object that we can display.
json_data = json.dumps(json_dict,indent=4) 
print(json_dict)
print(type(json_data)) # string
 
# convert a JSON encoded object into a python dictionary.
python_dict = json.loads(json_data)  
print(python_dict)
print(type(python_dict)) # dict