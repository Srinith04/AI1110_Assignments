#Importing numpy, scipy, mpmath and pyplot

from matplotlib import style
import numpy as np
import scipy 
import matplotlib.pyplot as plt

maxrange=50
maxlim=6.0
x = np.linspace(-6,6,50)#points on the x axis
x1 = np.linspace(-maxlim,maxlim,maxrange*2)
simlen = int(1e6) #number of samples
err = [] #declaring probability list

randvar = np.loadtxt('uni.dat',dtype='double')


#-----------------------For Practical CDF---------------------------------#

for i in range(0,50):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
plt.plot(x.T,err,color='red')#plotting the CDF

#--------------------------------------------------------------------------#


#-----------------------For Theoretical CDF--------------------------------#

def func_less0(x):
	return 0+x-x

def func_more1(x):
	return 1+x-x

def func(x):
	return x

x_1 = np.linspace(-maxlim,0,maxrange)
x_2 = np.linspace(0,1,maxrange)
x_3 = np.linspace(1,maxlim,maxrange)

plt.plot(x_1,func_less0(x_1),color='blue',linestyle='dashed')#plotting the CDF
plt.plot(x_2,func(x_2),color='blue',linestyle='dashed')#plotting the CDF
plt.plot(x_3,func_more1(x_3),color='blue',linestyle='dashed')#plotting the CDF

#--------------------------------------------------------------------------#


plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical","Theory"])

plt.title("Theoretical Vs Practical (CDF-Unifrom Random Variable)")
plt.savefig('../figs/unifrom_cdf.pdf')
plt.savefig('../figs/uniform_cdf.eps')
#plt.show()


