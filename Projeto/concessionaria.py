from adt.veiculos import Veiculos
from funcoes.bib import *

class Concessionaria():
	"""docstring for Concessionaria"""
	def __init__(self):
		self.quantidade_veiculos = quantidade_veiculos
		self.veiculos = Veiculos()
		
	def busca_veiculo():
		print("---- BUSCAR VEÍCULO -------\n")
		chassi = input("- Nº do Chassi do Veículo -\n")
		veiculo = self.veiculos.buscar(chassi)
		print("Informações do Veículo:\n")
		print(veiculo)

	def adiciona_veiculo():
		print("---- ADICIONAR VEÍCULO ------------------------\n")
		print("-- Preencha abaixo as informações do Veículo --\n")
		chassi = input("- Nº do Chassi -\n")
		nome = input("- Nome -\n")
		ano = input("- Ano  -\n")
		marca = input("- Marca -\n")
		preco = input("- Preço -\n")
		self.veiculos.adicionar(chassi, nome, ano, marca, preco)

	def remove_veiculo():
		print("---- REMOVER VEÍCULO ------\n")
		chassi = input("- Nº do Chassi do Veículo -\n")
		self.veiculos.remover(chassi)

