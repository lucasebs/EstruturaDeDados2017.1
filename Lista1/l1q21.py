'''
Chave = Nome edificio
Valor = endereco edificio
'''
dicEdificios = {}

def inserir_edificio(nome, endereco):
	dicEdificios[nome] = [nome, endereco]


def consultar_edificio(nome):
	return tuple(dicEdificios[nome])

inserir_edificio('ed1','rua1')
inserir_edificio('ed2','rua2')
inserir_edificio('ed3','rua3')

print(consultar_edificio('ed1'))
print(consultar_edificio('ed3'))
print(consultar_edificio('ed2'))
