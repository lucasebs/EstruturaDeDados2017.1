from l1q23 import Carro

carros = [None]*2

for i in range(0, len(carros)):
	nome = raw_input("Nome(modelo) do carro: ")
	anoFab = int(input("Ano de Fabricacao do carro: "))
	anoRev = int(input("Ano da Ultima revisao do carro: "))
	km = int(input("Quilometragem: "))

	carroTemp = Carro(nome, anoFab, anoRev, km)
	carros[i] = carroTemp

for i in range(0, len(carros)):
	print('Carro ' + str(i+1))
	print(carros[i])

