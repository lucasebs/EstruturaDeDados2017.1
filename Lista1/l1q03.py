salarioInicial = input('Salario do funcionario: ')
salarioAumento = 0
salarioFinal = 0

salarioAumento = salarioInicial + (salarioInicial * 0.15)
salarioFinal = salarioAumento - (salarioAumento * 0.08)

print('Salario Inicial: {0}\nSalario com aumento: {1}\nSalario Final:{2}'.format(salarioInicial, salarioAumento, salarioFinal))
