class Pessoa:
    def __init__(self, nome = None, idade = 10):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá {self.nome}'

if __name__ == '__main__':
    p = Pessoa('Mateus', 27)
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)