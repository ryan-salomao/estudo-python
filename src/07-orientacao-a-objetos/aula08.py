""" Aula 08 - Heranças entre Classes """

class Pessoa: # SUPER CLASSE
    def __init__(self, nome, sobrenome, cpf):
        print("Entrei no SUPER CONSTRUTOR")
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
    
    def obtem_nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

class Cliente(Pessoa): # SUB CLASSE
    def __init__(self, nome, sobrenome, cpf):
        super().__init__(nome, sobrenome, cpf)
        self.compras = []

    # def adiciona_compra(self, valor):
    #     print("Compra no valor")
    #     self.compras.append(valor)

class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, salario):
        super().__init__(nome, sobrenome, cpf)
        self.salario = salario
    
    def calcula_pagamento(self):
        return self.salario - ((10/100) * self.salario)

class Programador(Funcionario):
    def __init__(self, nome, sobrenome, cpf, salario, bonus):
        super().__init__(nome, sobrenome, cpf, salario)
        self.bonus = bonus

    def calcula_pagamento(self):
        pagamentos_salario = super().calcula_pagamento()
        return pagamentos_salario + self.bonus

programador = Programador("José", "Augusto", "123.123.123-12", 5000, 200)
print(programador.obtem_nome_completo())
print(programador.calcula_pagamento())
print(type(programador))

# cliente = Cliente("Paulo", "Mulotto", "123.123.123-12")
# print(cliente.obtem_nome_completo())
# print(type(cliente))

