somaImpares = 0

limiteInferior = input('Limite Inferior do Intervalo: ')
limiteSuperior = input('Limite Superior do Intervalo: ')

for i in range(limiteInferior, limiteSuperior+1):
	if( i%2 != 0 ):
		somaImpares += i

print('Soma dos Nimeros Impares do Intervalo [{0}-{1}]: {2}'.format(limiteInferior, limiteSuperior, somaImpares))
