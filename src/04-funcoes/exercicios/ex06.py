""" Exercício 06 """


COMPRIMENTO = float(input('Digite o comprimento do aquário em (cm): '))

ALTURA = float(input('Digite a altura do aquário em (cm): '))

LARGURA = float(input('Digite a largura do aquário em (cm): '))


aquario = {

    'comprimento': COMPRIMENTO,

    'altura': ALTURA,

    'largura': LARGURA

}


def volume(aquario):
    """ calcula o volume do aquário """

    comprimento = aquario['comprimento']

    altura = aquario['altura']

    largura = aquario['largura']


    volume = (comprimento * altura * largura) / 1000


    return volume


def potencia_necessaria(volume):
    """ calcula a potência necessária para o termostato do aquário """
    temperatura_ambiente = 22

    temperatura_desejada = 20


    potencia = volume * 0.05 * (temperatura_ambiente - temperatura_desejada)

    return potencia


def quantidade_filtragem(volume):
    """ calcula o mínimo de filtragem necessária para o aquário """

    min = volume * 2

    max = volume * 3

    filtragem = f'mínimo de {min} a {max} Litros'



    return filtragem 



VOLUME = volume(aquario)

POTENCIA = potencia_necessaria(VOLUME)

FILTRAGEM = quantidade_filtragem(VOLUME)


print('Volume do aquário em Litros:', VOLUME)

print('Potência do termostato necessaria:', POTENCIA)

print('Filtragem necessaria:', FILTRAGEM)





