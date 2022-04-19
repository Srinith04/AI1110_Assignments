#Code by Dasari Srinith(cs21btech11015)

import numpy as np
from numpy import random as RN 

#Total number of days for which data was available
N = 250
#Number of days the forecast was correct
n_0 = 175
#Number of days the forecast was wrong
n_1 = 75

# So , The Theoretical probabilities
pr_0 = n_0/N
pr_1 = n_1/N


# Let x take any value from 0 to 9 inclusive over the size N ,
x = RN.randint(0, 10, size=N)
# and if x = {3,4,5,6,7,8,9} , then we shall take the forecast to be correct on that day.
# and if x = {0,1,2} , then we shall take the forecast to be wrong on that day.

#Finding the number of numbers which are greater than or equal to 3.
x_0 = np.count_nonzero(x>=3)

#So ,number of numbers such that x=0,x=1,x=2 are
x_1 = N - x_0


print("Theoretical Probabilities:", pr_0, pr_1)
print("Practical Probabilities:", x_0/N, x_1/N)
