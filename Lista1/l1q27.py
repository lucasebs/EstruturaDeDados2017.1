from datetime import date

class Computador:

	def __init__(self, pmRef, pmNome, anoCompra, sO):
		self.placaMaeRef = pmRef
		self.placaMaeNome = pmNome
		self.anoCompra = anoCompra
		self.sistemaOperacional = sO

	def __str__(self):
		result = 'Placa Mae Referencia: ' + str(self.placaMaeRef) + '\n'
		result += 'Placa Mae Nome: ' + str(self.placaMaeNome) + '\n'
		result += 'Ano Compra: ' + str(self.anoCompra) + '\n'
		result += 'Sistema Operacional: ' + str(self.sistemaOperacional) 
		return result


	def obter_configuracao(self):
		return str(self.placaMaeRef) + ' - ' + str(self.placaMaeNome)

	def obter_tempo_de_uso(self):
		return date.year - self.anoCompra
