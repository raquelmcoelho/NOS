"""
Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:
    u Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa
    quantidade de combustível no tanque.
    u O consumo é especificado no construtor e o nível de combustível inicial é 0.
u Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa
distância, reduzindo o nível de combustível no tanque de gasolina.
u Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
u Forneça um método adicionarGasolina( ), para abastecer o tanque.
u Exemplo de uso:
meuFusca = Carro(15); # 15 quilômetros por litro de combustível.
meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível.
meuFusca.andar(100); # anda 100 quilômetros.
meuFusca.obterGasolina() # Imprime o combustível que resta no tanque.
"""


class Carro:
    def __init__(self, consumocombustivel):
        self.kmporlitro = float(consumocombustivel)
        self.qtdcombustivel = 0
        self.km_andados = 0

    def __str__(self):
        return """
        Km/Litro = %.2f
        Quantidade de Combustível = %.2f
        Km andados = %.2f
        """ % (self.kmporlitro, self.qtdcombustivel, self.km_andados)

    def obtergasolina(self):
        return self.qtdcombustivel

    def andar(self, km):
        litros = float(km) / self.kmporlitro
        if self.qtdcombustivel >= litros:
            self.qtdcombustivel -= litros
            self.km_andados += float(km)
            return f"Você consumiu {litros} litros e andou {km} km"
        else:
            return "Gasolina insuficiente"

    def abastecer(self, litro):
        self.qtdcombustivel += float(litro)


# instanciação do objeto
consumo = input("Quantos Km por Litro seu carro consome?\n")
novocarro = Carro(consumo)

# opções de manuseio do objeto
opc = 0
while opc != 5:
    opc = int(input("""
    Opções:
    ---------------------------------
    1 - Andar
    2 - Abastecer
    3 - Ver quantidade de combustível
    4 - Ver dados do seu carro
    5 - Sair
    ---------------------------------
    Inserir número da opção desejada: """))

    if opc == 1:
        quilometro = input("\nQuantos Km você quer andar?\n")
        print(novocarro.andar(quilometro))

    elif opc == 2:
        abastece = input("\nQuantos litros você deseja abastecer?\n")
        novocarro.abastecer(abastece)

    elif opc == 3:
        print(f"\nSeu carro possui {novocarro.obtergasolina()} litros")

    elif opc == 4:
        print(novocarro)

    elif opc == 5:
        break

    else:
        print("erro, selecione uma das opções indicando seu número")
