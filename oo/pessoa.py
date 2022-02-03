class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 10):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {self.nome}'

if __name__ == '__main__':
    mateus = Pessoa(nome='Mateus', idade=27)
    lucimar = Pessoa(mateus, nome = 'Lucimar', idade=54)
    print(mateus.cumprimentar())
    print(mateus.nome)
    print(mateus.idade)
    print(lucimar.nome)
    mateus.sobrenome = 'Leiros'
    for filho in lucimar.filhos:
        print(filho.nome)
    print(lucimar.__dict__)
    print(mateus.__dict__)
    del mateus.sobrenome
    print(mateus.__dict__)