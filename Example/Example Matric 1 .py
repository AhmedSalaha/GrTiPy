import numpy as np
from sympy import *
from sympy.matrices import Matrix
from GrTiPy import *
d=2
R, theta, phi = symbols('R theta phi')
x=np.array([theta, phi])
y=Matrix([R*cos(theta)*cos(phi),R*cos(theta)*sin(phi), R*sin(theta)])
Matric_coef(d,x,y)



