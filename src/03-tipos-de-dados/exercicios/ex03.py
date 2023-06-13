""" Exercício 03 """


MES = int(input('Digite o número do mês: '))
VALIDACAO_MES = 0 < MES <= 12


if VALIDACAO_MES:
    meses = {
            1: 'Janeiro', 
            2: 'Fevereiro', 
            3: 'Março', 
            4: 'Abril', 
            5: 'Maio', 
            6: 'Junho', 
            7: 'Julho', 
            8: 'Agosto', 
            9: 'Setembro', 
            10: 'Outubro', 
            11: 'Novembro', 
            12: 'Dezembro'
        }
    MES_ESCOLHIDO = ""

    for key, value in meses.items():
        if key == MES:
            MES_ESCOLHIDO = value 
    print(MES_ESCOLHIDO)
else:
    print('Mês inválido')