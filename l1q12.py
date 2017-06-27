def Maior(num1, num2):
	if (num1 > num2):
		return num1
	elif (num2 > num1):
		return num2

int1 = input('Informe Inteiro 1: ')
int2 = input('Informe Inteiro 2: ')

print('O maior inteiro eh: {}'.format(Maior(int1, int2)))