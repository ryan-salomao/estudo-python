""" Exercício 03 """

def soma(numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma

soma = soma(numeros=(8.0, 7.2, 14.8))
print(soma)