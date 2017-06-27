nomeAluno = raw_input("Nome do aluno: ")
quantDias = input("Quantidade de dias na semana: ")
tipoCurso = raw_input("Tipo do curso [B - Basico, I - Intermediario, A - Avancado]: ")

if (tipoCurso == 'B' or tipoCurso == 'b'):
	print('Valor total: {}'.format((quantDias*7)*15))
elif (tipoCurso == 'I' or tipoCurso == 'i'):
	print('Valor total: {}'.format((quantDias*8.5)*20))
elif (tipoCurso == 'A' or tipoCurso == 'a'):
	print('Valor total: {}'.format((quantDias*10)*25))
else:
	print('Tipo informado incorreto!')