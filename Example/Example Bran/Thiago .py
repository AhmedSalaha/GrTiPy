from GrTiPy import * 

d=4
t, r, theta, phi= symbols('t  r theta phi ')
u=np.array([t, r, theta, phi])
n, rho, P, pi, omega=symbols(' n rho P pi omega')


gamma = Function('gamma')(r)
alpha = Function('alpha')(r)
beta = Function('beta')(r)
phi = Function('phi')(r)

g00 =   exp(2*gamma)
g11 =  -exp(2*alpha)
g22 =  -exp(2*beta)
g33 =  -exp(2*beta)*sin(theta)**2

g=np.array([[g00,0,0,0],[0,g11,0,0],\
            [0,0,g22,0],[0,0,0,g33]])
gin=inverse_metric(g)

for i in range(d):
    for j in range(d):
        for k in range(d):
            if Christoffel_n_ab(d,u,g,gin,i,j,k) !=0:
                print("G(", u[i] ,u[j],u[k], ")="\
                         , simplify(Christoffel_n_ab(d,u,g,gin,i,j,k)))

def R(d,u,g,gin,a,b):
    sum=0.0
    for i in range(d):
        sum=sum+gin[a][i]*Ricci_Tensor_ab(d,u,g,gin,i,b)
    return sum
    

def G(d,u,g,gin,a,b):
    SumG=0.0
    for i in range(d):
        SumG=SumG+gin[a][i]*Einstein_Equation_ab(d,u,g,gin,a,b)    
    return SumG
