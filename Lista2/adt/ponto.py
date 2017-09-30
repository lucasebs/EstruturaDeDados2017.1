class Ponto:
	"""docstring for Ponto"""
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		result = ("(" + str(self.x) +
					"," + str(self.y) + ")")
		return result

