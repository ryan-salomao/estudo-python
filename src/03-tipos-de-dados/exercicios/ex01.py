""" Exercício 01 """

numeros = input('Digite os números da lista (formato: n1, n2, n3...): ')
lista_numeros = numeros.split(", ")

numeros_int = []
for numero in lista_numeros:
    numeros_int.append(float(numero))

MAIOR = max(numeros_int, key=int)
MENOR = min(numeros_int, key=int)

print('O maior número é: ', MAIOR)
print('O menor número é: ', MENOR)
