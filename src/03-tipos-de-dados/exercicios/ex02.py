""" Exercício 02 """


MES = int(input('Digite o número do mês: '))
VALIDACAO_MES = 0 < MES <= 12


if VALIDACAO_MES:
    meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
    MES_ESCOLHIDO = ""

    for i in range(len(meses)):
        if i == MES-1:
            MES_ESCOLHIDO = meses[i]
    print(MES_ESCOLHIDO)
else:
    print('Mês inválido')