import numpy as np
import csv


with open('data/isentropic_flow_table.csv', 'r') as f:
	reader = csv.reader(f)
	next(reader)  # skip header
	i_f_data = [r for r in reader]


def M2P(Ma):  # 1 output todo description
	"""
	*** description ***
	:param Ma: Mach number
	"""
	if Ma < 0 or Ma >= 6:
		raise ValueError('Mach number input outside valid domain')
	return np.interp(Ma, i_f_data[:, 0], i_f_data[:, 1])


def M2T(Ma):  # 1 output todo description
	"""
	*** description ***
	:param Ma: Mach number
	"""
	if Ma < 0 or Ma >= 6:
		raise ValueError('Mach number input outside valid domain')
	return np.interp(Ma, i_f_data[:, 0], i_f_data[:, 2])


def M2A(Ma):  # 1 output todo description
	"""
	*** description ***
	:param Ma: Mach number
	"""
	if Ma < 0 or Ma >= 6:
		raise ValueError('Mach number input outside valid domain')
	return np.interp(Ma, i_f_data[:, 0], i_f_data[:, 5])


def P2M(P):  # 1 output # todo P2M, description
	pass
	"""
	*** description ***
	:param P: P/P_0 pressure ratio
	"""
	if P < 0 or P >= 6:
		raise ValueError('*** input outside valid domain')
	return np.interp(P, i_f_data[:, 1], i_f_data[:, 0])


def P2T(P):  # 1 output todo P2T, description
	pass


def P2A(P):  # 1 output todo P2A, description
	pass


def T2M(P):  # 1 output todo T2M, description
	pass


def T2P(P):  # 1 output todo T2P, description
	pass


def T2A():  # 1 output todo T2A, description
	pass


def A2M():  # 2 outputs todo A2M, description
	pass


def A2P():  # 2 output todo A2P, description
	pass


def A2T():  # 2 outputs todo A2T, description
	pass
