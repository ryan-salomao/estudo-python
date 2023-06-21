""" Funções utilizadas no desafio 108 """

def metade(value):
    return value / 2


def dobro(value):
    return value * 2


def aumentar(value, aumento):
    return value + ((aumento / 100) * value)


def diminuir(value, desconto):
    return value - ((desconto / 100) * value)


def moeda(value):
    return f"R${value:.2f}"
