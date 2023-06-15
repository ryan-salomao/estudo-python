""" Exercício 06 """

breakpoint()


aquario = {


    'comprimento': float(input('Digite o comprimento do aquário em (cm): ')),


    'altura': float(input('Digite a altura do aquário em (cm): ')),


    'largura': float(input('Digite a largura do aquário em (cm): '))


}




termostato = {

    'temperatura_ambiente': float(input('Digite a temperatura do ambiente em (graus Cº): ')),


    'temperatura_desejada': float(input('Digite a temperatura desejada do aquário em (graus Cº): '))


}




def volume_recipiente(recipiente):

    """ calcula o volume do aquário """


    comprimento = recipiente['comprimento']


    altura = recipiente['altura']


    largura = recipiente['largura']



    volume = (comprimento * altura * largura) / 1000



    return volume



def potencia_necessaria(volume, temperaturas):


    """ calcula a potência necessária para o termostato do aquário """



    potencia = volume * 0.05 * (temperaturas['temperatura_ambiente'] - temperaturas['temperatura_desejada'])

    return potencia



def quantidade_filtragem(volume):


    """ calcula o mínimo de filtragem necessária para o aquário """


    minimo = volume * 2


    maximo = volume * 3


    filtragem = f'mínimo de {minimo} a {maximo} Litros'



    return filtragem 




VOLUME = volume_recipiente(aquario)


POTENCIA = potencia_necessaria(VOLUME, termostato)


FILTRAGEM = quantidade_filtragem(VOLUME)



print('Volume do aquário em Litros:', VOLUME)


print('Potência do termostato necessaria em Watts:', POTENCIA)


print('Filtragem necessaria:', FILTRAGEM)






