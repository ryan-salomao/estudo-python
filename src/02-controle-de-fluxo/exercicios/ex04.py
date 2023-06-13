""" Exercício 04 """

IDENTIFICADOR_FUNCIONARIO = input('digite o código de identificação do funcionário: ')
erros = []


if len(IDENTIFICADOR_FUNCIONARIO) != 7:
    erros.append('O identificador não possui 7 caracteres')

if IDENTIFICADOR_FUNCIONARIO[0] != 'B' or IDENTIFICADOR_FUNCIONARIO[1] != 'R':
    erros.append('O identificador não inicia com a sequencia "BR"')

if 1 <= int(IDENTIFICADOR_FUNCIONARIO[2:6]) <= 9999: 
    erros.append('O identificador não apresenta números inteiros entre 0001 e 9999')

if IDENTIFICADOR_FUNCIONARIO[6] != 'X':
    erros.append('O identificador não finaliza com o caracter X')
    
if erros:
    print('Identificador Informado: ', IDENTIFICADOR_FUNCIONARIO, '\nErros:')
    for erro in erros:
        print('* ', erro)
else:
    print('Identificador válido')
