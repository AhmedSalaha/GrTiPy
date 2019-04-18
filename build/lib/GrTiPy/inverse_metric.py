import numpy as np
import sympy as sp
from sympy import *
def inverse_metric(metric):
    return np.array(sp.Matrix(metric).inv())
    
