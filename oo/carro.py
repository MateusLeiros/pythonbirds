class Carro:
    def __init__(self, motor, direcao):
        self.motor = motor
        self.direcao = direcao

class Motor:
    velocidade = 0
    
    def acelerar(self):
        self.velocidade+=1
    
    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)


class Direcao:
    _direcoes = ('Norte','Leste','Sul','Oeste')
    _valor_direcao = 0
    direcao = _direcoes[_valor_direcao%4]

    def girar_a_direita(self):
        self._valor_direcao += 1
        direcao = self._direcoes[self._valor_direcao%4]
        return direcao
    
    def girar_a_esquerda(self):
        self._valor_direcao -= 1
        direcao = self._direcoes[self._valor_direcao%4]
        return direcao


if __name__ == '__main__':
    carro = Carro()