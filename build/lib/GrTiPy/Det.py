
import numpy as np
import sympy as sp
from sympy import *

def Det(metric):
    return np.array(sp.Matrix(metric).det())
