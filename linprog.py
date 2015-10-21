import numpy as np
import scipy as sp
from scipy import optimize

print(np.__version__)
print(sp.__version__)

A_ub = np.loadtxt("A_ub.txt")
b_ub = np.loadtxt("b_ub.txt")
c = np.loadtxt("c.txt")

res = optimize.linprog(c, A_ub, b_ub)
print(res)

print(np.dot(A_ub, res["x"]) <= b_ub)

# $ ipython3 linprog.py
# 1.9.2
# 0.16.0
#      fun: -190.60270595672296
#  message: 'Optimization terminated successfully.'
#   status: 0
#        x: array([  2.97493693e+02,   1.00000000e+02,   1.46656947e+01,
#          1.00000000e+02,   1.00000000e+02,   0.00000000e+00,
#          1.00000000e+02,   0.00000000e+00,   0.00000000e+00,
#          0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
#          0.00000000e+00,   8.43343053e-03,   1.35133800e-03,
#          2.75978408e-02,   0.00000000e+00,   2.46647019e-02,
#          2.57472418e+02])
#      nit: 13
#    slack: array([  0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
#          0.00000000e+00,   8.53343053e+01,   0.00000000e+00,
#          0.00000000e+00,   1.00000000e+02,   0.00000000e+00,
#          9.00000000e+02,   9.00000000e+02,   9.00000000e+02,
#          9.00000000e+02,   9.00000000e+02,   9.00000000e+02,
#          8.43343053e-03,   1.35133800e-03,   2.75978408e-02,
#          0.00000000e+00,   2.46647019e-02,   2.57472418e+02,
#          0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
#          1.00000000e+02,   0.00000000e+00,   2.57468078e+06])
#  success: True
# [ True  True  True  True  True  True  True  True  True  True  True  True
#   True  True  True  True  True  True  True  True  True  True False  True
#   True  True  True]
