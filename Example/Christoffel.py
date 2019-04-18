# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 17:43:35 2018

@author: Windows 7
"""
import numpy as np 
from sympy import * 


def Christoffel(d,g,ginverse):
    christoffel = [[[[]for k in range(d)] for j in range(d)] for i in range(d)]
    christoffel = [[[[]for k in range(d)] for j in range(d)] for i in range(d)]
    for n in range(d):
        for a in range(d):
            for b in range(d):
                summation=0.0
                for i in range(d):
                    summation= summation+ginverse[n][i]*(diff(g[i][a],x[b])+diff(g[i][b],x[a])-diff(g[a][b],x[i]))
                christoffel[n][a][b]=summation/2
    for n in range(0,d):
        for a in range(0,d):
            for b in range(0,d):
                M= print("christoffel[",x[n],",",x[a],",",x[b],"]=", simplify(christoffel[n][a][b]))
    return M

d=3
r,theta, phi= symbols('r theta phi')
x=np.array([r,theta, phi])
g00 = 1
g11 = r**2
g22 = r**2*sin(theta)**2
g=np.array([[g00,0,0],[0,g11,0],[0,0,g22]])
ginverse = np.array([[np.reciprocal(g00),0,0],[0,np.reciprocal(g11),0],[0,0,np.reciprocal(g22)]])

print(Christoffel(d,g,ginverse))
