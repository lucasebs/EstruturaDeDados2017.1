from datetime import date

class Pessoa:

	def __init__(self):
		self.primeiroNome = ""
		self.sobrenome = ""
		self.cpf = ""
		self.anoNascimento = ""
		
	def __str__(self):
		result = "Nome completo: " + self.obter_nome() + '\n'
		result += "CPF: " + str(self.cpf) + '\n'
		result += "Ano nascimento: " + str(self.anoNascimento) + '\n'
		result += "Idade: " + str(self.obter_idade())

		return result

	def obter_nome(self):
		return str(self.primeiroNome) + ' ' + str(self.sobrenome)

	def obter_idade(self):
		data = date.today()
		return data.year - self.anoNascimento

