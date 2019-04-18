# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 00:12:59 2018

@author: Windows 7
"""

import numpy as np
from sympy import *
from sympy.matrices import Matrix
def Matric(d,x,y):
    for i in range(d):
        for j in range(d):
            m=diff(y,x[i]).dot(diff(y,x[j]))
            F=print("G(",x[i],",",x[j],")=",simplify(m))
    return F

d=2
R, theta, phi = symbols('R theta phi')
x=np.array([theta, phi])
y=Matrix([R*cos(theta)*cos(phi),R*cos(theta)*sin(phi), R*sin(theta)])
print(Matric(d,x,y))
