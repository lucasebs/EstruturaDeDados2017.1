opcoes = {
	1:busca_veiculo(),
	2:adiciona_veiculo(),
	3:remove_veiculo()
}	


def menu():
	menu_w = ("Concesssionária Projeto ED IFPB\n"+
			"------------- MENU -------------\n"+
			" - 1 - : Buscar Veículo\n"+
			" - 2 - : Adicionar veiculo\n"+
			" - 3 - : Remover veiculo\n"+
			"------------- MENU -------------\n")
	return menu_w

def captura_menu():
	op = input("- Informe a operação desejada: ")
	return op

		
def busca_veiculo(self):
	print("---- BUSCAR VEÍCULO -------\n")
	chassi = input("- Nº do Chassi do Veículo -\n")
	veiculo = self.veiculos.buscar(chassi)
	print("Informações do Veículo:\n")
	print(veiculo)

def adiciona_veiculo(self):
	print("---- ADICIONAR VEÍCULO ------------------------\n")
	print("-- Preencha abaixo as informações do Veículo --\n")
	chassi = input("- Nº do Chassi -\n")
	nome = input("- Nome -\n")
	ano = input("- Ano  -\n")
	marca = input("- Marca -\n")
	preco = input("- Preço -\n")
	self.veiculos.adicionar(chassi, nome, ano, marca, preco)
	self.quantidade_veiculos += 1
	atualiza_arquivo()

def remove_veiculo(self):
	print("---- REMOVER VEÍCULO ------\n")
	chassi = input("- Nº do Chassi do Veículo -\n")
	self.veiculos.remover(chassi)
	self.quantidade_veiculos -= 1
	atualiza_arquivo()

def atualiza_arquivo(self):
	arq = open('arquivos/veiculos.txt','w')
	arq.write(self.veiculos.listar)
	arq.close()

