""" Exercício 03 """


def linha_para_dict(line, keys):
    
    values = line.strip().split(sep=',')
    dict_ = {}
   
    for i in range(len(keys)):
        dict_[keys[i]] = values[i]


    return dict_


def linhas_arquivos(file, keys):
    
    with open(file, "r", encoding="utf-8") as arquivo:

        lista_linhas = []

        for linha in arquivo:
            lista_linhas.append(linha_para_dict(linha, keys))
    
    
    return tuple(lista_linhas)


tupla_lista_compras = linhas_arquivos('src/06-arquivos/exercicios/lista_compras.txt', ['produto', 'quantidade'])

for tupla in tupla_lista_compras:
    print(tupla)
