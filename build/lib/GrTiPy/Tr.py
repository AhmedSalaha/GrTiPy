import numpy as np
import sympy as sp
from sympy import *

def Tr(metric):
    return np.array(sp.Matrix(metric).trace())
