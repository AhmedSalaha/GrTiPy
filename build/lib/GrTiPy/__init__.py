__version__ = "0.1.0"

import numpy as np
import sympy as sp
from sympy import *

from GrTiPy.inverse_metric import inverse_metric as inverse_metric
import GrTiPy.inverse_metric as inverse_metric
from GrTiPy.inverse_metric import inverse_metric

from GrTiPy.Det import Det as Det 
from GrTiPy.Det import Det
import GrTiPy.Det as Det

from GrTiPy.Tr import Tr as Tr
import GrTiPy.Tr as Tr
from GrTiPy.Tr import Tr

from GrTiPy.Christoffel_All import Christoffel_All as Christoffel_All
import GrTiPy.Christoffel_All as Christoffel_All
from GrTiPy.Christoffel_All import Christoffel_All

from GrTiPy.CovariantD import CovariantD as CovariantD
import GrTiPy.CovariantD as CovariantD
from GrTiPy.CovariantD import CovariantD

from GrTiPy.Christoffel_n_ab import Christoffel_n_ab as Christoffel_n_ab
import GrTiPy.Christoffel_n_ab as Christoffel_n_ab
from GrTiPy.Christoffel_n_ab import Christoffel_n_ab

from GrTiPy.Geodesics import Geodesics as Geodesics
import GrTiPy.Geodesics as Geodesics
from GrTiPy.Geodesics import Geodesics

from GrTiPy.Riemann_All import Riemann_All as Riemann_All
import GrTiPy.Riemann_All as Riemann_All
from GrTiPy.Riemann_All import Riemann_All

from GrTiPy.Riemann_nabc import Riemann_nabc as Riemann_nabc
import GrTiPy.Riemann_nabc as Riemann_nabc
from GrTiPy.Riemann_nabc import Riemann_nabc

from GrTiPy.Matric_coef import Matric_coef as Matric_coef
import GrTiPy.Matric_coef as Matric_coef
from GrTiPy.Matric_coef import Matric_coef

from GrTiPy.Ricci_scalar import Ricci_scalar as Ricci_scalar
import GrTiPy.Ricci_scalar as Ricci_scalar
from GrTiPy.Ricci_scalar import Ricci_scalar

from GrTiPy.Ricci_Tensor_All import Ricci_Tensor_All as Ricci_Tensor_All
import GrTiPy.Ricci_Tensor_All as Ricci_Tensor_All
from GrTiPy.Ricci_Tensor_All import Ricci_Tensor_All

from GrTiPy.Ricci_Tensor_ab import Ricci_Tensor_ab as Ricci_Tensor_ab
import GrTiPy.Ricci_Tensor_ab as Ricci_Tensor_ab
from GrTiPy.Ricci_Tensor_ab import Ricci_Tensor_ab

from GrTiPy.Einstein_Equation import Einstein_Equation as Einstein_Equation
import GrTiPy.Einstein_Equation as Einstein_Equation
from GrTiPy.Einstein_Equation import Einstein_Equation

from GrTiPy.Einstein_Equation_ab import Einstein_Equation_ab as Einstein_Equation_ab
import GrTiPy.Einstein_Equation_ab as Einstein_Equation_ab
from GrTiPy.Einstein_Equation_ab import Einstein_Equation_ab

from GrTiPy.Laplacian_operator import Laplacian_operator as Laplacian_operator
import GrTiPy.Laplacian_operator as Laplacian_operator
from GrTiPy.Laplacian_operator import Laplacian_operator

from GrTiPy.projection_tensor import projection_tensor as projection_tensor
import GrTiPy.projection_tensor as projection_tensor
from GrTiPy.projection_tensor import projection_tensor

from GrTiPy.Scalar_Brans_Dicke_field_Equation import Scalar_Brans_Dicke_field_Equation as Scalar_Brans_Dicke_field_Equation
import GrTiPy.Scalar_Brans_Dicke_field_Equation as Scalar_Brans_Dicke_field_Equation
from GrTiPy.Scalar_Brans_Dicke_field_Equation import Scalar_Brans_Dicke_field_Equation

from GrTiPy.Brans_Dicke_Equations import Brans_Dicke_Equations as Brans_Dicke_Equations
import GrTiPy.Brans_Dicke_Equations as Brans_Dicke_Equations
from GrTiPy.Brans_Dicke_Equations import Brans_Dicke_Equations

from GrTiPy.Brans_Dicke_Equations_ab import Brans_Dicke_Equations_ab as Brans_Dicke_Equations_ab
import GrTiPy.Brans_Dicke_Equations_ab as Brans_Dicke_Equations_ab
from GrTiPy.Brans_Dicke_Equations_ab import Brans_Dicke_Equations_ab

from GrTiPy.Spin_connection_first import Spin_connection_first as Spin_connection_first
import GrTiPy.Spin_connection_first as Spin_connection_first
from GrTiPy.Spin_connection_first import Spin_connection_first

from GrTiPy.Spin_connection import Spin_connection as Spin_connection
import GrTiPy.Spin_connection as Spin_connection
from GrTiPy.Spin_connection import Spin_connection

from GrTiPy.Wely_Tensor_abcd import Wely_Tensor_abcd as Wely_Tensor_abcd
import GrTiPy.Wely_Tensor_abcd as Wely_Tensor_abcd
from GrTiPy.Wely_Tensor_abcd import Wely_Tensor_abcd

from GrTiPy.Div import Div as Div
import GrTiPy.Div as Div
from GrTiPy.Div import Div

from GrTiPy.expansion_scalar import expansion_scalar as expansion_scalar
import GrTiPy.expansion_scalar as expansion_scalar
from GrTiPy.expansion_scalar import expansion_scalar

from GrTiPy.acceleration_vector import acceleration_vector as acceleration_vector
import GrTiPy.acceleration_vector as acceleration_vector
from GrTiPy.acceleration_vector import acceleration_vector

from GrTiPy.shear_tensor_ab import shear_tensor_ab as shear_tensor_ab
import GrTiPy.shear_tensor_ab as shear_tensor_ab
from GrTiPy.shear_tensor_ab import shear_tensor_ab

from GrTiPy.shear_tensor_ab import projection_tensor_ij as projection_tensor_ij
import GrTiPy.shear_tensor_ab as projection_tensor_ij
from GrTiPy.shear_tensor_ab import projection_tensor_ij

from GrTiPy.shear_tensor_ab import contrD as contrD
import GrTiPy.shear_tensor_ab as contrD
from GrTiPy.shear_tensor_ab import contrD

