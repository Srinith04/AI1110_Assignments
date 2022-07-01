#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import scipy 
import matplotlib.pyplot as plt



maxrange=50
maxlim=6.0
x = np.linspace(-maxlim,maxlim,maxrange) #points on the x axis for practical
x1 = np.linspace(-maxlim,maxlim,maxrange*2) #points on the x axis for theoretical
simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list


randvar = np.loadtxt('uni.dat',dtype='double') # Data


#-----------------------For Practical PDF---------------------------------#

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list

plt.plot(x[0:(maxrange-1)].T,pdf,'o')

#--------------------------------------------------------------------------#


#-----------------------For Theoretical PDF--------------------------------#

def uniform_pdf(x):
	if (x <= 0):
		return 0
	else :
		if (x > 1):
			return 0
		else :
			return 1
	
vec_uniform_pdf = scipy.vectorize(uniform_pdf)

plt.plot(x1,vec_uniform_pdf(x1))#plotting the CDF

#--------------------------------------------------------------------------#


plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend(["Numerical","Theory"])

plt.title("Theoretical Vs Practical (PDF-Unifrom Random Variable)")
plt.savefig('../figs/uni_pdf.pdf')
plt.savefig('../figs/uni_pdf.eps')
