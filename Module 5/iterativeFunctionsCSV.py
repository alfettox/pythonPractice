# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 18:42:20 2023

@author: dottd
"""

#Apply the Map Function

import csv

def fromCSV(path, delimiter, quotechar):
    data = []
    with open(path, newline='') as csvfile:
        filecontent = csv.DictReader(csvfile, delimiter=delimiter, quotechar=quotechar)
        for row in filecontent:
            data.append(row)
    return data

def extract_month(row):
    value = row['Date']
    MM = ""
    a = value.split("/")
    MM = a[0]
    new_row = row.copy()
    new_row.update({'Month': MM})
    return new_row

data = fromCSV(path='data/stocks.csv', delimiter=',', quotechar='|')
print(data[0])

data_mapped = map(extract_month, data)
data_mapped_list = list(data_mapped)
print(data_mapped_list[0])
