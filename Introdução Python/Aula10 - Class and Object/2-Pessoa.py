"""
2. Classe Pessoa: Crie uma classe que modele uma pessoa:
    1. Atributos: nome, idade, peso e altura
    2. Métodos: Envelhecer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo
    a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = int(idade)
        self.peso = float(peso)
        self.altura = float(altura)

    def envelhecer(self, age):
        for i in range(age):
            if self.idade < 21:
                self.crescer(0.005)
                self.idade += 1
            else:
                self.idade += 1

        return self.idade

    def engordar(self, eng):
        self.peso += float(eng)
        return self.peso

    def emagrecer(self, emag):
        self.peso -= float(emag)
        return self.peso

    def crescer(self, alt):
        self.altura += float(alt)
        return self.altura

    def __str__(self):
        return "\nNome: %s\nIdade: %d\nPeso: %.2f\nAltura: %.3f" % (self.nome, self.idade, self.peso, self.altura)


Raquel = Pessoa("Raquel", 18, 65.7, 1.65)
print(Raquel)
print()
Raquel.envelhecer(4)
print("Envelheceu 4 anos", Raquel)
print()
Raquel.emagrecer(2)
print("Emagreceu 2 kilos", Raquel)
print()
Raquel.engordar(5)
print("Engordou 5 kilos", Raquel)
print()
Raquel.crescer(0.05)
print("Cresceu 5 cm", Raquel)
print()
