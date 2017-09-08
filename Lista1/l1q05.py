sexo = raw_input('Sexo [M ou F]:')
altura = input('Altura: ')

if (sexo == 'F' or sexo == 'f'):
	print('Seu peso ideal: {}'.format((altura*altura) * 22))
elif (sexo == 'M' or sexo == 'm'):
	print('Seu peso ideal: {}'.format((altura*altura) * 23))
else:
	print('Sexo incorreto!')
