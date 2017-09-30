import math

class Retangulo:
	"""docstring for Retangulo"""
	def __init__(self, p1, p2, p3, p4):
		self.p1 = p1
		self.p2 = p2
		self.p3 = p3
		self.p4 = p4				
		self.lados = None

	def __str__(self):
		result = ("[" + str(self.p1) +
					"," + str(self.p2) +
					"," + str(self.p3) +
					"," + str(self.p4) + "]")
		return result

	def area(self):
		if self.lados is None:
			self.calcula_lados()
		
		return self.lados[0] * self.lados[1]

	def quadrado(self):
		self.calcula_lados()
		if (self.lados[0] == self.lados[1]):
			print("É um quadrado")
		else:
			print("Não é um quadrado")

	def calcula_lados(self):
		lado_a = math.sqrt((self.p2.x - self.p1.x)**2 + (self.p2.y - self.p1.y)**2)
		lado_b = math.sqrt((self.p1.x - self.p3.x)**2 + (self.p1.y - self.p3.y)**2)

		print(lado_a)
		print(lado_b)
				
		self.lados = (lado_a, lado_b)		


		


