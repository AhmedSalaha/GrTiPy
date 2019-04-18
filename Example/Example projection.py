from GrTiPy import * 

d=4
m,x1= symbols('m x1')
a=-1

g00 = -a**2
g02 = -a**2*exp(x1)
g11 = a**2
g20 = -a**2*exp(x1)
g22 = -a**2*exp(2*x1)/2
g33 = a**2
g=np.array([[g00,0,g02,0],[0,g11,0,0],[g20,0,g22,0],[0,0,0,g33]])

u_sup=np.array([-1,0,0,0])

projection_tensor(d,g,u_sup)
        
 
