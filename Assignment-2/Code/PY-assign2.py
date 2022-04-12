import cvxpy as cp

x = cp.Variable() 
y = cp.Variable()

constraints = [ 2*x + y <= 90 ,
                x + 2*y <= 80 ,
                  x + y <= 50 ,
                      x >= 0 ,
                      y >= 0 ]

obj = cp.Maximize( 48*x + 40*y)

prob = cp.Problem(obj , constraints)

prob.solve()

print("%f and %f"%(x.value,y.value))
