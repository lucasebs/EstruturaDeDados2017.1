from adt.lista_pessoas import Lista_pessoas
from adt.pessoa import Pessoa


lista = Lista_pessoas()
while True:
	nome = input("Informe Nome da Pessoa: ")
	if nome.lower() == "fechar":
		break
	ano_nascimento = input("Ano de Nascimento: ")
	email = input("E-mail: ")
	lista.adicionar(nome, ano_nascimento, email)

print(lista.listar())

