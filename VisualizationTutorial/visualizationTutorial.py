# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 15:56:52 2023

@author: dottd
"""

import matplotlib.pyplot as plot
import numpy as np

#LINE PLOT

x =["Ford", "Mazda", "Toyota", "Dodge", "Chrisler"]
y = [0, 3, 2, 5, 4]

plot.plot(x,y,color='green', marker='o',linestyle='dashed')

plot.show();


#LINE CHART
import matplotlib.pyplot as plt

x = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
y = [11, 5, 6, 4, 2, 8, 7, 9, 4, 6, 7, 1]

plt.plot(x, y, color='red', marker='x', linestyle='-')

plt.xlabel('Month')
plt.ylabel('Value')
plt.title('Sells')

plt.show()

#HISTOGRAM PLOT

plt.hist(y, bins=len(y), rwidth=0.8)

plot.show()