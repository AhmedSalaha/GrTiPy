import numpy as np 
from sympy import * 

def projection_tensor(d,g,u_sup):
    uscr = [[]for i in range(d)]
    uvv   = [[[] for l in range(d)] for k in range(d)] 
    HH    =  [[[] for l in range(d)] for k in range(d)] 

    for i in range(d):
        usum=0.0
        for j in range(d):
            usum=usum+g[i][j]*u_sup[j]
        uscr[i]=usum
    for i in range(d):
        for j in range(d):
            s= uscr[i]*uscr[j]
            uvv[i][j]=s
    for i in range(d):
        for j in range(d):
            h=g[i][j]+uvv[i][j]
            HH[i][j]=h
    for a in range(d):
        for b in range(d):
            HIJ=print("projection_tensor(", a, ",", b,")=",HH[a][b])
    return HIJ
    
