import numpy as np
from sympy import *
def Laplacian_operator(d,x,g,ginverse):
    pro=1
    for i in range(d):
        pro=pro*g[i][i]
    sum=0
    for k in range(d):
        for i in range(d):
            sum=sum+(1/sqrt(pro))*(diff((sqrt(pro)*ginverse[k][i]*diff(psi,x[i])),x[k]))
    Lap=expand(sum)
    return Lap


d=4
psi= Function('psi')(t,r,theta,phi)
t, r,theta, phi,a,b,l,H= symbols('t r theta phi a b l H')
x=np.array([t, r,theta, phi])

g00 = -(1-a/r+b**2/r**2-H**2*r**2)
g11 = 1/(1-a/r+b**2/r**2-H**2*r**2)
g22 = r**2
g33 =r**2*sin(theta)**2

g=np.array([[g00,0,0,0],[0,g11,0,0],[0,0,g22,0],[0,0,0,g33]])

ginverse = np.array([[np.reciprocal(g00),0,0,0],[0,np.reciprocal(g11),0,0],[0,0,np.reciprocal(g22),0],[0,0,0,np.reciprocal(g33)]])


print(Laplacian_operator(d,x,g,ginverse))