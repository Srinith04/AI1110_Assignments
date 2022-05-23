#Code By Dasari Srinith(cs21btech11015)

import matplotlib.pyplot as plt
import numpy as np
from math import comb

def func(x):
    sum = 0
    for i in range(x+1):
        sum = sum + i*comb(x,i)*((1/3)**i)*((2/3)**(x-i))
    
    return sum


x = np.linspace(0,10,11)

y = [0] * 11

for a in range(11):
    y[a] = func(a)
    
    
plt.grid()
plt.plot(x,y,marker='o',label='Plot for closed form')
plt.plot(x, x/3,linestyle='dashed', marker=None, label='Plot for expression')

plt.legend()
plt.show()
