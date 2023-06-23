""" Exercício 04 """
from classes.aluno import Aluno
from classes.projeto import Projeto
from classes.participacao import Participacao


aluno1 = Aluno("SP010101", "Joãoxinho", "jaum@email")

projeto1 = Projeto(1, "Laboratório de Desenvolvimento de Software", "Pedro Gomes")

participacao1 = Participacao(1, "22/05/2023", "07/09/2023", aluno1, projeto1)

projeto1.add_participacao(participacao1)


print("\n", projeto1, "\n")
