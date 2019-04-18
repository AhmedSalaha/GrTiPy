import numpy as np 
from sympy import * 
def Brans_Dicke_Equations(d,x,g,ginverse,psi,T):
    christoffel = [[[[]for k in range(d)] for j in range(d)] for i in range(d)]

    for n in range(d):
        for a in range(d):
            for b in range(d):
                summation=0.0
                for i in range(d):
                    summation= summation+ginverse[n][i]*(diff(g[i][a],x[b])+diff(g[i][b],x[a])-diff(g[a][b],x[i]))
                christoffel[n][a][b]=summation/2
        outpu=np.array(christoffel[n])    

    Riemann= [[[[[] for l in range(d)] for k in range(d)] for j in range(d)] for i in range(d)]

    for n in range(d):
        for a in range(d):
            for b in range(d):
                for c in range(d):
                    parials=diff(christoffel[n][a][c],x[b])-diff(christoffel[n][a][b],x[c])
                    summation=0.0
                    for i in range(d):
                        summation=summation+christoffel[n][b][i]*christoffel[i][a][c]-christoffel[n][c][i]*christoffel[i][a][b]
                    Riemann[n][a][b][c]=parials+summation

    Ricci =[[[] for j in range(d)] for i in range(d)]

    for a in range(d):
        for c in range(d):
            summation=0.0
            for i in range(d):
                summation=summation+simplify(Riemann[i][a][i][c])
            Ricci[a][c]=simplify(summation)


    summation=0.0        
    for a in range(d):
        for c in range(d):
            summation=summation+ginverse[a][c]*Ricci[a][c]
            R=summation 

    G=[[[] for i in range(d)] for j in range(d)]          

    pro=1
    for i in range(d):
        pro=-pro*g[i][i]
    sum=0
    for k in range(d):
        for i in range(d):
            sum=sum+(1/sqrt(pro))*(diff((sqrt(pro)*ginverse[k][i]*diff(phi,x[i])),x[k]))
    fin=sum

    summ=0.0
    for a in range(d):
        for b in range(d):
            summ=summ+diff(phi,x[a])*diff(phi,x[b])
    f=summ
    for a in range(d):
        for b in range(d):
            summ=Ricci[a][b]-(1/2)*R*g[a][b]-Lambda*g[a][b]+(8*pi/phi)*T[a][b]*g[a][b]+(omega/phi**2)*(diff(phi,x[a])*diff(phi,x[b])-(1/2)*g[a][b]*f)+\
                (1/phi)*(diff(phi,x[a],x[b])-g[a][b]*fin)  
            G[a][b]=summ       

    for a in range(d):
        for c in range(d):
            if G[a][c] !=0:        
                Bran=print("Brans_Dicke[",a,",",c,"]=", simplify(G[a][c]))
    return Bran
