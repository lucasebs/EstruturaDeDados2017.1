class Veiculo():
	"""
	Class:
		Veiculo : Objeto veiculo
	Summary:
		chassi 	(int) 	: Numero de chassi do veiculo.
		nome 	(str)	: Nome do veiculo correspondente ao chassi 
			informado
		ano 	(int)	: Ano de fabricacao do veiculo
		marca 	(str)	: Marca do veiculo 
		preco 	(float)	: Preco em Real do veiculo
	"""
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
				'Preço: R$ {}\n' .format(str(self.preco)))
		return result
