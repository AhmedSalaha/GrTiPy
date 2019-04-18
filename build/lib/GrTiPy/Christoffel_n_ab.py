import numpy as np 
from sympy import * 
def Christoffel_n_ab(d,x,g,ginverse,n,a,b):
    summation=0.0
    for i in range(d):
        summation= summation+ginverse[n][i]*(diff(g[i][a],x[b])+diff(g[i][b],x[a])-diff(g[a][b],x[i]))
        M= summation/2
    return M
