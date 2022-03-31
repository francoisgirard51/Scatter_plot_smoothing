# COMMENTS: The function 𝑓(𝑥)=𝐵𝑥𝑎+𝐶 therefore gives an approximate value
# of the 𝑦𝑖 as a function of the 𝑥𝑖.

import numpy as np
import matplotlib.pyplot as plt

xy_data = np.loadtxt("data2.txt")

x=xy_data[0]
y=xy_data[1]

C = np.min(y)-10
v = np.log(x)
w = np.log(y-C)

vw = v * w
vv = v**2

Mv = np.mean(v)
Mvv = np.mean(vv)
Mw = np.mean(w)
Mvw = np.mean(vw)
B = np.exp(b)

a = (Mvw - Mv*Mw) / (Mvv - (Mv)**2)
b = Mw - a*Mv

print('value a =', a)
print('value B =', B)
print('value C =', C)

t = np.arange(1, 100, 1)
u = B * np.power(t, a) + C
                     
plt.figure()
plt.plot(x, B*np.power(x, a) + C, label='function f(t)', c='red')
plt.plot(x, y, linestyle='none', label='scatter plots', marker='x')
plt.legend()                                  
fig.show()