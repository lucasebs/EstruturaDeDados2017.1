from sys import platform
from .bib import *
import json
import os

def captura_menu():
	op = input(" - Informe a operação desejada: ")
	return op

def seleciona_menu(op, c):
	if (op == '1'):
		busca_veiculo(c)
	elif (op == '2'):
		adiciona_veiculo(c)
	elif (op == '3'):
		remove_veiculo(c)
	elif op.lower() == 'sair':
		return True
	else:
		print("Opção Inválida!")

def busca_veiculo(c):
	cabecalho('b')
	chassi = captura_entrada(c, 'b')
	veiculo = c.veiculos.buscar(chassi)
	imprime_veiculo(veiculo)

def adiciona_veiculo(c):
	cabecalho('a')
	iv = captura_entrada(c, 'a')
	c.veiculos.adicionar(iv[0], iv[1], iv[2], iv[3], iv[4])
	c.quantidade_veiculos += 1
	atualiza_arquivo(c)
	sucesso('a')

def remove_veiculo(c):
	cabecalho('r')
	chassi = captura_entrada(c, 'r')
	removido = c.veiculos.remover(chassi)
	if removido == True:
		c.quantidade_veiculos -= 1
		atualiza_arquivo(c)
		sucesso('r')
	else:
		print(removido)

def atualiza_arquivo(c):

	arq = open('arquivos/veiculos.txt', 'w')	
	if c.veiculos.listar() is not None:
		arq.write(c.veiculos.listar())
	else:
		arq.write('')
	arq.close()

def limpar_tela():
	if platform == "linux" or platform == "linux2":
		os.system('clear')
	elif platform == "win32":
		os.system('cls')

def verifica_fim():
	parada = input()	
	if (parada.lower() == 'sair'):
		return True
