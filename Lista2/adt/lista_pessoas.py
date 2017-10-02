from .no_pessoa import No_pessoa
from .pessoa import Pessoa


class Lista_pessoas(object):
	def __init__(self):
		self.referencia = None

	def esta_vazia(self):
		return self.referencia is None

	def listar(self):
		if self.esta_vazia():
			return

		temp = self.referencia
		result = ''

		while temp is not None:
			result += str(temp.info_pessoa)
			temp = temp.proxima
			if temp is not None:
				result +="\n"
		return result

	def adicionar(self, nome, ano_nascimento, email):
		no_pessoa = No_pessoa()
		pessoa = Pessoa()
		pessoa.nome = nome 
		pessoa.ano_nascimento = ano_nascimento
		pessoa.email = email
		no_pessoa.info_pessoa = pessoa

		if self.esta_vazia():
			self.referencia = no_pessoa
			return

		temp = self.referencia

		if temp.proxima is None:
			temp.proxima = no_pessoa
			return

		while temp.proxima is not None:
			temp = temp.proxima

		temp.proxima = no_pessoa
			
