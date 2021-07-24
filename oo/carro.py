class Motor:
    velocidade = 0

    @classmethod
    def acelerar(cls):
        cls.velocidade += 1
        return cls.velocidade

    @classmethod
    def frear(cls):
        cls.velocidade -= 2
        cls.velocidade = max(0, cls.velocidade)
        return cls.velocidade

class Direcao:
    valor = 'Norte'
    @classmethod
    def girar_a_direita(cls):
        if cls.valor == 'Norte':
            cls.valor = 'Leste'
            return cls.valor
        if cls.valor == 'Sul':
            cls.valor = 'Oeste'
            return cls.valor
        if cls.valor == 'Oeste':
            cls.valor = 'Norte'
            return cls.valor
        if cls.valor == 'Leste':
            cls.valor = 'Sul'
            return cls.valor


    @classmethod
    def girar_a_esquerda(cls):
        if cls.valor == 'Norte':
            cls.valor = 'Oeste'
            return cls.valor
        if cls.valor == 'Oeste':
            cls.valor = 'Sul'
            return cls.valor
        if cls.valor == 'Sul':
            cls.valor = 'Leste'
            return cls.valor
        if cls.valor == 'Leste':
            cls.valor = 'Norte'
            return cls.valor

class Carro:

    def __init__(self, direcao,motor):
        self.direcao = direcao
        self.motor = motor

if __name__ == '__main__':
    motor = Motor()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    motor.acelerar()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)

    direcao = Direcao()
    print(direcao.valor)
    direcao.girar_a_direita()
    print(direcao.valor)

    carro = Carro(direcao,motor)

