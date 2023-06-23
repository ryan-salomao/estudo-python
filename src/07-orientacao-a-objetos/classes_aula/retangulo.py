""" Classe Retângulo """

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    # getter
    @property
    def base(self):
        return self._base

    # setter
    @base.setter
    def base(self, value):
        if value <= 0.0:
            raise ValueError('A base deve ser maior que zero')
        self._base = value

    # getter
    @property
    def altura(self):
        return self._altura

    # setter
    @altura.setter
    def altura(self, value):
        if value <= 0.0:
            raise ValueError('A altura deve ser maior que zero')
        self._altura = value

    @classmethod
    def from_list(cls, lista):
        return cls(lista[0], lista[1])

    @classmethod
    def from_string(cls, rep_retangulo):
        base, altura = rep_retangulo.split(sep=",")
        return cls(float(base), float(altura))

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

    # __str__(self)
    # representação do objeto como string para humanos
    def __str__(self):
        return f'Retangulo[base={self.base}, altura={self.altura}]'

    # __repr__(self)
    # representação do objeto como string para recriar 
    # esse objeto
    # logging, debug
    # representação canonica
    def __repr__(self):
        return f'Retangulo({self.base},{self.altura})'
