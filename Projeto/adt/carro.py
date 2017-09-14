class Carro:
	"""docstring for Carro"""
	def __init__(self,chassi, nome, ano, marca, preco):
		self.chassi = chassi
		self.nome = nome
		self.ano = ano
		self.marca = marca
		self.preco = preco

	def __str__(self):
		result = ('Chassi do carro: {}\n' .format(self.chassi) +
				'Nome do carro: {}\n' .format(self.nome) +
				'Ano: {}\n' .format(str(self.ano)) +
				'Marca: {}\n' .format(str(self.marca)) +
				'Preço: {}\n' .format(str(self.preco)))
		return result