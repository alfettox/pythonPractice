# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 12:39:55 2023

@author: dottd
"""

#JSON Files

import json
json_dict = {
    "first_name": "Giovanni",
    "last_name": "De Franceschi",
    "hobbies": ["hicking", "drawing"],
    "age": 37
}
 
json_data = json.dumps(json_dict,indent = 3) # indent each data item on a separate line 
print(json_data)
print(type(json_data)) # string