'''
Chave = Matriculas dos alunos,
Valor = nome, idade, cpf
'''
dicAlunos = {}

def inserir_aluno(matricula, informacoes):
	dicAlunos[matricula] = [matricula, informacoes]


def consultar_aluno(matricula):
	return tuple(dicAlunos[matricula])

def imprimir_alunos():
	print dicAlunos


def valores_alunos():
	return dicAlunos.values()


    
inserir_aluno(123, ['a', 10, 159])
inserir_aluno(456, ['b', 11, 357])
inserir_aluno(789, ['c', 12, 951])

print(consultar_aluno(456))
print(consultar_aluno(123))
print(consultar_aluno(789))

print ('Alunos:')

imprimir_alunos()

print ('Valores:') 
for i in valores_alunos():
	print i
