""" Aula 03 - loop for """

# 1. Repetir instrução
# 2. iteração em coleção de elementos


linguagens = ['C', 'Python', 'Java', 'Rust']

print(linguagens[0])
print(linguagens[1])
print(linguagens[2])

# for valor in colecao:
#     instrucao
#     instrucao
#     instrucao


for linguagem in linguagens:
    print(linguagem.upper())

# Comportamento do operador in é
# diferente com base no contexto
print('Java' in linguagens)

nota1 = 10.0
nota2 = 5.5
nota3 = 8.3

media = (nota1 + nota2 + nota3)
print(media)

notas = [10, 5.5, 8.3, 2.5]

soma = 0
for nota in notas:
    soma += nota

media = soma / len(notas)
print(media)


# range
# valores = range(10)
# valores = range(0, 10)
# valores = range(0, 11, 2)
valores = range(9, -1, -2)
print(valores)

for valor in valores:
    print(valor)

for i in range(len(linguagens)):
    print(linguagens[i])

for linguagem in linguagens:
    print(linguagem)
