import numpy as np
import pandas

data = pandas.read_csv('data/isentropic_flow_table.csv')  # , names=colnames)

M_data = data.Ma.tolist()
P_data = data.p.tolist()
T_data = data.t.tolist()
A_data = data.A.tolist()


# print(A_data)

def m2p(M):  # 1 output todo description
	"""
	*** description ***
	:param Ma: Mach number
	"""
	if M < 0 or M >= 6:
		raise ValueError('Mach number input outside valid domain')
	return np.interp(M, M_data, P_data)


def m2t(M):  # 1 output todo description
	"""
	*** description ***
	:param Ma: Mach number
	"""
	if M < 0 or M >= 6:
		raise ValueError('Mach number input outside valid domain')
	return np.interp(M, M_data, T_data)


def m2a(M):  # 1 output todo description
	"""
	*** description ***
	:param Ma: Mach number
	"""
	if M < 0 or M >= 6:
		raise ValueError('Mach number input outside valid domain')
	return np.interp(M, M_data, A_data)


print(m2a(0.05))


def p2m(P):  # 1 output # todo fix P2M, description
	"""
	*** description ***
	:param P: P/P_0 pressure ratio
	"""
	if P < 9.746e-4 or P > 1:
		raise ValueError('Pressure ratio input outside valid domain')
	return np.interp(P, P_data, M_data)


def p2t(P):  # 1 output todo P2T, description
	"""
	*** description ***
	:param P: P/P_0 pressure ratio
	"""
	if P < 0 or P >= 6:
		raise ValueError('Pressure ratio input outside valid domain')
	pass


def p2a(P):  # 1 output todo P2A, description
	"""
	*** description ***
	:param P: P/P_0 pressure ratio
	"""
	pass


def t2m(T):  # 1 output todo T2M, description
	"""
	*** description ***
	:param T: T/T_0 temperature ratio
	"""
	pass


def t2p(T):  # 1 output todo T2P, description
	"""
	*** description ***
	:param T: T/T_0 temperature ratio
	"""
	pass


def t2t(T):  # 1 output todo T2A, description
	"""
	*** description ***
	:param T: T/T_0 temperature ratio
	"""
	pass


def a2m(A):  # 2 outputs todo A2M, description
	"""
	*** description ***
	:param A: A/A* area ratio
	"""
	pass


def a2p(A):  # 2 output todo A2P, description
	"""
	*** description ***
	:param A: A/A* area ratio
	"""
	pass


def a2t(A):  # 2 outputs todo A2T, description
	"""
	*** description ***
	:param A: A/A* area ratio
	"""
	pass

