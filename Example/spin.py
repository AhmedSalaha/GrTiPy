 
import numpy as np 
from sympy import * 
from GrTiPy import * 

d=4
alpha,omaga=symbols(' alpha omaga')
t, r, theta, z= symbols('t  r theta z ')
u=np.array([t, r, theta, z])


g00 = -1
g02 = -alpha*omaga*r**2
g11 =  1
g20 =  -alpha*omaga*r**2
g22= alpha**2*r**2-alpha**2*omaga**2*r**4
g33 = 1

g=np.array([[g00,0,g02,0],[0,g11,0,0],[g20,0,g22,0],[0,0,0,g33]])

ginv=inverse_metric(g)

eta=np.array([[-1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
etain=inverse_metric(eta)
e=np.array([[1,0,-omaga*r,0],[0,1,0,0],[0,0,1/(alpha*r),0],[0,0,0,1]])
ein=inverse_metric(e)

Spin_connection(d,u,g,ginv,e,ein,eta,etain)
