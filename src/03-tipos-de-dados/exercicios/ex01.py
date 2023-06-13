""" Exercício 01 """

numeros = input('Digite os números da lista (formato: n1, n2, n3...): ')
lista_numeros = numeros.split(", ")

numeros_float = []
for numero in lista_numeros:
    numeros_float.append(float(numero))

MAIOR = max(numeros_float, key=float)
MENOR = min(numeros_float, key=float)

print('O maior número é: ', MAIOR)
print('O menor número é: ', MENOR)
