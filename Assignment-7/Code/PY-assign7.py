#Code by Dasari Srinith(cs21btech11015)

#########################################

#Two events A,B are mutuallu exclusice if 
#  P(A U B) = P(A) + P(B)
#Events E1,E2,E3...En are exhaustive if 
#  P(E1 U E2 U E3 U ...U En) = 1

#########################################

import numpy as np
from scipy.stats import binom

N = 100

def P(x):
    return x/N

#Number of times coin is tosses
n = 3

#Probability of favourable outcome(Here ,getting Head)
p = 0.5

x = binom.rvs(n,p,size=N)

#NOTE : The initials of events are same as that of the solution.

###############################
#CASE 1:

A = np.count_nonzero(x==3)
B = np.count_nonzero(x==0)
A_or_B = np.count_nonzero(x==0) + np.count_nonzero(x==3)

if (P(A) + P(B) == P(A_or_B)):
    print("Events are mutually exclusive\n")
else:
    print("Wrong example taken\n")

##############################
#CASE 2:

C = np.count_nonzero(x==0)
D = np.count_nonzero(x==1)
E = np.count_nonzero(x>=2)
C_or_D_or_E = np.count_nonzero(x>=0)

if (P(C) + P(D) + P(E) == P(C_or_D_or_E)):
    if(P(C_or_D_or_E)==1):
        print("Events are mutually exclusive and exhaustive\n")
else:
    print("Wrong example taken\n")

###############################
#CASE 3:

F = np.count_nonzero(x==3)
G = np.count_nonzero(x>=2)
F_or_G = np.count_nonzero(x>=2)

if(P(F)+P(G) != P(F_or_G)):
    print("Events are not mutually exclusive\n")
else:
    print("Wrong example taken\n")

###############################
#CASE 4:

H = np.count_nonzero(x==3)
I = np.count_nonzero(x==0)
H_or_I = np.count_nonzero(x==0) + np.count_nonzero(x==3)

if(P(H)+P(I)==P(H_or_I)):
    if(P(H_or_I)!=1):
        print("Events are mutually exclusive but not exhaustive\n")
else:
    print("Wrong example taken\n")

###############################
#CASE 5:

J = np.count_nonzero(x==0)
K = np.count_nonzero(x==1) 
L = np.count_nonzero(x==2)
J_or_K_or_L = np.count_nonzero(x<=2)

if(P(J) + P(K) + P(L)==P(J_or_K_or_L)):
    if(P(J_or_K_or_L)!=1):
        print("Events are mutually exclusive but not exhaustive\n")
else:
    print("Wrong example taken\n")

###############################
