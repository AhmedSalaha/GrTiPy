import numpy as np 
from sympy import * 

def Christoffel_n_ab(d,x,g,ginverse,n,a,b):
    summation=0.0
    for i in range(d):
        summation= summation+ginverse[n][i]*(diff(g[i][a],x[b])+diff(g[i][b],x[a])-diff(g[a][b],x[i]))
        M= summation/2
    return M

def Riemann_nabc(d,x,g,ginverse,n,a,b,c):
    parials=diff(Christoffel_n_ab(d,x,g,ginverse,n,a,c),x[b])-diff(Christoffel_n_ab(d,x,g,ginverse,n,a,b),x[c])
    summation=0.0
    for i in range(d):
        summation=summation+Christoffel_n_ab(d,x,g,ginverse,n,b,i)*Christoffel_n_ab(d,x,g,ginverse,i,a,c)-Christoffel_n_ab(d,x,g,ginverse,n,c,i)*Christoffel_n_ab(d,x,g,ginverse,i,a,b)
    Rie = parials+ summation 
    return Rie

def Ricci_Tensor_ab(d,x,g,ginverse,a,c):
    summation=0.0
    for i in range(d):
        summation=summation+Riemann_nabc(d,x,g,ginverse,i,a,i,c)
    RiiR=simplify(summation)
    return RiiR
