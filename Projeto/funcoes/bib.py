
def menu():
	menu_w = ("Concesssionária Projeto ED IFPB\n"+
			"------------- MENU -------------\n"+
			" - 1 - : Buscar Veículo\n"+
			" - 2 - : Adicionar veiculo\n"+
			" - 3 - : Remover veiculo\n")
	return menu_w
		
def busca_veiculo(self):
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
	atualiza_arquivo()

def remove_veiculo():
	print("---- REMOVER VEÍCULO ------\n")
	chassi = input("- Nº do Chassi do Veículo -\n")
	self.veiculos.remover(chassi)
	atualiza_arquivo()

def atualiza_arquivo():
	arq = open('arquivos/veiculos.txt','w')
	arq.write(self.veiculos.listar)
	arq.close()