valorCompra = input('Valor da Compra: ')

if (valorCompra >= 100):
	print('Compra com desconto! Valor compra: {}'.format((valorCompra - (valorCompra*0.1))))
else:
	print('Compra sem deconto! Valor compra: {}'.format(valorCompra))
