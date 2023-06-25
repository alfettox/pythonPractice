# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 18:56:10 2023

@author: dottd
"""

import csv
from functools import reduce

def read_car_data(file_path):
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def filter_by_make(data, make):
    filtered_data = filter(lambda car: car['Make'] == make, data)
    return list(filtered_data)

def filter_fuel_efficient_cars(data):
    filtered_data = filter(lambda car: int(car['City_MPG']) > 35, data)
    return list(filtered_data)

def filter_high_horsepower_cars(data):
    filtered_data = filter(lambda car: int(car['Horsepower']) > 100, data)
    return list(filtered_data)

def calculate_driving_cost(car, gas_cost_per_gallon):
    city_mpg = int(car['City_MPG'])
    cost_per_mile = gas_cost_per_gallon / city_mpg
    return round(cost_per_mile * 100, 2)

def calculate_average_mpg(data):
    total_city_mpg = reduce(lambda acc, car: acc + int(car['City_MPG']), data, 0)
    total_highway_mpg = reduce(lambda acc, car: acc + int(car['Highway_MPG']), data, 0)
    num_cars = len(data)
    avg_city_mpg = total_city_mpg / num_cars
    avg_highway_mpg = total_highway_mpg / num_cars
    return round(avg_city_mpg, 2), round(avg_highway_mpg, 2)

def calculate_average_cost(data):
    total_cost = reduce(lambda acc, car: acc + car['Cost'], data, 0)
    num_cars = len(data)
    avg_cost = total_cost / num_cars
    return round(avg_cost, 2)

# Step 1: Read car_data.csv file
car_data = read_car_data('./data/car_data.csv')

# Step 2: Filter cars by make
user_input = input("Enter a car make to filter by: ")
filtered_by_make = filter_by_make(car_data, user_input)
print(filtered_by_make)

# Step 3: Filter fuel-efficient cars
fuel_efficient_cars = filter_fuel_efficient_cars(car_data)
print(fuel_efficient_cars)

# Step 4: Filter cars with high horsepower
high_horsepower_cars = filter_high_horsepower_cars(car_data)
print(high_horsepower_cars)

# Step 5: Calculate cost of driving 100 miles for each car
gas_cost_per_gallon = float(input("Enter the current gas cost per gallon: "))
driving_costs = list(map(lambda car: calculate_driving_cost(car, gas_cost_per_gallon), car_data))
print(driving_costs)

# Step 6: Calculate average city MPG and highway MPG
average_city_mpg, average_highway_mpg = calculate_average_mpg(car_data)
print("Average City MPG:", average_city_mpg)
print("Average Highway MPG:", average_highway_mpg)

# Step 7: Calculate average cost of all cars
average_cost = calculate_average_cost(car_data)
print("Average Cost:", average_cost)
