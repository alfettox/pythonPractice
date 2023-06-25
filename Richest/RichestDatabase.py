# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 15:29:36 2023

@author: dottd
"""
import pandas as pd
import matplotlib.pyplot as plt

file_path = "C:/dev/Wiley Edge/git/c320/Python/Richest/billionaireList.csv"


df = pd.read_csv(file_path, encoding='latin-1')

# Access specific columns
rank = df['rank']
name = df['name']
net_worth = df['net_worth (in billion $)']
age = df['age']
country = df['country / territory']
source = df['source']
industry = df['industry']

# Perform data analysis or visualization
# Example: Calculate the maximum and minimum net worth
max_net_worth = net_worth.max()
min_net_worth = net_worth.min()

# Example: Plot the net worth over age
df.plot(x='age', y='net_worth (in billion $)', kind='scatter', xlabel='Age', ylabel='Net Worth (in billion $)', title='Net Worth vs. Age')
plt.show()

# Perform data manipulation or filtering
# Example: Select billionaires from a specific country
italy_billionaires = df[df['country / territory'] == 'Italy']
print("Italy Billionaires:")
print(italy_billionaires)

# Example: Find the most rewarding sector
most_rewarding_sector = df['industry'].value_counts().idxmax()
print("Most Rewarding Sector:", most_rewarding_sector)