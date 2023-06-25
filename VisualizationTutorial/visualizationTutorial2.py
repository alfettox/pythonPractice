# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 15:56:52 2023

@author: dottd
"""

import matplotlib.pyplot as plot
import numpy as np
 
list1 = [4, 3, 3, 3, 1, 3, 0, 4, 0, 4, 4, 0, 3, 1, 1] 
list2 = [3, 0, 1, 2, 2, 0, 0, 0, 0, 3, 3, 2, 3, 4, 1]
 
fig, axs = plot.subplots(1, 2, figsize=(15, 5)) 
 
axs[0].hist(list1) 
axs[1].hist([list2]) 
 
plot.show()

#SCATTER PLOT

import matplotlib.pyplot as plot
import numpy as np
 
np.random.seed(9999) #create a custom seed for generating random numbers 
data = np.random.randn(2, 999) #create a numpy matrix of 2x100 of random numbers
print(data)
 
plot.scatter(data[0], data[1]) #create the scatter plot using the first 100 values as x and second 100 values as y 
plot.show()

#HISTOGRAM 2D PLOT
import matplotlib.pyplot as plot
import numpy as np
 
np.random.seed(19680801)
data = np.random.randn(2, 900)
 
plot.hist2d(data[0], data[1]) 
 
plot.show()


#PIE
import matplotlib.pyplot as plot
 
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = ['Electronics', 'Clothing', 'Home Goods', 'Cleaning Supplies']
sizes = [15, 30, 45, 10]
explode = (0, .25, 0, 0)  # only "explode" the 2nd slice (i.e. 'Clothing')
 
plot.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
plot.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plot.show()


#COMBINED
import matplotlib.pyplot as plt
import numpy as np
 
np.random.seed(19680801)
data = np.random.randn(2, 100)
 
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
axs[0, 0].hist(data[0])
axs[1, 0].scatter(data[0], data[1])
axs[0, 1].plot(data[0], data[1])
axs[1, 1].hist2d(data[0], data[1])
 
plt.show()