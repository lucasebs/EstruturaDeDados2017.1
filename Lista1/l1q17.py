nomes = []

while True:
	nome = raw_input('Nome para guardar na lista: ')

	if (nome.lower() == 'fechar'):
		for nomeLista in nomes:
			print(nomeLista)

		break

	nomes.append(nome)

