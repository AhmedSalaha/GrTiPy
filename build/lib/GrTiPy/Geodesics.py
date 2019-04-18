import numpy as np 
from sympy import * 


def Geodesics(d,x,g,ginverse):
    christoffel = [[[[]for k in range(d)] for j in range(d)] for i in range(d)]

    f= symbols('f')                         
    for n in range(d):
        for a in range(d):
            for b in range(d):
                summation=0.0
                for i in range(d):
                    summation= summation+\
                    ginverse[n][i]*(diff(g[i][a],x[b])+diff(g[i][b],x[a])-\
                    diff(g[a][b],x[i]))
                christoffel[n][a][b]=summation/2

    geod = [[]for k in range(d)]
    for i in range(d):
        sum=0.0
        for j in range(d):
            for k in range(d):
                sum =sum+christoffel[i][j][k]*f(x[j])*f(x[k]) 
        geod[i]=-sum
        Ge=print("d",f(x[i]),"/ ds=",simplify(geod[i]))
    return Ge
    
