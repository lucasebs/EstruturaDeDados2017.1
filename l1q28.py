class Imovel:

	def __init__(self, numero, bairro, areaImovel, preco):
		self.numero = numero 
		self.bairro = bairro
		self.areaImovel = areaImovel
		self.preco = preco
		
	def  __str__(self):
		result = 'Numero de Inscricao do Imovel: ' + str(self.numero) + '\n'
		result += 'Bairro: ' + str(self.bairro) + '\n'
		result += 'Area do Imovel: ' + str(self.areaImovel) + '\n'
		result += 'Preco: ' + str(self.preco)
		return 

	def vender_imovel(self):
		return self.preco + (self.preco * 0.1)