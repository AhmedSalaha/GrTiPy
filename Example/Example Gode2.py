import numpy as np 
from sympy import * 
from GrTiPy import * 
d=4
x0, x1, x2, x3= symbols('x0 x1 x2 x3')
a=symbols('a')
coor=np.array([x0, x1, x2, x3])

g00 = -a**2
g02 = -a**2*exp(x1)
g11 =  a**2
g20 = -a**2*exp(x1)
g22 = -a**2*exp(2*x1)/2
g33 =  a**2

g=np.array([[g00,0,g02,0],[0,g11,0,0],\
            [g20,0,g22,0],[0,0,0,g33]])
gin=inverse_metric(g)

Christoffel(d,coor,g,gin)
Ricci_Tensor(d,coor,g,gin)
Ricci_scalar(d,coor,g,gin)
Einstein_Equation(d,coor,g,gin)
