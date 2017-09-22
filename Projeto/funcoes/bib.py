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
	if (op == "a"):
		print("\nVEÍCULO ADICIONADO COM SUCESSO!\n")
	elif (op == "r"):
		print("\nVEÍCULO REMOVIDO COM SUCESSO!\n")	

def captura_entrada(c, op):
	chassi = int(input(" - Nº do Chassi do Veículo: "))
	if (op == 'b' or op == 'r'):
		return chassi
	elif (op == 'a'):
		verifica = verifica_existencia(c, chassi)
		if verifica:
			print("Veículo já registrado na concessionária!")
			return True
		nome = input(" - Nome: ")
		ano = int(input(" - Ano: "))
		marca = input(" - Marca: ")
		preco = float(input(" - Preço: "))

		return (chassi, nome, ano, marca, preco)

def cabecalho(op):
	if (op == 'b'):
		print("\n---- BUSCAR VEÍCULO ---------------------------\n")
	elif (op == 'a'):
		print("\n---- ADICIONAR VEÍCULO ------------------------")
		print("-- Preencha abaixo as informações do Veículo --\n")
	elif (op == 'r'):
		print("\n---- REMOVER VEÍCULO --------------------------\n")
		

def imprime_veiculo(veiculo):
	if (veiculo == "Sem veículos na concessionária!" or	
		veiculo == "Veículo não registrado na concessionária!"):
		print('\n{}\n'.format(veiculo))
	else:
		print("\n----------------------------------")
		print("- Informações do Veículo ---------")
		print("----------------------------------")
		print('\n{}'.format(veiculo))
		print("----------------------------------")
