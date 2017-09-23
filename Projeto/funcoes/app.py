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
			a adicao de um veiculo na lista de veiculos da concessionaria c
	Summary: 
		iv (tupla) : Recebe da funcao captura_entrada() uma tupla	
	Attributes: 
		@param (c) (obj) : Objeto do tipo concessionaria
	'''
	# Exibe cabecalho da operacao de busca 'a'
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
	'''
	Function: 
		remove_veiculo : Recebe como parametro a concessionaria e executa
			a remocao de um veiculo na lista de veiculos da concessionaria c
	Summary: 
		chassi (int) : Recebe da funcao captura_entrada() um numero de chassi
		removido (str/bool) : Receve da funcao remover() da lista de veiculos da 
		concessionaria um valor booleano ou str com motivo da nao remocao
	Attributes: 
		@param (c) (obj) : Objeto do tipo concessionaria
	'''
	# Exibe cabecalho da operacao de busca 'b'
	cabecalho('r')
	# Recebe numero de chassi do retorno da funcao captura_entrada()
	chassi = captura_entrada(c, 'r')
	# Recebe valor booleano ou str da funcao remover() da lista de veiculos da concessionaria
	removido = c.veiculos.remover(chassi)
	# Verifica se removido tem valor True, significando que o veiculo foi removido da lista
	# de veiculos da concessionaria. 
	if removido == True:
		# Decrementa 1 na quantidade de veiculos apos adicionar o veiculo na lista
		c.quantidade_veiculos -= 1
		# Executa funcao atualiza_arquivo() passando como paramentro a 
		# concessionaria c
		atualiza_arquivo(c)
		# Executa funcao sucesso() para a operacao de remocao de veiculo
		sucesso('r')
	# Se veiculo nao tiver sido removido exibe o motivo na tela
	else:
		print(removido)

def atualiza_arquivo(c):	
	'''
	Function: 
		atualiza_arquivo : Recebe como parametro a concessionaria e executa
			a atualizacao do arquivo de registro(veiculos.txt)
	Summary: 
		arq (file) : Recebe arquivo aberto habilitado para escrita
	Attributes: 
		@param (c) (obj) : Objeto do tipo concessionaria
	'''
	# Abre arquivo veiculos.txt no modo de escrita e define nome como arq
	arq = open('arquivos/veiculos.txt', 'w')	
	# Verifica se a lista de veiculos esta vazia
	# Se tiver valor diferente de None escreve lista de veiculos no arquivo
	if c.veiculos.listar() is not None:
		arq.write(c.veiculos.listar())
	# Se nao, escreve str vazia no arquivo
	else:
		arq.write('')
	# Fecha o aquivo veiculos.txt definido como arq
	arq.close()

def limpar_tela():
	'''
	Function: 
		limpar_tela : Limpa a tela do terminal de operacao do sistema
	'''
	# Verifica o SO e executa o comando respectivo, se Linux ou Windows
	if platform == "linux" or platform == "linux2":
		os.system('clear')
	elif platform == "win32":
		os.system('cls')

def verifica_fim():
	'''
	Function: 
		verifica_fim : Recebe um valor da entrada e retorna se o sistema
			deve ser encerrado
	Summary: 
		parada (str) : Recebe da entrada padrao uma str 
	Returns: 
		True (bool) : Retorna True em caso de opcao para sair do sistema
	'''
	# Recebe da entrada padrao uma str de qualquer valor
	parada = input()	
	# Verifica se str transformada em minuscula e igual a 'sair', caso sim
	# retorna True para encerramento do sistema
	if (parada.lower() == 'sair'):
		return True

def carrega_lista(c):
	'''
	Function: 
		carrega_lista : Recebe como parametro a concessionaria e executa
			a leitura do arquivo de lista de veiculos(veiculos.txt)
			passando assim os dados para a lista interna do programa
	Summary: 
		arq (file) : Recebe arquivo aberto habilitado para escrita
		linhas (str) : Recebe da funcao readlines() do arquivo veiculos.txt
			uma str
		chassi 	(int) 	: Numero de chassi do veiculo.
		nome 	(str)	: Nome do veiculo correspondente ao chassi 
			informado
		ano 	(int)	: Ano de fabricacao do veiculo
		marca 	(str)	: Marca do veiculo 
		preco 	(float)	: Preco em Real do veiculo
	Attributes: 
		@param (c) (obj) : Objeto do tipo concessionaria
	'''
	# Abre arquivo veiculos.txt no modo de leitura e define nome como arq
	arq = open('arquivos/veiculos.txt', 'r')
	# Recebe da funcao readlines() do arquivo veiculos.txt uma str contendo
	# as linhas do arquivo 
	linhas = arq.readlines()
	
	# Laço para a leitura de cada linha das linhas do aquivo individualmente
	for linha in linhas:
		# Verifica conteudo da linha lida. E assum que conteudo restante da
		# linha, além da descricao do dado é o proprio dados, definindo assim
		# eles em suas respectivas variaveis
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
			# Adiciona o veiculo na lista de veiculos da concessionaria
			# com as informacoes do mesmo contidas nas variaveis definidas
			# a partir da leitura das linhas do arquivo
			c.veiculos.adicionar(int(chassi),nome, int(ano), marca, float(preco))
	# Fecha o aquivo veiculos.txt definido como arq
	arq.close()
