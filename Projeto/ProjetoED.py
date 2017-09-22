from funcoes.app import *
from funcoes.bib import *
from adt.concessionaria import Concessionaria


c1 = Concessionaria()
carrega_lista(c1)

limpar_tela()
print(apresentacao())
verifica_fim()

while True: 

	limpar_tela()
	print(menu())
	estado = seleciona_menu(captura_menu(), c1)

	print("\nPressione Enter para continuar...")
	if verifica_fim() or estado:
		break
	

