# Code by Dasari Srinith
# March 30 ,2022
# To verify the roots of x^2 +7x -7 = 0 are x=-7.89, x=0.89(rounded to two decimals)
# by plotting its graph.

import matplotlib.pyplot as plt
import numpy as np

def func(x,a,b,c):
	return a*x**2+b*x+c

# coeffs are the coefficients of the quadratic equation.
coeffs = [1,7,-7]
# Roots are roots of the quadratic equation.
Roots = np.roots(coeffs)
Roots = np.round(Roots,2)  # Rounded off to two decimals

x_values = np.linspace(-10,10,1000)
# Only from -10 to 10 is enough as f(-10) and f(10) are positive
# and f(0) is negative implying both roots are between -10 and 10
y_values = func(x_values,1,7,-7)

x_axis = np.zeros(1000)
plt.plot(x_values,x_axis,color="blue")  # Can be considered as X-Axis

y_axis = np.linspace(min(y_values), max(y_values), 1000)
plt.plot(x_axis, y_axis,color="blue")   # Can be considered as Y-Axis

plt.plot(x_values, y_values,color="red")   # Graph of the Quadratic equation

points = [*[(a, 0) for a in Roots]]
for a in points:
	plt.annotate(str(a), a, xytext=(a[0]+0.1,a[1]+5))
# So, That the solutions can be seen and verified on the plot

plt.savefig("../Fig/plot.png")
plt.show()
