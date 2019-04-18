import numpy as np 
from sympy import * 
from GrTiPy import * 
d=4
t, r, theta, phi= symbols('t r theta phi')
k=symbols('k')
coor=np.array([t, r, theta, phi])

a = Function('a')(t)
g00 =   1
g11 =  -a**2/(1-r**2/k**2)
g22 =  -a**2*r**2
g33 =  -a**2*r**2*sin(theta)**2

g=np.array([[g00,0,0,0],[0,g11,0,0],\
            [0,0,g22,0],[0,0,0,g33]])
gin=inverse_metric(g)

Einstein_Equation(d,coor,g,gin)
