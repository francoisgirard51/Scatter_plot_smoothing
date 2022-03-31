#

import numpy as np
import matplotlib.pyplot as plt

xy_data = np.loadtxt("data1.txt")

x=xy_data[0]
y=xy_data[1]

a = (np.mean(xy)-(np.mean(x)*np.mean(y)))/(np.mean(xx)-(np.mean(x)**2))
b = np.mean(y)- a * (np.mean(x))

xmin = np.min(x)
xmax = np.max(x)
ymin = a*xmin+b
ymax = a*xmax+b

mean_x=[]
mean_y=[]
s=0.5
for i in np.arange(0,20,s):
    test1=x>=i 
    test2=x<i+s
    test=np.logical_and(test1,test2)
    x_filter=x[test]
    y_filter=y[test]
    mean_x_filter=np.mean(x_filter)
    mean_y_filter=np.mean(y_filter)
    mean_x.append(mean_x_filter)
    mean_y.append(mean_y_filter)

plt.figure()
plt.plot(x, y, linestyle='none', label='scatter plots x and y', marker='x', c='lightblue')
plt.plot([xmin,xmax],[ymin,ymax], label='f(x) = ax + b' , c='red')
plt.plot(mean_x, mean_y, label='mean dots', c='green', linestyle='none', marker='x')
plt.legend()                                  
fig.show()