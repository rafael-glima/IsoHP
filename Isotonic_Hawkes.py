
# By Rafael Goncalves de Lima

##############################################################

# This is a implementation of the Isotonic Hawkes Processes
# algorithm, described in the homonymous paper (Wang et al., 2016)

##############################################################

import numpy as np
from KernelFunc import KernelFunc
from Compute_Coefficient2 import CompCoeff
import numpy.random as rd

# Uploading sequence

t = np.array([1., 2., 3., 4., 5., 6.])

siz = len(t)

# Computing x_i

K_Param = {'K1_Type': 'EXP', 'EXP_coeffs': [1., 1.]}

x = np.zeros_like(t)

x[0] = 0.

for i in range(1,len(t)):

	tmp = KernelFunc(t[i]-t[:i], K_Param)

	tmp = np.sum(tmp)

	x[i] = tmp

print x

# Compute aij

# a = np.zeros((siz+1,siz))

# for i in range(siz):

# 	a_i = CompCoeff(t[i])
# 	a[i,:] = a_i

a = CompCoeff(t)

print('a: ' + repr(a))

# Compute N_i

N = range(1,siz+1)

N = np.array(N)

# Initialize w_0 and g_0 randomly

w = np.append(rd.random((1,)),rd.random((1,))*np.ones(siz,))

g = rd.random((siz,))

g = np.cumsum(g)

# Update w and g

g_k = g

diff2 = [(g_k[i] - g_opt[i])**2 for i in range(len(g_k))]

error = np.sum((diff2))/siz






