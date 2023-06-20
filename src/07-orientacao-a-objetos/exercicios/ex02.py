""" Exercício 02 """

class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel
    
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


projeto1 = Projeto(1, 'Laboratório de Desenvolvimento de Software', 'Pedro Gomes')
projeto2 = Projeto.from_string("1,Laboratório de Manutenção de Hardware,João Santos")

print(projeto1)
print(projeto2)
print(projeto1 == projeto2)
