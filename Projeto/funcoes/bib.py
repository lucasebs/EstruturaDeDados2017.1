from sys import platform
import os
import json

def menu():
	menu_w = ("Concesssionária Projeto ED IFPB\n\n"+
			"------------- MENU -------------\n"+
			" - 1 - : Buscar Veículo\n"+
			" - 2 - : Adicionar veiculo\n"+
			" - 3 - : Remover veiculo\n"+
			"--------------------------------\n")
	return menu_w

def apresentacao():
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

def captura_menu():
	op = input("- Informe a operação desejada: ")
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

def verifica_existencia_veiculo(c, chassi):
	vcl_busca = c.veiculos.buscar(chassi)
	if type(vcl_busca) is not str :
		if (vcl_busca.chassi == chassi):
			return True
		else:
			return False
		
def busca_veiculo(c):
	print("\n---- BUSCAR VEÍCULO -------")
	chassi = input("- Nº do Chassi do Veículo: ")
	veiculo = c.veiculos.buscar(chassi)
	print("\n--------------------------")
	print("- Informações do Veículo -")
	print("--------------------------")
	print(veiculo)
	print("--------------------------\n")

def adiciona_veiculo(c):
	iv = input_adiciona(c)
	c.veiculos.adicionar(iv[0], iv[1], iv[2], iv[3], iv[4])
	c.quantidade_veiculos += 1
	atualiza_arquivo(c)
	sucesso('a')

def remove_veiculo(c):
	print("\n---- REMOVER VEÍCULO ------")
	chassi = input("- Nº do Chassi do Veículo: ")
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

def sucesso(op):
	if (op == "a"):
		print("\nVEÍCULO ADICIONADO COM SUCESSO!\n")
	elif (op == "r"):
		print("\nVEÍCULO REMOVIDO COM SUCESSO!\n")	


def input_adiciona(c):
	print("\n---- ADICIONAR VEÍCULO ------------------------")
	print("-- Preencha abaixo as informações do Veículo --\n")

	chassi = input("- Nº do Chassi: ")
	if verifica_existencia_veiculo(c, chassi):
		print("VEÍCULO JÁ REGISTRADO NO SISTEMA!")
		return
	nome = input("- Nome: ")
	ano = input("- Ano: ")
	marca = input("- Marca: ")
	preco = input("- Preço: ")

	return (chassi, nome, ano, marca, preco)