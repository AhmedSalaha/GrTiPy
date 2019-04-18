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
                    summation= summation+ginverse[n][i]*(diff(g[i][a],x[b])+diff(g[i][b],x[a])-diff(g[a][b],x[i]))
                christoffel[n][a][b]=summation/2

    geod = [[]for k in range(d)]
    for i in range(d):
        sum=0.0
        for j in range(d):
            for k in range(d):
                sum =sum+christoffel[i][j][k]*f(x[j])*f(x[k]) 
        geod[i]=sum
        Ge=print("d",f(x[j]),"/ ds=",simplify(geod[i]))
    return Ge
    
    
d=4
t, r,theta, phi,a,b,l,H= symbols('t r theta phi a b l H')
x=np.array([t, r,theta, phi])

g00 = -(1-a/r+b**2/r**2-H**2*r**2)
g11 = 1/(1-a/r+b**2/r**2-H**2*r**2)
g22 = r**2
g33 =r**2*sin(theta)**2

g=np.array([[g00,0,0,0],[0,g11,0,0],[0,0,g22,0],[0,0,0,g33]])

ginverse = np.array([[np.reciprocal(g00),0,0,0],[0,np.reciprocal(g11),0,0],[0,0,np.reciprocal(g22),0],[0,0,0,np.reciprocal(g33)]])

print(Geodesics(d,x,g,ginverse))