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
