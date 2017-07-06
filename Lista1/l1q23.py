from datetime import date

class Carro:
	def __init__(self, nome, fab, rev, km):
		self.nomeCarro = nome
		self.anoFab = fab
		self.anoRev = rev
		self.km = km


	def __str__(self):
		result = 'Nome carro: ' + str(self.nomeCarro) + '\n'
		result += 'Ano Fabricacao: ' + str(self.anoFab) + '\n'
		result += 'Ano Ultima Revisao: ' + str(self.anoRev) + '\n'
		result += 'quilometragem: ' + str(self.km)
		return result

	def validar_revisao(self, anoRef = None):
		if(anoRef == None):
			data = date.today()
			anoRef = data.year

		resultado = anoRef - self.anoRev

		if(resultado < 2):
			return "Revisao dentro do prazo!"
		elif(resultado < 5):
			return "Proximo da expiracao da garantia!"
		else:
			return "Revisao fora do prazo"

