"""
1. Criar uma classe que modele retângulos.
    1. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
    2. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
    3. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidas de um cômodo. Depois,
    deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
"""


# criação da classe retãngulo
class Retangulo:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def mudarlado(self, a1, b1):
        self.a = float(a1)
        self.b = float(b1)

    def lados(self):
        return self.a, self.b

    def area(self):
        return self.a * self.b

    def perimetro(self):
        return 2*(self.a + self.b)


L1, L2 = input("insira os lados do seu cômodo separados com espaço: \n").split(" ")
l1, l2 = input("insira os lados do seu piso separados com espaço: \n").split(" ")
# instanciação dos objetos comodo e piso
comodo = Retangulo(L1, L2)
piso = Retangulo(l1, l2)

# opções
resposta = 0
while resposta != 6:
    resposta = int(input("""
------------------------------------------------
Opções:
1 - Mudar Lados
2 - Acessar Lados
3 - Área
4 - Perímetro
5 - Quantos pisos e rodapés serão precisos
6 - sair
------------------------------------------------
Inserir resposta:
"""))
    if resposta == 1:
        l, ll = input("insira as novas medidas: ").split(" ")
        opc = int(input("1-Redefinir lados do cômodo\n2-Redefinir lados do Piso\nResposta: "))
        if opc == 1:
            comodo.mudarlado(l, ll)
        elif opc == 2:
            piso.mudarlado(l, ll)

    elif resposta == 2:
        print("\nLados do cômodo e piso: ", comodo.lados(), piso.lados())

    elif resposta == 3:
        print("\nÁrea do cômodo e piso: ", comodo.area(), piso.area())

    elif resposta == 4:
        print("\nPerímetro do cômodo e piso: ", comodo.perimetro(), piso.perimetro())

    elif resposta == 5:
        rodape = comodo.perimetro() / piso.area()
        QTDpisos = comodo.area() / piso.area()
        print("Serão precisos %.2f pisos para completar seu cômodo e %.2f para fazer o rodapé" % (QTDpisos, rodape))
