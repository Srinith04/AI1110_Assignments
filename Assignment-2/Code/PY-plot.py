import numpy as np
import matplotlib.pyplot as plt

def f1(x):
	return 90 - 2*x

def f2(x):
	return 40 - 0.5*x

def f3(x):
	return 50 - x
    
#The intercepts on x and y axis for the Lines are
# 2x + y = 90
x1,y1= 45,90   
# x + 2y = 80
x2,y2= 80,40
# x + y = 50
x3,y3= 50,50
# x = 0 ----> Y-AXIS
# y = 0 ----> X-AXIS

xmin = np.minimum(np.minimum(x1,x2),np.minimum(x2,x3))
ymin = np.minimum(np.minimum(y1,y2),np.minimum(y2,y3))

X = np.linspace(0,xmin,1000)
P = np.linspace(0,ymin,1000)

Y =np.minimum(np.minimum(f1(X),f2(X)),np.minimum(f3(X),f2(X)))

Y1 = np.zeros(1000)

plt.grid()

plt.plot(X, Y) # Minimum of the 3 graphs
 
plt.plot(X, Y1,color= "red") # X-AXIS

plt.plot(Y1, P,color = "green") # Y-AXIS

plt.fill_between(X, 0, Y, color='orange', alpha=1,label ="Feasible region") #Shading the feasible region.



x = []
y = []
with open("Points.txt","r") as fp:
    for lines in fp :
        x.append(lines[0:8])
        y.append(lines[10:-1])
x.remove(x[0])
y.remove(y[0])
for i in range(len(x)):
    x[i] = float(x[i])
    y[i] = float(y[i])

# To annoatate the point of intersections of lines and checking from graph 
# the vertices of feasible region

plt.scatter(x,y,c="black",s=10)

row = 10
col = 2
points = [[0 for i in range(col)] for j in range(row)] 

a=0
for i in x:
    points[a][0]=i
    a = a + 1
    
a=0
for i in y:
    points[a][1]=i
    a = a + 1

a = 0
s = ["$P_1$","$P_2$","$P_3$","$P_4$","$P_5$","$P_6$","$P_7$","$P_8$","$P_9$","$P_{10}$"]
for i in points:
    plt.annotate(s[a],i,xytext = (i[0], i[1]+2),size=10)
    a = a + 1

plt.legend()

plt.savefig("../Fig/plot2.png")
plt.show()
