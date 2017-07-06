from l1q25 import Pessoa 

pessoas = [None]*2

for i in range(0, len(pessoas)):
	pNome = raw_input("Primeiro Nome: ")
	sNome = raw_input("Sobrenome: ")
	cpf = int(input("CPF: "))
	anoNasc = int(input("Ano de Nascimento: "))

	pessoaTemp = Pessoa()
	pessoaTemp.primeiroNome = pNome
	pessoaTemp.sobrenome = sNome
	pessoaTemp.cpf = cpf
	pessoaTemp.anoNascimento = anoNasc
	pessoas[i] = pessoaTemp


for i in range(0, len(pessoas)):
	print(' ---- ' + str(i+1) + ' Pessoa' + ' ---- ')
	print(pessoas[i])


