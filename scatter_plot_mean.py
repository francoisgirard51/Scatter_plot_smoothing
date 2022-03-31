# COMMENTS: This script plots the mean of the scatter plot of the data.

import numpy as np
import matplotlib.pyplot as plt

xy_data = np.loadtxt("data1.txt")

x=xy_data[0]
y=xy_data[1]

xx = x * x
xy = x * y

a = (np.mean(xy)-(np.mean(x)*np.mean(y)))/(np.mean(xx)-(np.mean(x)**2))

b = np.mean(y)- a * (np.mean(x))

xmin = np.min(x)
xmax = np.max(x)
ymin = a*xmin+b
ymax = a*xmax+b

plt.figure()
plt.plot(x, y, linestyle='none', marker='x')
plt.plot([xmin,xmax],[ymin,ymax], label='f(x) = ax + b' , c='red')
plt.legend()                                  
fig.show()