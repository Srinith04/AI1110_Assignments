#Code by Dasari Srinith(cs21btech11015)

import numpy as np
from numpy import random as RN 

#Let us consider 1000 people
N = 1000

## The data from the quesiton can be written as,

# When 1000 people who have disease take test ,990 people get positive.
n_1_1 = 990
# When 1000 healthy people take test ,5 person gets positive.
n_1_0 = 5
# When 1000 random people are taken ,1 person has disease
n_1 = 1

# So , For Theoretical probabilities
pr_1 = n_1/N                           # pr(X=1)
pr_0 = 1 - pr_1                        # pr(X=0)
pr_1_1 = n_1_1/N                       # pr((Y=1)|(X=1))
pr_1_0 = n_1_0/N                       # pr((Y=1)|(X=0))

print("Theoretical Probability for pr((X=1)|(Y=1)): ",(pr_1 * pr_1_1)/((pr_1 * pr_1_1) + (pr_0 * pr_1_0)))


# Let x take any value from 1 to 1000 inclusive over the size N ,
x = RN.randint(1, 1001, size=N)
# and if x = {1} , then we shall take that the person has disease
# and if x = {2,3,4,...,1000} , then we shall take the person has no disease

x_1 = np.count_nonzero(x==1)    # Who have disease
x_0 = N - x_1                   # Who dont have disease

# Let y1 take any value from 1 to 1000 inclusive over the size N ,
y1 = RN.randint(1, 1001, size=N)
# and if y1 = {1,2,3,...,990} , then we shall take that the blood test for people who have disease is positive
# and if y1 = {991,992,993,...,1000} , then we shall take the blood test for people who have disease is not positive

y1_1 = np.count_nonzero(y1<=990)   # Blood test is positive
y1_0 = N - y1_1                    # Blood test is negative 


# Let y2 take any value from 1 to 1000 inclusive over the size N ,
y2 = RN.randint(1, 1001, size=N)
# and if y2 = {1,2,3,4,5} , then we shall take that the blood test for healthy people is positive 
# and if y2 = {6,7,8,...,1000} , then we shall take the blood test for healthy people is not positive

y2_1 = np.count_nonzero(y2<=5)    # Blood test is positive
y2_0 = N - y2_1                   # Blood test is negative


print("Practical Probability : ",((x_1/N) * (y1_1/N))/(((x_1/N) * (y1_1/N)) + ((x_0/N) * (y2_1/N))))
