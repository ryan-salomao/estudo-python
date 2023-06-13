""" Exercício 03 """

IDENTIFICADOR_FUNCIONARIO = input('digite o código de identificação do funcionário: ')
IDENTIFICADOR_INVALIDO = 'Código identificador inválido'


if len(IDENTIFICADOR_FUNCIONARIO) != 7:
    print(IDENTIFICADOR_INVALIDO)
elif 'BR' not in IDENTIFICADOR_FUNCIONARIO:
    print(IDENTIFICADOR_INVALIDO)
elif IDENTIFICADOR_FUNCIONARIO[0] != 'B' or IDENTIFICADOR_FUNCIONARIO[1] != 'R':
    print(IDENTIFICADOR_INVALIDO)
elif 1 <= int(IDENTIFICADOR_FUNCIONARIO[2:6]) <= 9999: 
    print(IDENTIFICADOR_INVALIDO)
elif IDENTIFICADOR_FUNCIONARIO[6] != 'X':
    print(IDENTIFICADOR_INVALIDO)
else:
    print('Identificador válido')
