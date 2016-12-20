''' Module for exceptions lesson'''

def convert(s):
	'''Convert to an integer'''
	x = -1
	try:
		x = int(s)
		print("Conversion successful! x =", x)
	except (ValueError, TypeError):
		print("Conversion failed!")
	return x