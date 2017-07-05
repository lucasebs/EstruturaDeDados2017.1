class Computador:

	def __init__(self, pmRef, pmNome, anoCompra, sO):
		self.placaMaeRef = pmRef
		self.placaMaeNome = pmNome
		self.anoCompra = anoCompra
		self.sistemaOperacional = sO

	def __str__(self):
		result = 'Placa Mae: ' + str()