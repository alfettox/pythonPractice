# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 15:44:24 2023

@author: Giovanni De Franceschi
"""
import json
from collections import defaultdict

def calculate_scores(data):
    restaurant_scores = defaultdict(list)
    cuisine_scores = defaultdict(lambda: defaultdict(list))

    entry = json.loads(data)

    restaurant_name = entry['name']
    borough = entry['borough']
    cuisine = entry['cuisine']
    scores = [grade['score'] for grade in entry['grades']]

    restaurant_scores[restaurant_name].extend(scores)
    cuisine_scores[cuisine][borough].extend(scores)

    print("Average score for each restaurant:")
    for restaurant, scores in restaurant_scores.items():
        average_score = sum(scores) / len(scores)
        print(f"{restaurant}: {average_score}")

    print("\nMinimum score for each restaurant:")
    for restaurant, scores in restaurant_scores.items():
        min_score = min(scores)
        print(f"{restaurant}: {min_score}")

    print("\nMaximum score for each restaurant:")
    for restaurant, scores in restaurant_scores.items():
        max_score = max(scores)
        print(f"{restaurant}: {max_score}")

    print("\nAverage score for each type of cuisine in each borough:")
    for cuisine, borough_scores in cuisine_scores.items():
        print(f"Cuisine: {cuisine}")
        for borough, scores in borough_scores.items():
            average_score = sum(scores) / len(scores)
            print(f"Borough: {borough} - Average Score: {average_score}")

    print("\nMinimum score for each type of cuisine in each borough:")
    for cuisine, borough_scores in cuisine_scores.items():
        print(f"Cuisine: {cuisine}")
        for borough, scores in borough_scores.items():
            min_score = min(scores)
            print(f"Borough: {borough} - Minimum Score: {min_score}")


json_file_path = 'restaurant.json'
with open(json_file_path, 'r', encoding='utf-8') as file:
    json_data = json.load(file)
    
calculate_scores(json_data)
