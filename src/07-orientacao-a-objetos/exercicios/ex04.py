""" Exercício 04 """

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
        if value == " " or not value:
            raise ValueError("O prontuario não pode ser vazio ou nulo")
        self._prontuario = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        if value == " " or not value:
            raise ValueError("O nome não pode ser vazio ou nulo")
        self._nome = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if value == " " or not value:
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


class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel
        self.participacoes = []
    
    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        if value <= 0 or not value:
            raise ValueError("O codigo não pode ser vazio ou nulo (códigos devem ser maior que 0)")
        self._codigo = value

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        if value == " " or not value:
            raise ValueError("O titulo não pode ser vazio ou nulo")
        self._titulo = value

    @property
    def responsavel(self):
        return self._responsavel

    @responsavel.setter
    def responsavel(self, value):
        if value == " " or not value:
            raise ValueError("O responsavel não pode ser vazio ou nulo")
        self._responsavel = value

    @classmethod
    def from_string(cls, rep_aluno):
        codigo, titulo, responsavel = rep_aluno.split(sep=",")
        return cls(int(codigo), titulo, responsavel)

    def add_participacao(self, participacao):
        self.participacoes.append(participacao)

    def print_participacoes(self):
        print("Participações do Projeto:", self.titulo)
        if len(self.participacoes) > 0:
            print(len(self.participacoes))
        else:
            print("Nenhuma participação")

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.codigo == value.codigo
        return False

    def __hash__(self):
        return hash(self.codigo)

    def __str__(self):
        return f'Projeto[codigo={self.codigo}, titulo={self.titulo}, responsavel={self.responsavel}]'

    def __repr__(self):
        return f'Projeto({self.codigo},{self.titulo},{self.responsavel})'


class Participacao:
    def __init__(self, codigo, data_inicio, data_fim, aluno, projeto):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto = projeto
    
    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        if value <= 0 or not value:
            raise ValueError("O codigo não pode ser vazio ou nulo (códigos devem ser maior que 0)")
        self._codigo = value

    @property
    def data_inicio(self):
        return self._data_inicio

    @data_inicio.setter
    def data_inicio(self, value):
        if value == " " or not value:
            raise ValueError("A data de inicio não pode ser vazio ou nulo")
        self._data_inicio = value

    @property
    def data_fim(self):
        return self._data_fim

    @data_fim.setter
    def data_fim(self, value):
        if value == " " or not value:
            raise ValueError("A data de fim não pode ser vazio ou nulo")
        self._data_fim = value

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.codigo == value.codigo
        return False

    def __hash__(self):
        return hash(self.codigo)

    def __str__(self):
        return f'Participacao[codigo={self.codigo}, data_inicio={self.data_inicio}, data_fim={self.data_fim}, aluno={self.aluno}, projeto={self.projeto}]'

    def __repr__(self):
        return f'Participacao({self.codigo},{self.data_inicio},{self.data_fim},{self.aluno},{self.projeto})'


aluno1 = Aluno('SP010101', 'Joãoxinho', 'jaum@email')

projeto1 = Projeto(1, 'Laboratório de Desenvolvimento de Software', 'Pedro Gomes')

participacao1 = Participacao(1, "22/05/2023", "07/09/2023", aluno1, projeto1)

projeto1.add_participacao(participacao1)

print(projeto1.print_participacoes())

