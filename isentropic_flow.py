import numpy as np
import pandas

data = pandas.read_csv('data/isentropic_flow_table.csv')

M_data = data.Ma.tolist()
P_data = data.p.tolist()
T_data = data.t.tolist()
A_data = data.A.tolist()


class IsentropicFlow(object):
	"""Isentropic Flow Table Lookup Toolkit"""
	version = '1.0'
	
	def __init__(self, M=0, P=0, T=0, A=0, verbose=False):
		self.M = M
		self.P = P
		self.T = T
		self.A = A
		self.verbose = verbose
	
	def __repr__(self):
		return "IsentropicFlow({}, {}, {}, {})".format(self.M, self.P, self.T, self.A)
	
	def __str__(self):
		return 'M = {}\nP = {}\nT = {}\nA = {}'.format(self.M, self.P, self.T, self.A)
	
	@classmethod
	def mach_lookup(cls, M, verbose=False):
		"""
		Returns pressure ratio, temperature ratio, and area ratio
		corresponding to input Mach number using linear interpolation.
		:param M: Mach number
		:return P: Pressure ratio
		:return T: Temperature ratio
		:return A: Area ratio
		"""
		if M < 0 or M >= 6:
			raise ValueError('Mach number outside valid input domain')
		cls.M = M
		cls.P = np.interp(M, M_data, P_data)
		cls.T = np.interp(M, M_data, T_data)
		cls.A = np.interp(M, M_data, A_data)
		cls.verbose = verbose
		if cls.verbose:
			print(cls.__str__(cls))
	
	@classmethod
	def pressure_lookup(cls, P, verbose=False):
		"""
		Returns pressure ratio, temperature ratio, and area ratio
		corresponding to input Mach number using linear interpolation.
		:param M: Mach number
		:return P: Pressure ratio
		:return T: Temperature ratio
		:return A: Area ratio
		"""
		if P < 9.746e-4 or P > 1:
			raise ValueError('Mach number outside valid input domain')
		cls.P = P
		cls.M = np.interp(P, M_data, M_data)
		cls.T = np.interp(P, M_data, T_data)
		cls.A = np.interp(P, M_data, A_data)
		cls.verbose = verbose
		if cls.verbose:
			print(cls.__str__(cls))
	
	@classmethod
	def temperature_lookup(cls, T, verbose=False):
		"""
		Returns pressure ratio, temperature ratio, and area ratio
		corresponding to input Mach number using linear interpolation.
		:param M: Mach number
		:return P: Pressure ratio
		:return T: Temperature ratio
		:return A: Area ratio
		"""
		if T < 0.1379 or T > 1:
			raise ValueError('Mach number outside valid input domain')
		cls.T = T
		cls.M = np.interp(T, T_data, M_data)
		cls.P = np.interp(T, T_data, P_data)
		cls.A = np.interp(T, T_data, A_data)
		cls.verbose = verbose
		if cls.verbose:
			print(cls.__str__(cls))
	
	def a2m(self, A):  # 2 outputs todo define function, change error range
		"""
		Returns Mach number corresponding to input area ratio using linear interpolation.
		:param A: A/A* area ratio
		"""
		pass
		if A < 0 or A >= 6:
			raise ValueError('Area ratio outside valid input domain')
	
	def a2p(self, A):  # 2 output todo define function, change error range
		"""
		Returns pressure ratio corresponding to input area ratio using linear interpolation.
		:param A: A/A* area ratio
		"""
		pass
		if A < 0 or A >= 6:
			raise ValueError('Area ratio outside valid input domain')
	
	def a2t(self, A):  # 2 outputs todo define function, change error range
		"""
		Returns temperature ratio corresponding to input area ratio using linear interpolation.
		:param A: A/A* area ratio
		"""
		pass
		if A < 0 or A >= 6:
			raise ValueError('Area ratio outside valid input domain')
