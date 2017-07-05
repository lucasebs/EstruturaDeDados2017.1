especies = []

def TuplaEspecies(listaEspecies):
	return tuple(listaEspecies)

while True:
	especie = raw_input('Inserir Especie: ')

	if (especie.lower() == 'fim'):
		print(TuplaEspecies(especies))
		break

	especies.append(especie)