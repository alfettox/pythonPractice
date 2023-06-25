# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 14:57:28 2023

@author: dottd
"""

#Giovanni De Franceschi

import geopandas as gpd

file_path = "C:\dev\Wiley Edge\git\c320\Python\MontrealGeoJson\montreal.geojson"  # Replace with the actual file path
import geopandas as gpd

# Read the GeoJSON file
gdf = gpd.read_file(file_path)

# Print the entire GeoDataFrame
print(gdf)

# Access the geometry column
geometry = gdf['geometry']
print(geometry)

# Access a specific attribute column
prname = gdf['PRNAME']
print(prname)

# Plot the GeoDataFrame
gdf.plot()

# Select features based on a condition
selected = gdf[gdf['PRNAME'] == 'Quebec / Québec']
print(selected)

# Perform spatial operations
# Example: Find features that intersect a specific geometry
point = gpd.GeoSeries([geometry[0].representative_point()])
intersects = gdf[gdf.intersects(point.geometry[0])]
print(intersects)


gdf.plot(color='red', linewidth=0.5, alpha=0.7)
points.plot(ax=gdf.plot())
# Find features within a certain distance of a point
buffered_point = point.buffer(0.1)  # Buffer the point by 0.1 units
intersects = gdf[gdf.intersects(buffered_point)]

# Identify features that intersect a polygon
polygon = gpd.GeoDataFrame(geometry=[Polygon([(x1, y1), (x2, y2), (x3, y3), (x4, y4)])])
intersects = gdf[gdf.intersects(polygon.geometry[0])]

# Filter the GeoDataFrame based on attribute values
selected = gdf[gdf['PRNAME'] == 'Quebec / Québec']

# Calculate statistics
mean_population = gdf['population'].mean()
total_area = gdf['area'].sum()

# Group features by attributes
grouped = gdf.groupby('PRNAME').size()
