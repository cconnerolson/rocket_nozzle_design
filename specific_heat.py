# Schomate Equation to calculate the specific heat of water vapor as a function of temperature


def specific_heat(T):
	t = T #/ 1000
	if 500 <= T <= 1700:
		a, b, c, d, e = 30.092, 6.832514, 6.793425, -2.53448, 0.082139
	elif 1700 < T <= 6000:
		a, b, c, d, e = 41.96426, 8.622053, -1.49978, 0.098119, -11.1576
	else:
		raise ValueError('Input temperature outside of valid domain')
	return a + b * T + c * T**2 + d * T**3 + e / T**2

