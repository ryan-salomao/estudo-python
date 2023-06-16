""" Exercício 01 """


def carregar_dados_alunos(arquivo):
    with open(arquivo, "r", encoding="utf-8") as arq:

        dados_alunos = []

        for linha in arq:
            dados_aluno = linha.split(sep=',')
            dicionario_dados_aluno = {
                'prontuario': dados_aluno[0],
                'nome': dados_aluno[1],
                'email': dados_aluno[2]
            }

            dados_alunos.append(dicionario_dados_aluno)
                

    return tuple(dados_alunos)


tupla_dados_alunos = carregar_dados_alunos("src/06-arquivos/exercicios/dados_alunos.txt")

for tupla in tupla_dados_alunos:
    print(tupla)
