from sys import platform
from .bib import *
import os

def captura_menu():
	'''
	Function: 
		captura_menu : Recebe da entrada padrao a opcao e retorna como
			operacao
	Summary: 
		op (int) : Recebe da entrada padrao opcao do menu
	Returns: 
		op (int) : Retorna inteiro reference a operacao da opcao lida da
			entrada principal, referente a opcao do menu
	'''
	# Recebe da entrada padrao opcao do menu
	# 1 - Buscar Veiculo
	# 2 - Adicinar Veiculo
	# 3 - Remover Veiculo 
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
	if iv != True: 
		c.veiculos.adicionar(int(iv[0]), iv[1], int(iv[2]), iv[3], float(iv[4]))
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

def carrega_lista(c):
	arq = open('arquivos/veiculos.txt', 'r')
	linhas = arq.readlines()
	result = ''
	
	for linha in linhas:
		if "Chassi do carro: " in linha:
			chassi = linha[17: -1]
		elif "Nome do carro: " in linha:
			nome = linha[15: -1]
		elif "Ano: " in linha:
			ano = linha[5: -1]	
		elif "Marca: " in linha:
			marca = linha[7: -1]
		elif "Preço: R$ " in linha:
			preco = linha[10: -1]
			print(chassi,nome, ano, marca, preco)
			c.veiculos.adicionar(int(chassi),nome, int(ano), marca, float(preco))
	
	arq.close()
