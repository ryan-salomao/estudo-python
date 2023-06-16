""" Exercício 02 """


def carregar_dados_projetos(arquivo):

    with open(arquivo, "r", encoding="utf-8") as arq:

        dados_projetos = []

        for linha in arq:
            dados_projeto = linha.split(sep=',')

            dicionario_dados_projeto = {
                'codigo': int(dados_projeto[0]),
                'titulo': dados_projeto[1],
                'responsavel': dados_projeto[2]
            }

            dados_projetos.append(dicionario_dados_projeto)


    return tuple(dados_projetos)


tupla_dados_projetos = carregar_dados_projetos("src/06-arquivos/exercicios/dados_projeto.txt")

for tupla in tupla_dados_projetos:
    print(tupla)