import numpy as np 
from sympy import * 
from GrTiPy import * 


Lambda, rho, P, pi, omega=symbols(' Lambda rho P pi omega')
d=5
t, r,theta,varphi,psi= symbols('t r theta varphi psi')

x=np.array([t, r, theta, varphi,psi])
Lambda, rho, P, pi, omega=symbols(' Lambda rho P pi omega')
a= Function('a')(t)
phi= Function('phi')(t)

g00 = 1
g11 = - a**2
g22 = - a**2*r**2
g33 = - a**2*r**2*sin(theta)**2
g44 = - a**2

g=np.array([[g00,0,0,0,0],[0,g11,0,0,0],[0,0,g22,0,0],[0,0,0,g33,0],[0,0,0,0,g44]])

ginverse = np.array([[np.reciprocal(g00),0,0,0,0],[0,np.reciprocal(g11),0,0,0],[0,0,np.reciprocal(g22),0,0],[0,0,0,np.reciprocal(g33),0],[0,0,0,0,np.reciprocal(g44)]])

T=np.array([[-rho,0,0,0,0],[0,P,0,0,0],[0,0,P,0,0],[0,0,0,P,0],[0,0,0,0,P]])

print(Scalar_Brans_Dicke_field_Equation(d,x,g,ginverse,phi,T))

