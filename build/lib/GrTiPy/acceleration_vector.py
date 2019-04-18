import numpy as np
from sympy import *

def U_i(d,g,V,i):
    uu=0.0
    for j in range(d):
        uu=uu+V[j]*g[i][j]
    us=uu
    return us
    
def Christoffel_n_ab(d,x,g,ginverse,n,a,b):
    summation=0.0
    for i in range(d):
        summation= summation+ginverse[n][i]*(diff(g[i][a],x[b])+diff(g[i][b],x[a])-diff(g[a][b],x[i]))
        M= summation/2
    return M

def acceleration_vector(d,x,g,ginverse,V,i):
    acc=0.0
    for j in range(d):
        acc=acc+diff(U_i(d,g,V,i),x[j])
    sec=0.0
    for j in range(d):
        for k in range(d):
            sec=sec+Christoffel_n_ab(d,x,g,ginverse,k,i,j)*U_i(d,g,V,k)
    accel=(acc-sec)*V[i]
    return accel
