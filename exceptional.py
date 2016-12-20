''' Module for exceptions lesson'''

def convert(s):
	'''Convert to an integer'''
	try:
		x = int(s)
		print("Conversion successful! x =", x)
	except ValueError:
		x = -1
		print("Conversion failed!")
	except TypeError:
		print("Conversion failed!")
		x = -1
	return x