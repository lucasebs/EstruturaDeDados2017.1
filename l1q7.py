destino = input("Norte - 1\nNordeste - 2\nCentro Oeste - 3\nSul - 4\nInforme numero do destino: ")
idaVolta = raw_input('Ida e Volta [S ou N]: ')

if ( idaVolta == 'S' or idaVolta == 's'):
	if(destino == 1):
		print('Preco da passagem: RS 900,00')
	elif (destino == 2):
		print('Preco da passagem: RS650,00')
	elif (destino == 3):
		print('Preco da passagem: RS 600,00')
	elif (destino == 4):
		print('Preco da passagem: RS 550,00')
elif ( idaVolta == 'N' or idaVolta == 'n'):
	if(destino == 1):
		print('Preco da passagem: RS 500,00')
	elif (destino == 2):
		print('Preco da passagem: RS 350,00')
	elif (destino == 3):
		print('Preco da passagem: RS 350,00')
	elif (destino == 4):
		print('Preco da passagem: RS 300,00')