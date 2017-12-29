
import numpy as np

def KernelFunc(vector, para):

	K1_Param = para

	if K1_Param['K1_Type'] == 'EXP':

		coeffs = K1_Param['EXP_coeffs']

		alpha = coeffs[0]

		beta = coeffs[1]

		vector[vector < 0.] = -np.inf

		#print('vector: '+repr(vector))

		return alpha*np.exp(-beta*vector)

	if K1_Param['K1_Type'] == 'PWL':

		coeffs = K1_Param['PWL_coeffs']

		K = coeffs[0]

		c = coeffs[1]

		p = coeffs[2]

		return K*np.power(vector+c,-p)

	if K1_Param['K1_Type'] == 'SQR':

		coeffs = K1_Param['SQR_coeffs']

		B = coeffs[0]

		L = coeffs[1]

		# def SQR(vector, B, L):

		vector[vector > L] == 0

		vector[vector <= L] == B

		return vector

	if K1_Param['K1_Type'] == 'SNS':

		coeffs = K1_Param['SNS_coeffs']

		A = coeffs[0]

		omega = coeffs[1]

		# def SNS(vector, A, omega):

		vector[vector < np.pi/omega] = A*np.sin(omega*vector[vector < np.pi/omega])

		vector[vector >= np.pi/omega] = 0

		return vector