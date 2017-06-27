soma = 0.0
quant = 0
while True:
	numero = input('Numero Inteiro: ')	

	if (numero < 0):
		print('Media dos {0} numeros lidos: {1}'.format(quant, soma/quant))
		break
	soma += numero
	quant += 1