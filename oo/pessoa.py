class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome = None, idade = 10):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'
    
    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos: {cls.olhos}'
    
class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    mateus = Homem(nome='Mateus', idade=27)
    lucimar = Pessoa(mateus, nome = 'Lucimar', idade=54)
    print(mateus.cumprimentar())
    print(mateus.nome)
    print(mateus.idade)
    print(lucimar.nome)
    mateus.sobrenome = 'Leiros'
    for filho in lucimar.filhos:
        print(filho.nome)
    #__dict__ possui referencias apenas à atributos de instância, não apresenta atributos de classe, exceto no caso de uma alteração dinâmica
    print(lucimar.__dict__)
    print(mateus.__dict__)
    del mateus.sobrenome
    print(mateus.__dict__)
    print(Pessoa.olhos)
    print(mateus.olhos)
    print(Pessoa.metodo_estatico(), mateus.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), mateus.nome_e_atributos_de_classe())
    print(mateus.cumprimentar())
    print(lucimar.cumprimentar())