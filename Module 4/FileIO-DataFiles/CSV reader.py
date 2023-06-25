# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 09:50:25 2023

@author: dottd
"""

#CSV files


#import csv;

#with open('data/stocks_short.csv') as f:
    
#    csv_file = csv.reader(f, delimiter = ',')
    
#    for row in csv_file:
#        print(row)
#        print(row[0])
#        print(row[1])
        
#f.close();


#

import csv

with open('data/stocks.csv') as f:
    csv_file = csv.reader(f, delimiter=',')

    opening_prices = []  # List to store all the opening prices

    # Skip the first row (header row) of the CSV file
    next(csv_file)

    for row in csv_file:
        opening_price = float(row[1])  # Extract the opening price from the row
        opening_prices.append(opening_price)  # Add the opening price to the list

    average_opening_price = sum(opening_prices) / len(opening_prices)  # Calculate the average

    print("Average Opening Price:", average_opening_price)
