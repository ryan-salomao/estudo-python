""" Exercício 04 """
breakpoint()

def soma(*args):
    soma = 0
    for numero in args:
        soma += numero
    return soma

soma = soma(8.0, 7.2, 14.8)
print(soma)