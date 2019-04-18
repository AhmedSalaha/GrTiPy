import numpy as np 
from sympy import * 
def Christoffel_All(d,x,g,ginverse):
    christoffel = [[[[]for k in range(d)] \
                     for j in range(d)] for i in range(d)]
    christoffel = [[[[]for k in range(d)] \
                     for j in range(d)] for i in range(d)]
    for n in range(d):
        for a in range(d):
            for b in range(d):
                summation=0.0
                for i in range(d):
                    summation= summation+\
                    ginverse[n][i]*(diff(g[i][a],x[b])+diff(g[i][b],x[a])-diff(g[a][b],x[i]))
                christoffel[n][a][b]=summation/2
    for n in range(0,d):
        for a in range(0,d):
            for b in range(0,d):
                M= print("christoffel[",x[n],",",x[a],",",x[b],"]="\
                         , expand(simplify(christoffel[n][a][b])))
    return M
