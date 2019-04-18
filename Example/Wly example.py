import numpy as np 
from sympy import * 
from GrTiPy import * 
d=4
r,theta,varphi,t= symbols('r theta varphi t')

x=np.array([r, theta, varphi, t])
k= Function('k')(r,t)

g=np.array([[0,0,0,-1],[0,r**2,0,0],[0,0,r**2*sin(theta)**2,0],[-1,0,0,-2*k**2]])

gin=inverse_metric(g)

factor(Wely_Tensor_abcd(d,x,g,gin,0,1,1,3))