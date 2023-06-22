""" Classe Participacao """

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
            raise ValueError(
                "O codigo não pode ser vazio ou nulo (códigos devem ser maior que 0)"
            )
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
        return f"Participacao[codigo={self.codigo}, data_inicio={self.data_inicio}, data_fim={self.data_fim}, aluno={self.aluno}, projeto={self.projeto}]"

    def __repr__(self):
        return f"Participacao({self.codigo},{self.data_inicio},{self.data_fim},{self.aluno},{self.projeto})"
