from funcoes.bib import *
from adt.concessionaria import Concessionaria


c1 = Concessionaria()

while True: 
	print(menu())
	seleciona_menu(captura_menu(), c1)
	parada = input()
	if (parada == -1):
		break




