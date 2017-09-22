from .app import * 

def menu():
	'''
	Function: 
		menu : Menu Inicial do Pojeto Concessionaria	
	Summary: 
		menu_w (str) : String montando conteúdo estrutural do 
		Menu iniciar exibindo as suas funções principais.
		1 - Buscar Veiculo
		2 - Adicinar Veiculo
		3 - Remover Veiculo 
	Returns: 
		menu_w (str) 
	'''
	menu_w = ("\n------- Concesssionária Projeto ED IFPB -------\n\n"+
				"-------------------- MENU ---------------------\n"+
				" - 1 - : Buscar Veículo\n"+
				" - 2 - : Adicionar veiculo\n"+
				" - 3 - : Remover veiculo\n"+
				"-----------------------------------------------\n")
	return menu_w

def apresentacao():
	'''
	Function: 
		apresentacao : Pagina inicial do Projeto Concessionaria.
	Summary: 
		apresentacao (str) : String montando conteúdo estrutural da 
		página inicial do projeto, apresentando guia/dicas para o uso
		do Projeto Concessionaria
	Returns: 
		apresentacao (str)
	'''
	apresentacao = ('  Bem vindo ao Sistema da Concesssionária Projeto ED IFPB\n\n'+
					'  Dicas de Uso:\n'+
					'	  - Para finalizar a execução do programa, basta digitar "sair"\n'+
					'	    no menu "Informe a operação desejada, logo após a execução\n '+
					'	    de alguma atividade(buscar,adicionar ou remover) ou durante\n'+
					'		a mensagem "Pressione Enter para continuar..."\n\n'
					'  Desenvolvido por:\n'+
					'     - Leonardo\n'+
					'     - Lucas\n'+
					'     - Vinícius\n\n'+
					'  Pressione Enter para iniciar...')
	return apresentacao

def cabecalho(op):
	'''
	Function: 
		cabecalho : Exibe o cabecalho da operacao recebida como parametro
	Attributes: 
		@param (op) (str) : String  de identificacao da operacao.
			'b' -	Buscar Veiculo
			'a' -	Adicionar Veiculo
			'r' -   Remover Veiculo
	'''
	# Verifica qual a operacao e imprime o respectivo cabecalho
	if (op == 'b'):
		print("\n---- BUSCAR VEÍCULO ---------------------------\n")
	elif (op == 'a'):
		print("\n---- ADICIONAR VEÍCULO ------------------------")
		print("-- Preencha abaixo as informações do Veículo --\n")
	elif (op == 'r'):
		print("\n---- REMOVER VEÍCULO --------------------------\n")

def verifica_existencia(c, chassi):
	'''
	Function: 
		verifica_existencia : Função que verifica se no registro da
		concessionaria ja contem o veiculo passado como parametro.
	Summary: 
		vcl_busca (ojb) : Objeto do tipo veiculo.
	Attributes: 
		@param (c) (obj) : Objeto do tipo Concessionaria
		@param (chassi) (int) : Inteiro contendo o número do chassi
		do veiculo para verificacao
	Returns: 
		True (bool) : Se veiculo ja está registrado na concessionaria
		False (bool) : Se veiculo não está registrado na concessionaria
	'''
	# Recebe da função buscar(), da lista veiculos da concessionaria c,
	# um objeto do tipo veiculo, correspondente ao chassi passado como
	# parametro. Ou recebe str informando que chassi não está nos registros
	vcl_busca = c.veiculos.buscar(chassi)
	# Verifica se vcl_busca não é do tipo str, sendo assim um obj
	if type(vcl_busca) is not str :
		if (vcl_busca.chassi == chassi):
			return True
		else:
			return False

def sucesso(op):
	'''
	Function: 
		sucesso : Exibe na tela mensagem de sucesso na operacao
	Attributes: 
		@param (op) (str) : String  de identificacao da operacao.
			'a' -	Adicionar Veiculo
			'r' -   Remover Veiculo
	'''
	# Verifica qual a operacao e imprime a respectiva mensagem de sucesso
	if (op == "a"):
		print("\nVEÍCULO ADICIONADO COM SUCESSO!\n")
	elif (op == "r"):
		print("\nVEÍCULO REMOVIDO COM SUCESSO!\n")	

def captura_entrada(c, op):
	'''
	Function: 
		captura_entrada : Captura dados da entrada padrao e retorna 
			para as respectivas operacoes
	Summary: 
		chassi 	(int) 	: Numero de chassi do veiculo.
		nome 	(str)	: Nome do veiculo correspondente ao chassi 
			informado
		ano 	(int)	: Ano de fabricacao do veiculo
		marca 	(str)	: Marca do veiculo 
		preco 	(float)	: Preco em Real do veiculo
		verifica (bool) : Recebe retorno da funcao verifica_existencia()
	Attributes: 
		@param (c) (obj) : Objeto do tipo Concessionaria
		@param (op) (str) : String  de identificacao da operacao.
			'b' - Buscar Veiculo
			'a' - Adicionar Veiculo
			'r' - Remover Veiculo
	Returns: 
		chassi (int) : Retorna um numero do chassi lido da entrada 
			padrao 
		(chassi, nome, ano, marca, preco) (tupla ) : Retorna uma tupla
			com dados lidos na entrada padrao 
		True (bool) : Retorna valor booleano se veiculo já tiver sido
			registrado na concessionaria
	'''
	# Recebe da entrada padrao numero do chassi do veiculo
	chassi = int(input(" - Nº do Chassi do Veículo: "))
	
	# Verifica a operacao recebida como parametro. 
	# Se operacao = busca ou remocao o unico dado lido é o numero do chassi.
	if (op == 'b' or op == 'r'):
		return chassi
	# Se operacao = adicao, dados restantes sao lidos da entrada padrao
	elif (op == 'a'):
		# Recebe da funcao verifica_existencia() valor booleano
		# True - Se veiculo ja está registrado na concessionaria
		# False - Se veiculo não está registrado na concessionaria
		verifica = verifica_existencia(c, chassi)
		# Verifica se variavel 'verifica'
		# True - Exibe na tela que veiculo já foi registrado e retorna 
		# valor booleano para fora da funcao. 
		if verifica:
			print("Veículo já registrado na concessionária!")
			return True
		# Recebem da entrada padrao
		# str com o nome do veiculo
		nome = input(" - Nome: ")
		# int com o ano de fabricacao do veiculo
		ano = int(input(" - Ano: "))
		# str com a marca do veiculo
		marca = input(" - Marca: ")
		# float com o preco em Real do veiculo
		preco = float(input(" - Preço: "))
		
		# Retorna Tupla com os dados do veiculo para ser adicionado
		# na concessionaria
		return (chassi, nome, ano, marca, preco)		

def imprime_veiculo(veiculo):
	'''
	Function: 
		imprime_veiculo : Exibe na tela informacoes recebidas como parametro
	Attributes: 
		@param (veiculo) (str) : 
	'''
	# Verifica se o parametro recebido sao informacoes do veiculo ou
	# informacoes de registro da concessionaria
	if (veiculo == "Sem veículos na concessionária!" or	
		veiculo == "Veículo não registrado na concessionária!"):
		print('\n{}\n'.format(veiculo))
	else:
		print("\n----------------------------------")
		print("- Informações do Veículo ---------")
		print("----------------------------------")
		print('\n{}'.format(veiculo))
		print("----------------------------------")
