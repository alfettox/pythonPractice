# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 15:14:28 2023

@author: dottd
"""

import pandas as pd
import matplotlib.pyplot as plt


file_path = "c:/dev\Wiley Edge\git\c320\Python\SteamGamesPopularity/SteamCharts.csv"

df = pd.read_csv(file_path, encoding='latin-1')

# Print the entire DataFrame
print(df)

'''
# Access specific columns
game_name = df['gamename']
year = df['year']
month = df['month']
average_players = df['avg']
gain = df['gain']
peak_players = df['peak']
average_peak_percentage = df['avg_peak_perc']

# Perform data analysis or visualization
# Example: Calculate the maximum and minimum average players
max_players = average_players.max()
min_players = average_players.min()

# Example: Plot the average players over time
df.plot(x='month', y='avg', xlabel='Month', ylabel='Average Players', title='Average Players Over Time')

# Perform data manipulation or filtering
# Example: Select rows based on a condition
popular_games = df[df['peak'] > 10000]

# Example: Group data by a column and calculate statistics
monthly_average = df.groupby(['year', 'month'])['avg'].mean()

'''



# Group data by year and find the game(s) with the highest average players
most_played_games = df.groupby('year')['avg'].idxmax()  # Get the index of the row with the highest average players for each year
most_played_games_df = df.loc[most_played_games, ['year', 'gamename', 'avg']]  # Select the relevant columns for the most played games

# Plot the average players of the most played games over the years
plt.plot(most_played_games_df['year'], most_played_games_df['avg'], marker='o')
plt.xlabel('Year')
plt.ylabel('Average Players')
plt.title('Most Played Games - Average Players Over the Years')  # Add a title to the plot
plt.show()