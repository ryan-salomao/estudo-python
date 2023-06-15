""" Exercício 05 """



individuo = {
    'altura': float(input("Digite seu peso em (Kg): ")),
    'peso': float(input("Digite sua altura em (m): "))
}


def calcular_imc(individuo):
    """ retorna o imc de um individuo com base na altura e peso """

    peso = individuo["peso"]
    altura = individuo["altura"]


    IMC = peso / (altura * altura)
    
    return IMC



def obter_classificacao(IMC):
    """ retorna a classificação com base no imc """

    classificacao = ""


    if IMC < 18.5:

        classificacao = "Baixo peso"


    elif 18.5 <= IMC <= 24.9:

        classificacao = "Peso normal"


    elif 25.0 <= IMC <= 29.9:
        classificacao = "Excesso de peso"


    elif 30.0 <= IMC <= 34.9:
        classificacao = "Obesidade de Classe 1"


    elif 35.0 <= IMC <= 39.9:
        classificacao = "Obesidade de Classe 2"
    else:
        classificacao = "Obesidade de Classe 3"

    return classificacao



def situacao_individuo(IMC):
    """ retorna a situação ('normal', 'perder peso', 'ganhar peso') com base no imc """

    situacao = ""


    if IMC < 18.5:
        situacao = "ganhar peso"


    elif 18.5 <= IMC <= 24.9:
        situacao = "normal"


    elif 25.0 <= IMC <= 29.9:
        situacao = "perder peso"


    elif 30.0 <= IMC <= 34.9:
        situacao = "perder peso"


    elif 35.0 <= IMC <= 39.9:
        situacao = "perder peso"
    else:
        situacao = "perder peso"

    return situacao



IMC = calcular_imc(individuo)


classificacao = obter_classificacao(IMC)


situacao = situacao_individuo(IMC)


print("Classificacao atual:", classificacao)


print("Situacao atual:", situacao)


