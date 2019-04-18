import numpy as np
from sympy import *
from GrTiPy.Det import Det as Det 
from GrTiPy.Det import Det
import GrTiPy.Det as Det

def Laplacian_operator(d,x,g,ginverse,psi):
    pro=-Det(g)
    sum=0
    for k in range(d):
        for i in range(d):
            sum=sum+(1/sqrt(pro))*(diff((sqrt(pro)*ginverse[k][i]*diff(psi,x[i])),x[k]))
    Lap=expand(sum)
    return Lap