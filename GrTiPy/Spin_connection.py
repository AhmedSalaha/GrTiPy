import numpy as np 
from sympy import * 



def Spin_connection(d,x,g,ginv,e,ein,eta):
    omag = [[[[]for k in range(d)] for j in range(d)] for i in range(d)]
    christoffel = [[[[]for k in range(d)] for j in range(d)] for i in range(d)]
    Sec = [[[[]for k in range(d)] for j in range(d)] for i in range(d)]
    for n in range(d):
        for a in range(d):
            for b in range(d):
                summation=0.0
                for i in range(d):
                    summation= summation+ginv[n][i]*(diff(g[i][a],x[b])+diff(g[i][b],x[a])-diff(g[a][b],x[i]))
                christoffel[n][a][b]=summation/2
    for n in range(d):
        for a in range(d):
            for b in range(d):
                s1=0.0
                for c in range(d):
                    for v in range(d):
                        s1=s1+eta[a][c]*e[v][b]*diff(ein[c][v],x[n])
                Sec=s1
    for n in range(d):
        for a in range(d):
            for b in range(d):
                summ=0.0
                for c in range(d):
                    for v in range(d):
                        for s in range(d):
                            summ=summ+(eta[a][c]*e[c][v]*ein[s][b]*christoffel[v][s][n])
                omag[n][a][b]=summ-Sec
    for n in range(d):
        for a in range(d):
            for b in range(d):
                M= print("omag[",x[n],",",x[a],",",x[b],"]=", simplify(omag[n][a][b]))
    return M