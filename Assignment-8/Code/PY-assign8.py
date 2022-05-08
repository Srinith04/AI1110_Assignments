#Code by Dasari Srinith(cs21btech11015)

import numpy as np
from numpy import random as RN 

#Total number of cards in a deck of 52 cards are
T = 52
#Number of aces in the deck of 52 cards are
n_1 = 4
#Number of Kings in the deck of 52 cards are
n_0 = 4

# So , The Theoretical probabilities
pr_0 = n_0/T                           # pr(X=0)
pr_1 = n_1/T                           # pr(X=1)
pr_0_0 = (n_0-1)/(T-1)                 # pr((X=0)|(X=0))
pr_1_00 = n_1/(T-2)                    # pr((X=1)|(X=0)(X=0))

print("Theoretical Probability : ",pr_0 * pr_0_0 * pr_1_00)

#Let us consider 100 trials of picking 3 cards from deck without replacement.
N = 100

###For 1st Draw :

# Let x take any value from 0 to 12 inclusive over the size N ,
x = RN.randint(0, 13, size=N)
# and if x = {0} , then we shall take the drawn card to be a king.
# and if x = {12} , then we shall take the drawn card to be an ace.
# and for other values of x we shall take the drawn card to be other than ace or king.

x_0 = N - np.count_nonzero(x>=1)


###For 2st Draw :
###For calulating the pr((X=0)|(X=0)) let us take that in the first draw the card is a king. 
y = RN.randint(0, 51, size=N-1)
# and if y = {0,1,2} , then we shall take the drawn card to be a king.
# and if y = {3,4,5,6} , then we shall take the drawn card to be an ace.
# and for other values of y we shall take the drawn card to be other than ace or king.

y_0 = np.count_nonzero(y<=2)


###For 3st Draw :
###For calculating the pr((X=1)|(X=0)(X=0)) let us take that in the seccond draw also the card is king.
z = RN.randint(0, 50, size=N-2)
# and if z = {0,1} , then we shall take the drawn card to be a king.
# and if z = {2,3,4,5} , then we shall take the drawn card to be an ace.
# and for other values of z we shall take the drawn card to be other than ace or king.

z_0 = np.count_nonzero(z==2)+np.count_nonzero(z==3)+np.count_nonzero(z==4)+np.count_nonzero(z==5)


print("Practical Probability : ",(x_0/N)*(y_0/N-1)*(z_0/N-2))
