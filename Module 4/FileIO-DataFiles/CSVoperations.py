# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 12:37:46 2023

@author: dottd
"""

#write row

import csv
row_1 = ["employee_id","first_name","last_name"] # header row
row_2 = ["EMP2345235636","robert","balti"] # first row
row_3 = ["EMP2498799899","mark","smith"] # second row
row_4 = ["EMP2498989890","mary","caldwell"] # third row
with open('data/employee.csv', 'w') as csv_file: # open file in write mode
    # use the writer class to create a writer object 
    # that we will use to write data into the file
    writer = csv.writer(csv_file,delimiter=',')  
    writer.writerow(row_1) # writing the header row
    writer.writerow(row_2) # writing the first row
    writer.writerow(row_3) # writing the second row
    writer.writerow(row_4) # writing the third row
 
csv_file.close()
 
f = open('data/employee.csv', 'r')
print(f.read())
f.close()


#Roes as lsit
import csv
dataset = [["EMP9807976877","mary","donald"],["EMP9807976872","jacky","foreman"],
           ["EMP4564564598","leslie","knope"]] 
            # a list of lists: each nested list is a separate row
 
# open file in append mode, which will add the data at the end of the  file
with open('data/employee.csv', 'a') as csv_file: 
    # use the writer class to create a writer object 
    # that we will use to write data into the file
    writer = csv.writer(csv_file,delimiter=',') 
    # write multiple rows at once using writerows
    writer.writerows(dataset) 
 
csv_file.close()
 
f = open('data/employee.csv', 'r')
print(f.read())
f.close()

#Rows as dict
import csv
 
# create three rows of data; item order is not important because each dictionary 
# uses keys to identify each value
row_1 = {"employee_id":"EMP4564576566","first_name":"jack","last_name":"russel"} 
row_2 = {"first_name":"jenny","last_name":"clapper","employee_id":"EMP9807976875"} 
row_3 = {"employee_id":"EMP4564564566","last_name":"cruz","first_name":"mario"} 
fieldnames = ["employee_id","first_name","last_name"]
with open('data/employee.csv', 'w') as csv_file: 
    writer = csv.DictWriter(csv_file,delimiter=',',fieldnames=fieldnames)  
    writer.writeheader()
    writer.writerow(row_1) # write the first row
    writer.writerow(row_2) # write the second row
    writer.writerow(row_3) # writethe third row
 
csv_file.close()
 
f = open('data/employee.csv', 'r')
print(f.read())
f.close()