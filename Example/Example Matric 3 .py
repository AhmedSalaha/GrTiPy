import numpy as np
from sympy import *
from sympy.matrices import Matrix
from GrTiPy import *
d=2
c, u, v = symbols('c u v')
x=np.array([u, v])
y=Matrix([(c*cosh(v/c)*cos(u),c*cosh(v/c)*sin(u),v)])
Matric_coef(d,x,y)
