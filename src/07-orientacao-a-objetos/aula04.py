""" Aula 04 - Propriedades """
from classes_aula.retangulo import Retangulo
# forma de controlar acesso aos atributos de uma instancia
# formas personalizadas de obter e alterar o valor de um atributo


retangulo1 = Retangulo(3.0, 3.0)

retangulo1.base = 3.0
retangulo1.altura = 3.0
print(retangulo1.base)
