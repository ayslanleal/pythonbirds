
class Pessoa:
    olhos = 3
    def __init__(self,*filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)


    def cumprimentar(self):
        return 'Olá'

    @staticmethod
    def metodo_estatico():
        return 4

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos: {cls.olhos}'

class Homem(Pessoa):
    pass

class Mutante(Pessoa):
    olhos = 3



if __name__ == '__main__':
    luciano = Pessoa(nome='Luciano')
    renzo = Pessoa(luciano,nome='Renzo')
    print(luciano.cumprimentar())
    print(luciano.nome)
    for i in renzo.filhos:
        print(renzo.nome)
    print(luciano.nome_e_atributos_de_classe())
    print(luciano.metodo_estatico())

