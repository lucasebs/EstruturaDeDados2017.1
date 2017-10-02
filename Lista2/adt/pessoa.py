from datetime import date

class Pessoa:
	"""docstring for Ponto"""
	def __init__(self):
		self.__nome = None
		self.__ano_nascimento = None
		self.__email = None

	def __str__(self):
		result = ("(" + str(self.__nome) +
					", " + str(self.__ano_nascimento) +
					", " + str(self.__email) + ") ")
		return result

	@property
	def nome(self):
		return self.__nome

	@nome.setter
	def nome(self, nome):
		self.__nome = nome

	@property
	def ano_nascimento(self):
		return self.__ano_nascimento

	@ano_nascimento.setter
	def ano_nascimento(self, ano_nascimento):
		self.__ano_nascimento = ano_nascimento		

	@property
	def email(self):
		return self.__email

	@email.setter
	def email(self, email):
		self.__email = email

	def obter_idade(self):
		return date.today().year - self.ano_nascimento


