from .no_vclo import No_vclo
from .veiculo import Veiculo


class Veiculos(object):
	"""
	Class:
		Veiculos : Lista de veiculos registrados na concessionaria
	Summary:
		referencia (Obj) : Objeto do tipo No_vclo definindo inicio da lista
	"""
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
			result += str(temp.info_veiculo)
			temp = temp.proximo_veiculo
			if temp is not None:
				result +="-------------------------------\n"
		return result

	def remover(self, chassi):
		if self.esta_vazia():
			return "Sem veículos na concessionária!"

		vclo_anterior = self.referencia

		if vclo_anterior.info_veiculo.chassi == chassi and vclo_anterior.proximo_veiculo is not None:
			self.referencia = vclo_anterior.proximo_veiculo
			return True
		elif vclo_anterior.info_veiculo.chassi == chassi:  
			self.referencia = None 
			return True

		vclo_corrente = vclo_anterior.proximo_veiculo


		while vclo_corrente.proximo_veiculo is not None and vclo_corrente.info_veiculo.chassi != chassi:
			vclo_anterior = vclo_corrente
			vclo_corrente = vclo_corrente.proximo_veiculo

		if(vclo_corrente.proximo_veiculo is not None):
			vclo_anterior.proximo_veiculo = vclo_corrente.proximo_veiculo
			vclo_corrente.proximo_veiculo = None
			return True

		if vclo_corrente is None:
			return "Veículo não registrado na concessionária!"

		if vclo_corrente.info_veiculo.chassi == chassi:
			vclo_corrente = None
			vclo_anterior.proximo_veiculo = None
			return True

	def adicionar(self, chassi, nome, ano, marca, preco):
		novo_vclo = No_vclo()
		novo_vclo.info_veiculo = Veiculo(chassi, nome, ano, marca, preco)

		if self.esta_vazia():
			self.referencia = novo_vclo
			return

		temp = self.referencia

		if temp.proximo_veiculo is None:
			temp.proximo_veiculo = novo_vclo
			return

		while temp.proximo_veiculo is not None:
			temp = temp.proximo_veiculo

		temp.proximo_veiculo = novo_vclo

	def buscar(self, chassi):
		if self.esta_vazia():
			return "Sem veículos na concessionária!"

		temp = self.referencia
		if temp.proximo_veiculo is None and temp.info_veiculo.chassi == chassi:
			return temp.info_veiculo
		elif temp.proximo_veiculo is None and temp.info_veiculo.chassi != chassi:
			return "Veículo não registrado na concessionária!"

		while (temp is not None and temp.info_veiculo.chassi != chassi):
			temp = temp.proximo_veiculo

		if temp is None:
			return "Veículo não registrado na concessionária!"

		return temp.info_veiculo
			
