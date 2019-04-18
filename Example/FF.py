# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 00:59:21 2018

@author: Windows 7
"""

from numpy import *
import numpy as np 
from pylab import *
import matplotlib.pyplot as plt
from math import *
from math import ceil
from cmath import *
x= arange(0.0 , 1.0, 0.1)
# define the function which need to inverse 
t=0.05
def Fs(s):
    return (1-(exp((x-1)*sqrt(s))+exp(-x*sqrt(s)))/(1+exp(-sqrt(s))))/s
segma=-0.005
T=15
finv=0.0
for k in range(0,100):
    a=real(Fs(segma+k*np.pi*1j/T))
    b=imag(Fs(segma+k*np.pi*1j/T))
    finv=finv+(a*np.cos(k*pi*t/T)-b*np.sin(k*pi*t/T))
    fin=(np.exp(segma*t)/T)*(Fs(segma)/2+finv)

print(fin)
plt.figure(1)
plt.plot(t, fin, 'r--')
plt.show()
show()
    
