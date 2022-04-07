# Code by Dasari Srinith
# March 30 ,2022
# To plot the graph of x^2 +7x -7 = 0.

import numpy as np
from math import sqrt
from matplotlib import pyplot as plt


def f(x):
     return (x**2+7*x-7)


x = []
y = []
with open("Data.txt","r") as fp:
    for lines in fp :
        x.append(lines[0:8])
        y.append(lines[10:-1])
x.remove(x[0])
y.remove(y[0])
for i in range(len(x)):
    x[i] = float(x[i])
    y[i] = float(y[i])
plt.grid()
plt.plot(x,y,color="red",label = 'y=f(x)')
x_values = np.linspace(-10,10,1000)
x_axis = np.zeros(1000)
plt.plot(x_values,x_axis,color="blue",label = "X-Axis")  # Can be considered as X-Axis

# coeffs are the coefficients of the quadratic equation.
coeffs = [1,7,-7]
# Roots are roots of the quadratic equation.
Roots = np.roots(coeffs)
Roots = np.round(Roots,2)  # Rounded off to two decimals

plt.plot(Roots[0],0,marker='o',markersize=4,markerfacecolor='Black',markeredgecolor='Black')
plt.plot(Roots[1],0,marker='o',markersize=4,markerfacecolor='Black',markeredgecolor='Black')
plt.annotate((Roots[0],0),(Roots[0],0),(-7.5,1.5))
plt.annotate((Roots[1],0),(Roots[1],0),(1.5,1.5))
plt.legend()

plt.savefig("../Fig/_plot.png")
plt.show()
