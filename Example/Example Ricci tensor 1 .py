import numpy as np 
from sympy import * 
from GrTiPy import * 
d=4
r, theta, phi, t= symbols('r theta phi t')
c=symbols('c')
coor=np.array([ t, r, theta, phi])

U = Function('U')(r)
V = Function('V')(r)

g00 = U
g11 = -V
g22 = -r**2
g33 = -r**2*sin(theta)**2

g=np.array([[g00,0,0,0],[0,g11,0,0],\
            [0,0,g22,0],[0,0,0,g33]])
ginverse = np.array([[np.reciprocal(g00),0,0,0],[0,np.reciprocal(g11),0,0],[0,0,np.reciprocal(g22),0],[0,0,0,np.reciprocal(g33)]])

gin=inverse_metric(g)

Ricci_Tensor(d,coor,g,ginverse)
Ricci_scalar(d,coor,g,ginverse)

