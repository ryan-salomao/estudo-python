""" Aula 05 - Métodos especiais """
from classes_aula.retangulo import Retangulo

retangulo1 = Retangulo(10.0, 5.0)
retangulo2 = Retangulo(3.0, 15.0)

print(retangulo1.__repr__)

retangulo3 = eval('Retangulo(7.5,12.3)')
retangulo4 = eval(repr(retangulo3))

print(retangulo1)
print(retangulo2)
print(retangulo3)
print(retangulo4)
