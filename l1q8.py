idade = input('Idade: ')
peso = input('Peso: ')

if ( peso>90 ):
	if ( idade>50 ):
		print('1')
	elif ( idade>20 ):
		print('4')
	else:
		print('7')
elif ( peso>60 ):
	if ( idade>50 ):
		print('2')
	elif ( idade>20 ):
		print('5')
	else:
		print('8')
else:
	if ( idade>50 ):
		print('3')
	elif ( idade>20 ):
		print('6')
	else:
		print('9')
