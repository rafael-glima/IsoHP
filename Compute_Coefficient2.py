import numpy as np
from KernelFunc import KernelFunc
from scipy.optimize import fsolve

def CompCoeff(ts):

	#t = np.append(0,ts)

	t = ts

	#print('t:'+repr(t))

	#global siz

	siz = len(t)

	a = np.zeros((siz,siz))

	#print('a.shape: ' + repr(a.shape))

	tp = np.zeros((siz,siz))

	#print('tp.shape: ' + repr(tp.shape))

	xti = np.zeros((siz,))

	# xti[0] = 0.

	# xti[1] = 0

	#xti = xti[1:]

	K_Param = {'K1_Type': 'EXP', 'EXP_coeffs': [1., 1.]}

	for i in range(1,siz):

		# Compute tpj that satisfies xptj = xti

		x_ti = KernelFunc(t[i] - t[1:i],K_Param)

		x_ti = np.sum(x_ti)

		xti[i] = x_ti

	print('xti :'+repr(xti))

	for i in range(1,siz):

		xt_i = xti[i]

		#def find_t_root(x,args=(t[:i],xti,K_Param)):
		def find_t_root(x,ti,xt_i,K_Param):

			#xti = xti

			ti = ti

			#print('ti[1:i] :' + repr(ti[1:i]))

			xpt = KernelFunc(x-ti[:i], K_Param)

			xpt = np.sum(xpt)

			#print('xpt - xt_i :' + repr(xpt - xt_i))

			return xpt - xt_i

		for j in range(1,siz):

			x0 = t[j-1]

			#print('x0: '+repr(x0))
			
			#tpj = fsolve(find_t_root,x0,args=(t[1:j],xti,K_Param))

			#tpj = fsolve(find_t_root,x0,t[1:j],xti,K_Param)

			tpj = fsolve(lambda x: find_t_root(x,t[:j],xt_i,K_Param),x0)

			# print('t: '+repr(x0))

			# print('tpj: ' + repr(tpj[0]))

			tp[i,j] = tpj[0]

			#print('tpj.shape: ' + repr(tpj.shape))

	tp[:,0] = 0.

	tp[0,0] = t[1]

	tp[0,1:] = np.inf #t[1]

	#tp[1,1:] = np.inf

	print('tp: ' + repr(tp))

	#tp = np.transpose(tp)

	# print('t: ' + repr(t))

	for j in range(1,siz): #range(1,siz-1):

		a[0,j] = 0.

		for i in range(1,siz):			

			# print('min(tp[i,j-1], t[i]) :' + repr(min(tp[i,j-1], t[i])))

			# print('max(tp[i,j],t[i-1]) :' + repr(max(tp[i,j],t[i-1])))

			bij = min(tp[i+1,j], t[i]) - max(tp[i,j],t[i])

			# bij = min(tp[j,i-1], t[i]) - max(tp[j,i],t[i-1])

			a[i,j] = a[i-1,j] + bij

			#a[j,i] = a[j-1,i] + bij

	return a[1:,:]
