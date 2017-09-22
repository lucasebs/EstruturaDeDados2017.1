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
	'''
	Function: 
		seleciona_menu : Recebe como parametros a operacao do menu
			e seleciona funcao respectiva a operacao
	Attributes: 
		@param (op) (int) : Identificacao da operacao.
			1 -	Buscar Veiculo
			2 -	Adicionar Veiculo
			3 -	Remover Veiculo
		@param (c) (obj) : Objeto do tipo concessionaria
	Returns: 
		True (bool) : Retorna True em caso de opcao para sair do sistema
	'''
	# Verifica operacao recebida como parametro e executa a respectiva funcao
	# ou se usuário deseja sair do sistema
	# 1 - Buscar Veiculo
	if (op == '1'):
		# Executa funcao de busca passando a concessionaria c como parametro
		busca_veiculo(c)
	# 2 - Adicionar Veiculo
	elif (op == '2'):
		# Executa funcao de adicao passando a concessionaria c como parametro
		adiciona_veiculo(c)
	# 3 - Remover Veiculo
	elif (op == '3'):
		# Executa funcao de remocao passando a concessionaria c como parametro
		remove_veiculo(c)
	# Se receber da entrada padrao a str "sair", retorna True
	elif op.lower() == 'sair':
		return True
	# Se for recebida qualquer outra informacao na entrada padrao imprime erro da opcao
	else:
		print("Opção Inválida!")

def busca_veiculo(c):
	'''
	Function: 
		busca_veiculo : Recebe como parametro a concessionaria e executa
			na lista de veiculos desta a buscar do veiculo
	Summary: 
		chassi (int) : Recebe da funcao captura_entrada() um numero de chassi
		veiculo (obj) : Recebe um objeto do tipo Veiculo da funcao buscar()
	Attributes: 
		@param (c) (obj) : Objeto do tipo concessionaria
	'''
	# Exibe cabecalho da operacao de busca 'b'
	cabecalho('b')
	# Recebe numero de chassi do retorno da funcao captura_entrada()
	chassi = captura_entrada(c, 'b')
	# Recebe um objeto do tipo Veiculo da funcao buscar() da lista de veiculos
	# da concessionaria c
	veiculo = c.veiculos.buscar(chassi)
	# Imprime o veiculo
	imprime_veiculo(veiculo)

def adiciona_veiculo(c):
	'''
	Function: 
		adiciona_veiculo : Recebe como parametro a concessionaria e executa
			a adicao de um veiculo na lista de veiculos da concessionaria
	Summary: 
		iv (tupla) : Recebe da funcao captura_entrada() uma tupla	
	Attributes: 
		@param (c) (obj) : Objeto do tipo concessionaria
	'''
	# Exibe cabecalho da operacao de busca 'b'
	cabecalho('a')
	# iv = Informacoes do Veiculo. Recebe tupla da funcao captura_entrada() com 
	# as informacoes do veiculo para ser armazenado na lista de veiculos da 
	# concessionaria c
	iv = captura_entrada(c, 'a')
	# Verifica se iv nao e um valor booleano True, sendo assim uma tupla
	if iv != True: 
		# Adiciona o veiculo, com as informacoes do mesmo contidas em iv
		# na lista de veiculos da concessionaria
		c.veiculos.adicionar(int(iv[0]), iv[1], int(iv[2]), iv[3], float(iv[4]))
		# Incrementa 1 na quantidade de veiculos apos adicionar o veiculo na lista
		c.quantidade_veiculos += 1
		# Executa funcao atualiza_arquivo() passando como paramentro a 
		# concessionaria c
		atualiza_arquivo(c)
		# Executa funcao sucesso() para a operacao de adicao de veiculo
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
			c.veiculos.adicionar(int(chassi),nome, int(ano), marca, float(preco))
	
	arq.close()
