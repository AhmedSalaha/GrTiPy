import numpy as np 
from sympy.matrices import Matrix
from sympy import * 
from GrTiPy import * 
def Div(d,g,x,V):
    pro=1
    for i in range(d):
        pro=pro*g[i][i]
    Summ=0.0
    for i in range(d):
        Summ=Summ+1/sqrt(pro)*diff(pro*V[i],x[i])
    LL=print("Div.V=",simplify(Summ))
    return LL
