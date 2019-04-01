def specific_heat(T):
	"""
	Shchomate equation to calculate specific heat of water vapor for a given temperature T.
	:param T: Temperature (K)
	"""
	t = T / 1000
	if 500 <= T < 1700:
		a, b, c, d, e = [30.092, 6.832514, 6.793425, -2.53448, 0.082139]
	elif T == 1700:
		print(48.915)
		return
		
	elif 1700 < T <= 6000:
		a, b, c, d, e = [41.96426, 8.622053, -1.49978, 0.098119, -11.1576]
	else:
		raise ValueError('Input temperature outside valid domain')
	c_p = a + (b * t) + (c * t**2) + (d * t**3) + (e / t**2)
	print(c_p)


temp = float(input("input temperature (K)... "))
specific_heat(temp)
