from GrTiPy import * 

d=4
m,x= symbols('m x')

g=np.array([[-1,0,0,0],
            [0,exp(2*m*x)/2,0,exp(m*x)],
             [0,0,-1,0],[0,exp(m*x),0,-1]])

u_sup=np.array([0,0,0,1])

projection_tensor(d,g,u_sup)
        
gin=inverse_metric(g)

u = np.array([x, y, z, t])

print(expansion_scalar(d,u,g,gin,u_sup))