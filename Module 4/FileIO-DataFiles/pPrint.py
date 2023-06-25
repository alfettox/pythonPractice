# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 12:46:36 2023

@author: dottd
"""

#pprint

import json
from pprint import pprint
 
with open('data/prizes.json','r') as jsonfile:    
    data = json.load(jsonfile)
 
for row in data['prizes']:
    pprint(row['category'])
    pprint(row['year'])