# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 12:47:03 2023

@author: dottd
"""

#Create Json

import json
from pprint import pprint
# create a list of dictionaries, which represent 
# a list of items that will be stored in the file.
data = []  
data.append({"name":"John Smith","DOB":"10/10/1979"})
data.append({"name":"Michael Douglas","DOB":"12/31/1979"})
with open('data/person.json', 'w') as outfile:  
    json.dump(data, outfile)
 
f = open('data/person.json', 'r')
pprint(f.read())
f.close()