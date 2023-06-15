""" Exercício 06 """


COMPRIMENTO = float(input('Digite o comprimento do aquário em (cm): '))

ALTURA = float(input('Digite a altura do aquário em (cm): '))

LARGURA = float(input('Digite a largura do aquário em (cm): '))

TEMPERATURA_AMBIENTE = float(input('Digite a temperatura do ambiente em (graus Cº): '))

TEMPERATURA_DESEJADA = float(input('Digite a temperatura desejada do aquário em (graus Cº): '))


aquario = {

    'comprimento': COMPRIMENTO,

    'altura': ALTURA,

    'largura': LARGURA

}


termostato = {

    'temperatura_ambiente': TEMPERATURA_AMBIENTE,

    'temperatura_desejada': TEMPERATURA_DESEJADA

}


def volume(aquario):
    """ calcula o volume do aquário """

    comprimento = aquario['comprimento']

    altura = aquario['altura']

    largura = aquario['largura']


    volume = (comprimento * altura * largura) / 1000


    return volume


def potencia_necessaria(volume, termostato):
    """ calcula a potência necessária para o termostato do aquário """

    potencia = volume * 0.05 * (termostato['temperatura_ambiente'] - termostato['temperatura_desejada'])

    return potencia


def quantidade_filtragem(volume):
    """ calcula o mínimo de filtragem necessária para o aquário """

    min = volume * 2

    max = volume * 3

    filtragem = f'mínimo de {min} a {max} Litros'


    return filtragem 



VOLUME = volume(aquario)

POTENCIA = potencia_necessaria(VOLUME, termostato)

FILTRAGEM = quantidade_filtragem(VOLUME)


print('Volume do aquário em Litros:', VOLUME)

print('Potência do termostato necessaria em Watts:', POTENCIA)

print('Filtragem necessaria:', FILTRAGEM)





