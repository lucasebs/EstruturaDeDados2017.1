from carro import Carro
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
			print(Veiculo.info_veiculo)
			temp = temp.proximo_veiculo

	def remover_especifico(self, chassi)
		if self.esta_vazia():
			return

		vclo_anterior = self.referencia
		vclo_corrente = vclo_anterior.proximo_veiculo

		while vclo_corrente is not None and vc:

			vclo_anterior = vclo_corrente
			vclo_corrente = vclo_corrente.proximo_veiculo

		if 
