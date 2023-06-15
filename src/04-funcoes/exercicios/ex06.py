""" Exercício 06 """


aquario = {

    'comprimento': float(input('Digite o comprimento do aquário em (cm): ')),

    'altura': float(input('Digite a altura do aquário em (cm): ')),

    'largura': float(input('Digite a largura do aquário em (cm): '))

}


termostato = {

    'temperatura_ambiente': float(input('Digite a temperatura do ambiente em (graus Cº): ')),

    'temperatura_desejada': float(input('Digite a temperatura desejada do aquário em (graus Cº): '))

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





