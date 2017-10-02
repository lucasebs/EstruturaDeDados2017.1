from adt.pessoa import Pessoa

p1 = Pessoa()
p1.nome = "Pessoa_1" 
p1.ano_nascimento = 1995 
p1.email = "email_pessoa_1@email.com" 

print(p1.nome)
print(p1.ano_nascimento)
print(p1.email)

print(p1.obter_idade())
print(p1)
print("-----")
p2 = Pessoa()
p2.nome = "Pessoa_2" 
p2.ano_nascimento = 1990
p2.email = "email_pessoa_2@email.com" 

print(p2.nome)
print(p2.ano_nascimento)
print(p2.email)

print(p2.obter_idade())
print(p2)



print("-----")
p3 = Pessoa()
p3.nome = "Pessoa_3" 
p3.ano_nascimento = 1969
p3.email = "email_pessoa_3@email.com" 

print(p3.nome)
print(p3.ano_nascimento)
print(p3.email)

print(p3.obter_idade())
print(p3)

print("-----")