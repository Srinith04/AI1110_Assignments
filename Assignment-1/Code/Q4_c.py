# Code by Dasari Srinith
# March 30 ,2022
# To verify the roots of x^2 +7x -7 = 0 are x=-7.89, x=0.89(rounded to two decimals)
# by plotting its graph.

import matplotlib.pyplot as plt
import numpy as np

# coeffs are the coefficients of the quadratic equation.
coeffs = [1,7,-7]
# Roots are roots of the quadratic equation.
Roots = np.roots(coeffs)
Roots = np.round(Roots,2)  # Rounded off to two decimals

x_values = np.linspace(-10,10,1000)
# Only from -10 to 10 is enough as f(-10) and f(10) are positive
# and f(0) is negative implying both roots are between -10 and 10
y_values = x_values**2 + 7*x_values - 7

x_axis = np.zeros(1000)
plt.plot(x_values,x_axis,color="blue")  # Can be considered as X-Axis

y_axis = np.linspace(min(y_values), max(y_values), 1000)
plt.plot(x_axis, y_axis,color="blue")   # Can be considered as Y-Axis

plt.plot(x_values, y_values,color="red",label ="Graph of $x^2-7x+7=0$")   # Graph of the Quadratic equation

plt.legend()
plt.annotate("X-AXIS",(7.5,-10))
plt.annotate("Y-AXIS",(0.3,150))
plt.plot(Roots[0],0,marker='o',markerfacecolor='Black',markeredgecolor='Black')
plt.plot(Roots[1],0,marker='o',markerfacecolor='Black',markeredgecolor='Black')
plt.annotate((Roots[0],0),(Roots[0],0),(Roots[0],4))
plt.annotate((Roots[1],0),(Roots[1],1),(Roots[1],-8))
# So, That the solutions can be seen and verified on the plot

plt.savefig("../Fig/_plot_.png")
plt.show()
