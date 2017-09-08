class Carro:
	"""docstring for Carro"""
	def __init__(self):
		self.chassi = chassi
		self.nome = nome
		self.ano = ano
		self.marca = marca
		self.preco = preco

	def __str__(self):
		result = 'Chassi do carro: {}\n' .format(self.chassi)
		result += 'Nome do carro: {}\n' .format(self.nome)
		result += 'Ano: {}\n' .format(str(self.ano))
		result += 'Marca: {}\n' .format(str(self.marca))
		result += 'Preço: {}\n' .format(str(self.preco))
		return result 