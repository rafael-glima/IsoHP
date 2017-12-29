
import numpy as np
from KernelFunc import KernelFunc
from scipy.optimize import fsolve

def CompCoeff(ts,i):

	t = ts

	global siz

	siz = len(t)

	t_i = t[i]

	a_i = np.zeros((siz+1,))

	tp = np.array((siz,))

	K_Param = {'K1_Type': 'EXP', 'EXP_coeffs': [1., 1.]}

	for j in range(siz):

		# Compute tpj that satisfies xptj = xtj

		xtj = KernelFunc(t_i - t[:i],K_Param)

		xtj = np.sum(xtj)

		def find_t_root(x,args=(t[:j],xtj)):

			xtj = xtj

			xpt = KernelFunc(x-t[:j+1])

			xpt = np.sum(xpt)

			return xpt - xtj

		x0 = t[j]
		
		tpj = fsolve(find_t_root,x0,args=(t[:j],xtj))

		tp[j] = tpj

	for j in range(1,siz):

		a_i[0] = 0

		 for i in range(1,siz):

			# Compute bij

			b_i[j] = min(tp[j-1],t[i]) - max(tp[j],t[i-1])

			# Compute aij

			a_i[j] = a

	return a_i[1:,:]