from adt.ponto import Ponto
from adt.retangulo import Retangulo

p1 = Ponto(-3,3)
p2 = Ponto(-3,0)
p3 = Ponto(3,0)
p4 = Ponto(3,3)

r1 = Retangulo(p1, p2, p3, p4)

p5 = Ponto(0,0)
p6 = Ponto(0,4)
p7 = Ponto(4,0)
p8 = Ponto(4,4)


r2 = Retangulo(p5, p6, p7, p8)

print(r1)
print(r2)

print(r1.area())

print(r2.area())

r1.quadrado()
r2.quadrado()