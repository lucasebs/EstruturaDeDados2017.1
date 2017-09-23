from .veiculos import Veiculos
from funcoes.bib import *

class Concessionaria():
	"""
	Class: 
		Concessionaria 
	Summary:
		quantidade_veiculos (int) : Quantidade de veiculos registrados
			na concessionaria
		veiculos (list) : Lista do tipo Veiculos contendo veiculos
			registrados na concessionaria
	"""
	def __init__(self):
		self.quantidade_veiculos = 0
		self.veiculos = Veiculos()
