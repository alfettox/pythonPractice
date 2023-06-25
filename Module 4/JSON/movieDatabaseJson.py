# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 14:53:10 2023

@author: Giovanni De Franceschi

"""
import json;

def count_element(json_file):
    with open(json_file, 'r', encoding="utf-8") as file:
        data = json.load(file)
    return len(data)

def get_movie_year(json_file, movie_title):
    with open(json_file, 'r', encoding="utf-8") as file:
        data = json.load(file)
    for movie in data:
        if movie['title'] == movie_title:
            return movie['year']
    return None

def count_movies_director(json_file, director_name):
    with open(json_file, 'r', encoding="utf-8") as file:
        data = json.load(file)
    count = 0
    for movie in data:
        if director_name in movie['directors']:
            count += 1
    return count


def list_directors(json_file):
    with open(json_file, 'r', encoding="utf-8") as file:
        data = json.load(file)
    directors_list = set()
    for movie in data:
        for director in movie['directors']:
            trimmed_director = director.strip()
            directors_list.add(trimmed_director)
    return directors_list


#COUNT NUMBER OF ELEMENTS IN THE JSON

file_path = 'movies.json'
total_movies = count_element(file_path)
print(f"Number of movies: {total_movies}")


#FIND THE YEAR OF A SPECIFIC MOVIE
movie_title = 'A Separation'
movie_year = get_movie_year(file_path, movie_title)
if movie_year:
    print(f"The movie '{movie_title}' was made in: {movie_year}")
else:
    print("Movie not found")

#COUNT HOW MANY MOVIES A DIRECTOR HAS MADE
director_name = 'Martin Scorsese'
movies_director = count_movies_director(file_path, director_name)
print(f"Martin Scorsese has directed: {movies_director} movies")

#LIST DIRECTORS
directorsList = list_directors(file_path);

print('Directors:')
for direct in directorsList:
    print(direct);

