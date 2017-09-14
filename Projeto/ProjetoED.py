from funcoes.bib import *
from adt.concessionaria import Concessionaria


c1 = Concessionaria()

while True: 
	limpar_tela()

	print(menu())
	seleciona_menu(captura_menu(), c1)

	if verifica_fim():
		break

