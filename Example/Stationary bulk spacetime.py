
import numpy as np 
from sympy import * 
from GrTiPy import * 

d=4

r=symbols('r')

t, r, theta, phi = symbols('t r theta phi')

x=np.array([t, r, theta, phi])


gg = Function('gg')(r)

a = Function('')(r)

b= Function('b')(r)

g00 = exp(2*gg)
g11 = -exp(2*gg+4*b)
g22 = -exp(2*b)
g33 = -exp(2*b)*sin(theta)**2


g=np.array([[g00,0,0,0],[0,g11,0,0],[0,0,g22,0],[0,0,0,g33]])

ginv=inverse_metric(g)

Ricci_Tensor(d,x,g,ginv)