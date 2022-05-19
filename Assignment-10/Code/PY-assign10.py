#Code by Dasari Srinith(cs21btech11015)

import numpy as np
from scipy.stats import binom

n = 4
p = 1/3

mean = binom.stats(n, p, moments='m')

print(mean)
