# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 16:20:57 2023

@author: dottd
"""

#ETL Tutorial
#Extract transform load, used to move data between databases, servers and machines

from extract import extract # import the external extract class
from transform import transform # import the external extract class
from load import load # import the external load class


import csv
import json


class Extract:
    def fromCSV(self, file_path):
        try:
            data = []
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append(row)
            return data
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return []


class Transform:
    def renameAttribute(self, dataset, old_attr, new_attr):
        transformed_dataset = map(lambda d: {new_attr: d.pop(old_attr), **d}, dataset)
        return list(transformed_dataset)

    def filterData(self, dataset, condition):
        transformed_dataset = filter(condition, dataset)
        return list(transformed_dataset)


class Load:
    def toCSV(self, dataset, file_path):
        try:
            with open(file_path, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=dataset[0].keys())
                writer.writeheader()
                writer.writerows(dataset)
            print("Data saved to CSV successfully.")
        except Exception as e:
            print(f"Error occurred while saving to CSV: {e}")

    def toJSON(self, dataset, file_path):
        try:
            with open(file_path, 'w') as file:
                json.dump(dataset, file)
            print("Data saved to JSON successfully.")
        except Exception as e:
            print(f"Error occurred while saving to JSON: {e}")


# Step 1: Extract data from the source file
extractor = Extract()
dataset = extractor.fromCSV("data/got_chars.csv")

# Step 2: Transform the data
transformer = Transform()
transformed_data = transformer.renameAttribute(dataset, "old_attribute", "new_attribute")
transformed_data = transformer.filterData(transformed_data, lambda d: d["attribute"] == "value")

# Step 3: Load the transformed data into CSV and JSON files
loader = Load()

# Save the transformed data to a CSV file
loader.toCSV(transformed_data, "output.csv")

# Save the transformed data to a JSON file
loader.toJSON(transformed_data, "output.json")
