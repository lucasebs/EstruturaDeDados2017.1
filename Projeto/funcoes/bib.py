

def menu():
	menu_w = ("Concesssionária Projeto ED IFPB\n"+
			"------------- MENU -------------\n"+
			" - 1 - : Buscar Veículo\n"+
			" - 2 - : Adicionar veiculo\n"+
			" - 3 - : Remover veiculo\n"+
			"--------------------------------\n")
	return menu_w

def captura_menu():
	op = input("- Informe a operação desejada: ")
	return op

def seleciona_menu(op, c):
	opcoes[op](c)

		
def busca_veiculo(c):
	print("---- BUSCAR VEÍCULO -------\n")
	chassi = input("- Nº do Chassi do Veículo -\n")
	veiculo = c.veiculos.buscar(chassi)
	print("Informações do Veículo:\n")
	print(veiculo)

def adiciona_veiculo(c):
	print("---- ADICIONAR VEÍCULO ------------------------\n")
	print("-- Preencha abaixo as informações do Veículo --\n")
	chassi = input("- Nº do Chassi -\n")
	nome = input("- Nome -\n")
	ano = input("- Ano  -\n")
	marca = input("- Marca -\n")
	preco = input("- Preço -\n")
	c.veiculos.adicionar(chassi, nome, ano, marca, preco)
	c.quantidade_veiculos += 1
	atualiza_arquivo()

def remove_veiculo(c):
	print("---- REMOVER VEÍCULO ------\n")
	chassi = input("- Nº do Chassi do Veículo -\n")
	c.veiculos.remover(chassi)
	c.quantidade_veiculos -= 1
	atualiza_arquivo()

def atualiza_arquivo(self):
	arq = open('arquivos/veiculos.txt','w')
	arq.write(self.veiculos.listar)
	arq.close()

opcoes = {'1' : busca_veiculo, '2' : adiciona_veiculo, '3' : remove_veiculo}

