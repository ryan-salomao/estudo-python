""" Aula 01 - Manipulando Arquivos """

# open("caminho","r")

# r- leitura
# a - Append / incrementar
# w - Escrita
# x - Criar Arquivo
# r+ - Leitura + Escrita

# arquivo = open("src/06-arquivos/test3.txt", "x", encoding="utf-8")

# print(arquivo.readable())
# print(arquivo.read())
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())

# lista = arquivo.readlines()

# print(lista)

# print(lista[3])

# arquivo.write("Python\n")
# arquivo.write("C++\n")
# arquivo.write("Terraform\n")


# arquivo.close()

import os 

# if os.path.exists("src/06-arquivos/test2.txt"):
#     os.remove("src/06-arquivos/test2.txt")
# else:
#     print("Arquivo não existe")

os.rmdir("src/06-arquivos/nova_pasta")
