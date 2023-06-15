""" Exercício 05 """


breakpoint()


pessoa = {
    "peso": float(input("Digite seu peso em (Kg): ")),
    "altura": float(input("Digite sua altura em (m): "))
}


def calcular_imc(individuo):
    """retorna o imc de um individuo com base na altura e peso"""

    peso = individuo["peso"]

    altura = individuo["altura"]

    imc = peso / (altura * altura)

    return imc


def obter_classificacao(imc):
    """retorna a classificação com base no imc"""

    classificacao = ""

    if imc < 18.5:
        classificacao = "Baixo peso"

    elif 18.5 <= imc <= 24.9:
        classificacao = "Peso normal"

    elif 25.0 <= imc <= 29.9:
        classificacao = "Excesso de peso"

    elif 30.0 <= imc <= 34.9:
        classificacao = "Obesidade de Classe 1"

    elif 35.0 <= imc <= 39.9:
        classificacao = "Obesidade de Classe 2"
    else:
        classificacao = "Obesidade de Classe 3"

    return classificacao


def situacao_individuo(imc):
    """retorna a situação ('normal', 'perder peso', 'ganhar peso') com base no imc"""

    situacao = ""

    if imc < 18.5:
        situacao = "ganhar peso"

    elif 18.5 <= imc <= 24.9:
        situacao = "normal"

    elif 25.0 <= imc <= 29.9:
        situacao = "perder peso"

    elif 30.0 <= imc <= 34.9:
        situacao = "perder peso"

    elif 35.0 <= imc <= 39.9:
        situacao = "perder peso"
    else:
        situacao = "perder peso"

    return situacao


IMC = calcular_imc(pessoa)


CLASSIFICACAO = obter_classificacao(IMC)


SITUACAO = situacao_individuo(IMC)


print("Classificacao atual:", CLASSIFICACAO)


print("Situacao atual:", SITUACAO)
