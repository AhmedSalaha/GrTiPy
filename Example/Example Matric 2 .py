import numpy as np
from sympy import *
from sympy.matrices import Matrix
from GrTiPy import *
d=2
r, theta, a = symbols('r theta a')
x=np.array([r, theta])
y=Matrix([r+theta,r-theta, (a/2)*((r+theta)**2-(r-theta)**2)])
Matric_coef(d,x,y)
