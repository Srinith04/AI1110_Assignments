#Code by Dasari Srinith(cs21btech11015)

import numpy as np
from numpy import random as RN 

#Total number of cards in a deck of 52 cards are
N = 52
#Number of aces in the deck of 52 cards are
n_1 = 4
#Number of non - aces in the deck of 52 cards are
n_0 = N - n_1

# So , The Theoretical probabilities
pr_1 = n_1/N
pr_0 = n_0/N


# Let x take any value from 0 to 12 inclusive over the size N ,
x = RN.randint(0, 13, size=N)
# and if x = {0} , then we shall take the drawn card is an ace.
# and if x = {1,2,3,4,5,6,7,8,9,10,11,12} , then we shall take the drawn card is not an ace.

#Finding the number of numbers which are greater than or equal to 1.
x_0 = np.count_nonzero(x>=1)

#So ,number of numbers such that x=0 are
x_1 = N - x_0


print("Theoretical Probabilities that the drawn card is an ace and not an ace are respectively:", pr_1, pr_0)
print("Practical Probabilities that the drawn card is an ace and not an ace are respectively :", x_1/N, x_0/N)
