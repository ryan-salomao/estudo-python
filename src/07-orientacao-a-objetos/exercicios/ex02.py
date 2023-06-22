""" Exercício 02 """
from classes import projeto as pj


projeto1 = pj.Projeto(1, 'Laboratório de Desenvolvimento de Software', 'Pedro Gomes')
projeto2 = pj.Projeto.from_string("1,Laboratório de Manutenção de Hardware,João Santos")

print(projeto1)
print(projeto2)
print(projeto1 == projeto2)
