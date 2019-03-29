import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("isentropic_flow_table.csv")

# print(df)

# df.plot(kind='scatter', x='A/A*', y='P/P_0')
# plt.show()


def M2P(Ma_in):  # 1 output
	for ii in df:
		if df.Ma[ii] > Ma_in:
			Ma1, Ma2 = df.Ma[(ii - 1)], df.Ma[(ii)]
			d_Ma = Ma2 - Ma1
			P = df.Ma[(ii - 1)]
			# raise ValueError('invalid input')
		

def M2T(Ma):  # 1 output
	pass


def M2A(Ma):  # 1 outputs
	pass


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
