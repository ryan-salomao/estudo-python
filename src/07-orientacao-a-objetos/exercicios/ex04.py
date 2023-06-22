""" Exercício 04 """
from classes import aluno as al
from classes import projeto as pj
from classes import participacao as pt


aluno1 = al.Aluno("SP010101", "Joãoxinho", "jaum@email")

projeto1 = pj.Projeto(1, "Laboratório de Desenvolvimento de Software", "Pedro Gomes")

participacao1 = pt.Participacao(1, "22/05/2023", "07/09/2023", aluno1, projeto1)

projeto1.add_participacao(participacao1)


print("\n", projeto1, "\n")
