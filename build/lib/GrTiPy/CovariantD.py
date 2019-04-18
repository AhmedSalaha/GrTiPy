import numpy as np 
from sympy import * 
def Christoffel_n_ab(d,x,g,ginverse,n,a,b):
    summation=0.0
    for i in range(d):
        summation= summation+ginverse[n][i]*(diff(g[i][a],x[b])+diff(g[i][b],x[a])-diff(g[a][b],x[i]))
        M= summation/2
    return M


def CovariantD(d,u,g,gin,V,a,b):
    Ca=diff(V[a],u[b])
    sa=0.0
    for j in range(d):
        sa=sa+Christoffel_n_ab(d,u,g,gin,a,b,j)*V[j]
    Caa=Ca+sa
    return Caa