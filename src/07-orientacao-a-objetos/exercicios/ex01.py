""" Exercício 01 """
from classes import aluno as al


aluno1 = al.Aluno('SP010101', 'Joãoxinho', 'jaum@email')
aluno2 = al.Aluno.from_string("SP010101,Xorginho,xorge@email.com")

print(aluno1)
print(aluno2)
print(aluno1 == aluno2)
