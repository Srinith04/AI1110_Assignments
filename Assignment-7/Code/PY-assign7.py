#Code by Dasari Srinith(cs21btech11015)

# Checks and Prints the nature of example events taken in the solution .

#########################################

#Two events A,B are mutually exclusive if 
#  P(A U B) = P(A) + P(B)
#Events E1,E2,E3...En are exhaustive if 
#  P(E1 U E2 U E3 U ...U En) = 1

#########################################

import numpy as np
from numpy import random as RN 

N = 100

# Returns the Probability for N trials(here 100 times)
def P(x):
    return x/N

# Let us take a random variable x , which take any value from 1 to 8 inclusive over the size N ,
x = RN.randint(1, 9, size=N)
# and if x = {1} , then we shall take 000
# and if x = {2} , then we shall take 001
# and if x = {3} , then we shall take 010
# and if x = {4} , then we shall take 100
# and if x = {5} , then we shall take 011
# and if x = {6} , then we shall take 101
# and if x = {7} , then we shall take 110
# and if x = {8} , then we shall take 111

#NOTE : The initials of events are same as that of the solution.

###############################
#CASE 1:

A = np.count_nonzero(x==8)
B = np.count_nonzero(x==1)
A_or_B = np.count_nonzero(x==1) + np.count_nonzero(x==8)

if (P(A) + P(B) == P(A_or_B)):
    print("Events are mutually exclusive\n")
else:
    print("Wrong example taken\n")

##############################
#CASE 2:

C = np.count_nonzero(x==1)
D = np.count_nonzero(x==2) + np.count_nonzero(x==3) + np.count_nonzero(x==4)
E = np.count_nonzero(x>=5)
C_or_D_or_E = np.count_nonzero(x>=1)

if (P(C) + P(D) + P(E) == P(C_or_D_or_E)):
    if(P(C_or_D_or_E)==1):
        print("Events are mutually exclusive and exhaustive\n")
else:
    print("Wrong example taken\n")

###############################
#CASE 3:

F = np.count_nonzero(x==8)
G = np.count_nonzero(x>=5)
F_or_G = np.count_nonzero(x>=5)

if(P(F)+P(G) != P(F_or_G)):
    print("Events are not mutually exclusive\n")
else:
    print("Wrong example taken\n")

###############################
#CASE 4:

H = np.count_nonzero(x==8)
I = np.count_nonzero(x==1)
H_or_I = np.count_nonzero(x==1) + np.count_nonzero(x==8)

if(P(H)+P(I)==P(H_or_I)):
    if(P(H_or_I)!=1):
        print("Events are mutually exclusive but not exhaustive\n")
else:
    print("Wrong example taken\n")

###############################
#CASE 5:

J = np.count_nonzero(x==1)
K = np.count_nonzero(x==2) + np.count_nonzero(x==3) + np.count_nonzero(x==4)
L = np.count_nonzero(x==5) + np.count_nonzero(x==6) + np.count_nonzero(x==7)
J_or_K_or_L = np.count_nonzero(x<8)

if(P(J) + P(K) + P(L)==P(J_or_K_or_L)):
    if(P(J_or_K_or_L)!=1):
        print("Events are mutually exclusive but not exhaustive\n")
else:
    print("Wrong example taken\n")

###############################
