import numpy as np 
from sympy import * 
import numpy as np
from sympy import *
from GrTiPy.Det import Det as Det 
from GrTiPy.Det import Det
import GrTiPy.Det as Det
omega, pi= symbols('omega pi')

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
    
def Einstein_Equation_ab(d,x,g,ginverse,a,b):
    En=Ricci_Tensor_ab(d,x,g,ginverse,a,b)-(1/2)*Ricciscalar(d,x,g,ginverse)*g[a][b]
    return En

def Laplacian_operator(d,x,g,ginverse,psi):
    pro=-Det(g)
    sum=0
    for k in range(d):
        for i in range(d):
            sum=sum+(1/sqrt(pro))*(diff((sqrt(pro)*ginverse[k][i]*diff(psi,x[i])),x[k]))
    Lap=expand(sum)
    return Lap
def der(d,psi,x):
    summ =0.0
    for a in range(d):
        for b in range(d):
            summ=summ+diff(psi,x[a])*diff(psi,x[b])
    f=summ
    return f
def Brans_Dicke_Equations_ab(d,x,g,ginverse,psi,a,b):
    Bran =  Einstein_Equation_ab(d,x,g,ginverse,a,b)+(omega/psi**2)*(diff(psi,x[a])*diff(psi,x[b])-0.5*g[a][b]*der(d,psi,x))-(1/psi)*(diff(psi,x[a],x[b])-g[a][b]*Laplacian_operator(d,x,g,ginverse,psi))
    return Bran