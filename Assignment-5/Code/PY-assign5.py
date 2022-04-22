#Code by Dasari Srinith (cs21btech11015)

import numpy as np
import pandas as pd
from numpy import random as RN 

# Importing data from excel

read = pd.read_excel(r'assign5/data.xlsx')
raw_data = np.array(read)

# It is given that data was taken from 40 students , so sample space ,
N = 40

freqency = np.array(raw_data[1])

pr_7 = freqency[7]/N

print("Probability that a student was born in August from data is ",pr_7)

x = RN.randint(0, 12, size=N)

x_7 = np.count_nonzero(x==7)

print("Experimental Probability that a student was born in August is ",x_7/N)
