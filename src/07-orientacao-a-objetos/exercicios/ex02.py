""" Exercício 02 """
from classes.projeto import Projeto


projeto1 = Projeto(1, 'Laboratório de Desenvolvimento de Software', 'Pedro Gomes')
projeto2 = Projeto.from_string("1,Laboratório de Manutenção de Hardware,João Santos")

print(projeto1)
print(projeto2)
print(projeto1 == projeto2)
