""" Exercício 02 """

notas = input("Digite as notas 1, 2 e 3: ")
lista_de_notas = notas.split(", ")

notas_float = []
for nota in lista_de_notas:
    notas_float.append(float(nota))

soma = 0
for nota in notas_float:
    soma += nota

def validacao(notas):
    lista_validada = []
    for nota in notas:
        if 0 <= nota <= 10:
           lista_validada.append(nota) 
    return lista_validada

if validacao(notas_float) == notas_float:
    media = soma / len(notas_float)
    if media >= 6:
        print('Aprovado')
    elif media >= 4:
        print('Recuperação')
    else:
        print('Reprovado')
else:
    print('Notas inválidas')