# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 12:33:58 2023

@author: dottd
"""

#Dictionary reader

import csv

with open('data/stocks_short.csv') as f:
    csv_file = csv.DictReader(f, delimiter=',')

    for row in csv_file:
        print(row)
        


# List

def read_csv(filepath,delimiter=","):
    import csv
    dataset = list()
    with open(filepath) as f: 
 
        # use the DictReader function of the csv module to 
        # read the file using the same delimiter
        csv_file = csv.DictReader(f, delimiter=delimiter) 
 
        # csv_file is an iterable object that we can iterate on using a for loop
        for row in csv_file:
            dataset.append(row)
 
    return dataset
 
dataset = read_csv("data/stocks_short.csv")
print(len(dataset)) # number of rows in the dataset
print(dataset[0]) # print first row in the dataset
print(dataset)