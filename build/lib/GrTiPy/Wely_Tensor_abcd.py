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
def Ricciscalar(d,x,g,ginverse):
    summation=0.0
    for a in range(d):
        for c in range(d):
            summation=summation+ginverse[a][c]*Ricci_Tensor_ab(d,x,g,ginverse,a,c)
    R=summation 
    Ricciscalar=R
    return Ricciscalar
    
def Wely_Tensor_abcd(d,x,g,ginverse,i,j,h,k):
    R1=Riemann_nabc(d,x,g,ginverse,i,j,h,k)
    l=(1/(d-2))
    R11 = g[i][h]*Ricci_Tensor_ab(d,x,g,ginverse,j,k)-g[j][h]*Ricci_Tensor_ab(d,x,g,ginverse,i,k)
    R22 = g[j][k]*Ricci_Tensor_ab(d,x,g,ginverse,i,h)-g[i][k]*Ricci_Tensor_ab(d,x,g,ginverse,j,h)
    m=1/((d-1)*(d-2))
    R2=Ricciscalar(d,x,g,ginverse)*(g[i][h]*g[j][k]-g[j][h]*g[i][k])
    wely=R1-l*(R11+R22)+m*(R2)
    return wely
