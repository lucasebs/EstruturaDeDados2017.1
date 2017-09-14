from no_vclo import No_vclo
from veiculo import Veiculo


class Veiculos(object):
	"""docstring for Veiculos"""
	def __init__(self):
        self.referencia = None

    def esta_vazia():
    	return self.referencia is None:


	def listar(self):
		if self.esta_vazia():
			return

		temp = self.referencia

		while temp is not None:
			print(temp.info_veiculo)
			temp = temp.proximo_veiculo

	def remover(self, chassi)
		if self.esta_vazia():
			return "Sem veículos na concessionária!"

		vclo_anterior = self.referencia
		vclo_corrente = vclo_anterior.proximo_veiculo

		while vclo_corrente is not None and vc:
			vclo_anterior = vclo_corrente
			vclo_corrente = vclo_corrente.proximo_veiculo

		if(vclo_corrente is not None):
			vclo_anterior.proximo_veiculo = vclo_corrente.proximo_veiculo
			vclo_corrente.proximo_veiculo = None

	def adicionar(self, chassi, nome, ano, marca, preco):
		novo_vclo = No_vclo()
		novo_vclo.info_veiculo = Veiculo(chassi, nome, ano, marca, preco)

		if self.esta_vazia():
			self.referencia = novo_vclo
			return

		temp = self.referencia

		while temp.proximo_veiculo is not None:
			temp = temp.proximo_veiculo

		temp.proximo_veiculo = novo_vclo

	def buscar(self, chassi):
		if self.esta_vazia()
			return "Sem veículos na concessionária!"

		temp = self.referencia

		while (temp is not None and temp.info_veiculo.chassi != chassi):
			temp = temp.proximo_veiculo

		return temp.info_veiculo	
			