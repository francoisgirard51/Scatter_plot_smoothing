# COMMENTS: This script plots the mean of the scatter plot of the data.

import numpy as np
import matplotlib.pyplot as plt

xy_data = np.loadtxt("data1.txt")

x=xy_data[0]
y=xy_data[1]

fig = plt.figure()
plt.plot(x, y, linestyle='none', marker='x')
fig.show()