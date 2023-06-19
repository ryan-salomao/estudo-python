""" Exercício 01 """

class Aluno:
    def __init__(self, prontuario, nome, email):
        self.prontuario = prontuario
        self.nome = nome
        self.email = email
    
    @property
    def prontuario(self):
        return self._prontuario

    @prontuario.setter
    def prontuario(self, value):
        if value == " " or value == "":
            raise ValueError("O prontuario não pode ser vazio ou nulo")
        self._prontuario = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        if value == " " or value == "":
            raise ValueError("O nome não pode ser vazio ou nulo")
        self._nome = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if value == " " or value == "":
            raise ValueError("O email não pode ser vazio ou nulo")
        self._email = value

    @classmethod
    def from_string(cls, rep_aluno):
        prontuario, nome, email = rep_aluno.split(sep=",")
        return cls(prontuario, nome, email)

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.prontuario == value.prontuario
        return False

    def __hash__(self):
        return hash(self.prontuario)

    def __str__(self):
        return f'Aluno[prontuario={self.prontuario}, nome={self.nome}, email={self.email}]'

    def __repr__(self):
        return f'Aluno({self.prontuario},{self.nome},{self.email})'


aluno1 = Aluno('SP010101', 'Joãoxinho', 'jaum@email')
aluno2 = Aluno.from_string("SP020202,Xorginho,xorge@email.com")

print(aluno1)
print(aluno2)
