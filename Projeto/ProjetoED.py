from funcoes.bib import *
from adt.concessionaria import Concessionaria
from sys import platform
import os


c1 = Concessionaria()

while True: 
	print(menu())
	seleciona_menu(captura_menu(), c1)
	parada = input()	
	if (parada.lower() == 'sair'):
		break
	if platform == "linux" or platform == "linux2":
		os.system('clear')
	elif platform == "win32":
		os.system('cls')
