from funcoes.app import *
from funcoes.bib import *
from adt.concessionaria import Concessionaria

# Cria objeto do tipo Concessionaria
c1 = Concessionaria()
# Carrega do arquivo na lista os veiculos da concessionaria passada como parametro
carrega_lista(c1)

# Limpa tela do terminal de execucao do sistema
limpar_tela()
# Exibe apresentacao do sistema, pagina inicial contendo nome, dicas e uso e 
# desenvolvedores
print(apresentacao())
# Verifica fim da execucao do sistema
verifica_fim()

while True: 
	
	# Limpa tela do terminal de execucao do sistema
	limpar_tela()
	# Exibe menu inicial do sistema, contendo opcoes de operacao
	print(menu())
	# Recebe estado de finalizacao do sistema da funcao seleciona_menu()
	estado = seleciona_menu(captura_menu(), c1)

	print("\nPressione Enter para continuar...")
	# Verifica fim da execucao do sistema ou recebe o estado de finalizado,
	# caso sim, interrompe o laço de execução
	if verifica_fim() or estado:
		break
	

