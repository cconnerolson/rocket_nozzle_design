import numpy as np
import pandas

data = pandas.read_csv('data/isentropic_flow_table.csv')  # , names=colnames)

M_data = data.Ma.tolist()
P_data = data.p.tolist()
T_data = data.t.tolist()
A_data = data.A.tolist()


# print(A_data)

def m2p(M):  # 1 output
	"""
	Returns pressure ratio corresponding to input Mach number using linear interpolation.
	:param M: Mach number
	"""
	if M < 0 or M >= 6:
		raise ValueError('Mach number outside valid input domain')
	return np.interp(M, M_data, P_data)


def m2t(M):  # 1 output
	"""
	Returns temperature ratio corresponding to input Mach number using linear interpolation.
	:param M: Mach number
	"""
	if M < 0 or M >= 6:
		raise ValueError('Mach number outside valid input domain')
	return np.interp(M, M_data, T_data)


def m2a(M):  # 1 output
	"""
	Returns area ratio corresponding to input Mach number using linear interpolation.
	:param M: Mach number
	"""
	if M < 0 or M >= 6:
		raise ValueError('Mach number outside valid input domain')
	return np.interp(M, M_data, A_data)


def p2m(P):  # 1 output todo verify output, verify error range
	"""
	Returns Mach number corresponding to input pressure ratio using linear interpolation.
	:param P: P/P_0 pressure ratio
	"""
	if P < 9.746e-4 or P > 1:  # todo change error range
		raise ValueError('Pressure ratio outside valid input domain')
	return np.interp(P, P_data, M_data)


def p2t(P):  # 1 output todo verify output, change error range
	"""
	Returns temperature ratio corresponding to input pressure ratio using linear interpolation.
	:param P: P/P_0 pressure ratio
	"""
	if P < 0 or P >= 6:
		raise ValueError('Pressure ratio outside valid input domain')
	return np.interp(P, P_data, T_data)


def p2a(P):  # 1 output todo verify output, change error range
	"""
	Returns area ratio corresponding to input pressure ratio using linear interpolation.
	:param P: P/P_0 pressure ratio
	"""
	pass
	if P < 0 or P >= 6:
		raise ValueError('Pressure ratio outside valid input domain')
	return np.interp(P, P_data, A_data)


def t2m(T):  # 1 output todo verify output, change error range
	"""
	Returns Mach number corresponding to input temperature ratio using linear interpolation.
	:param T: T/T_0 temperature ratio
	"""
	if T < 0 or T >= 6:
		raise ValueError('Temperature ratio outside valid input domain')
	return np.interp(T, T_data, M_data)


def t2p(T):  # 1 output todo verify output, change error range
	"""
	Returns pressure ratio corresponding to input temperature ratio using linear interpolation.
	:param T: T/T_0 temperature ratio
	"""
	if T < 0 or T >= 6:
		raise ValueError('Temperature ratio outside valid input domain')
	return np.interp(T, T_data, P_data)


def t2a(T):  # 1 output todo verify output, change error range
	"""
	Returns area ratio corresponding to input temperature ratio using linear interpolation.
	:param T: T/T_0 temperature ratio
	"""
	if T < 0 or T >= 6:
		raise ValueError('Temperature ratio outside valid input domain')
	return np.interp(T, T_data, A_data)


def a2m(A):  # 2 outputs todo define function, change error range
	"""
	Returns Mach number corresponding to input area ratio using linear interpolation.
	:param A: A/A* area ratio
	"""
	pass
	if A < 0 or A >= 6:
		raise ValueError('Area ratio outside valid input domain')


def a2p(A):  # 2 output todo define function, change error range
	"""
	Returns pressure ratio corresponding to input area ratio using linear interpolation.
	:param A: A/A* area ratio
	"""
	pass
	if A < 0 or A >= 6:
		raise ValueError('Area ratio outside valid input domain')


def a2t(A):  # 2 outputs todo define function, change error range
	"""
	Returns temperature ratio corresponding to input area ratio using linear interpolation.
	:param A: A/A* area ratio
	"""
	pass
	if A < 0 or A >= 6:
		raise ValueError('Area ratio outside valid input domain')
