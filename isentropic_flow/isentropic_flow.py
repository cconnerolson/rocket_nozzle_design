import numpy as np
from isentropic_flow.import_data import i_f_data


def M2P(Ma):  # 1 output
	"""
	*** description ***
	:param Ma: Mach number
	"""
	if Ma < 0 or Ma >= 6:
		raise ValueError('Mach number input outside valid domain')
	return np.interp(Ma, i_f_data[:, 0], i_f_data[:, 1])


def M2T(Ma):  # 1 output
	"""
	*** description ***
	:param Ma: Mach number
	"""
	if Ma < 0 or Ma >= 6:
		raise ValueError('Mach number input outside valid domain')
	return np.interp(Ma, i_f_data[:, 0], i_f_data[:, 2])


def M2A(Ma):  # 1 outputs
	"""
	*** description ***
	:param Ma: Mach number
	"""
	if Ma < 0 or Ma >= 6:
		raise ValueError('Mach number input outside valid domain')
	return np.interp(Ma, i_f_data[:, 0], i_f_data[:, 5])


def P2M(P):  # 1 output
	pass


def P2T(P):  # 1 output
	pass


def P2A(P):  # 1 output
	pass


def T2M(P):  # 1 output
	pass


def T2P(P):  # 1 output
	pass


def T2A():  # 1 output
	pass


def A2M():  # 2 outputs
	pass


def A2P():  # 2 output
	pass


def A2T():  # 2 outputs
	pass
