"""Implementar uma aplicação utilizando a arquitetura do Echo Server
Clássico utilizando a classe Carros, proposta na aula de 19/04. A
aplicação Cliente deve passar os dados para o servidor e executar
os métodos da classe. A aplicação deve ser um simulador de
consumo. Por exemplo, deve ser informado o consumo do veículo,
a quantidade de combustível abastecida, a distância que se
pretende percorrer e quanto restará no tanque após percorrer a
distância."""

# server.py
from socket import *


# Classe Carro
class Carro:
    def __init__(self, consumocombustivel):
        self.kmporlitro = float(consumocombustivel)
        self.qtdcombustivel = 0
        self.km_andados = 0

    def __str__(self):
        return """
Km/Litro = %.2f
Quantidade de Combustivel = %.2f
Km andados = %.2f
        """ % (self.kmporlitro, self.qtdcombustivel, self.km_andados)

    def obtergasolina(self):
        return f"Seu tanque possui {self.qtdcombustivel} litros de combustivel"

    def andar(self, km):
        litros = float(km) / self.kmporlitro
        if self.qtdcombustivel >= litros:
            self.qtdcombustivel -= litros
            self.km_andados += float(km)
            return f"Voce consumiu {litros} litros e andou {km} km"
        else:
            return "Gasolina insuficiente"

    def abastecer(self, litro):
        self.qtdcombustivel += float(litro)
        return f"Voce abasteceu {litro} litros"


# criação do socket
serverCarro = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 4321
serverCarro.bind((host, port))
serverCarro.listen(3)


while True:
    print("server carro está ouvindo")
    clientsocket, addr = serverCarro.accept()
    print("Got a connection from %s %s" % (str(addr), str(clientsocket)))

    # introdução
    intro = """
SIMULADOR DE CONSUMO DE COMBUSTIVEL
seja bem vindo(a)! 

instrucoes:
- Nenhuma palavra eh acentuada devido a codificacao do programa
- Insira o numero correspondente a opcao desejada na tabela
- Sempre insira APENAS numeros se for requisitado alguma resposta
- Sempre aperte ENTER para continuar

Mas primeiro precisamos saber quantos Km por Litro seu carro consome: 
"""

    # instanciação do objeto
    clientsocket.send(intro.encode('ascii'))
    consumo = clientsocket.recv(1024)
    novocarro = Carro(consumo.decode('ascii'))

    # opções de manuseio do objeto
    opc = 0
    while opc != 5:
        tabela = """
-----------------------------------,
Opcoes:                            |
-----------------------------------|
1 - Andar                          |
2 - Abastecer                      |
3 - Ver quantidade de combustivel  |
4 - Ver dados do seu carro         |
5 - Sair                           |
-----------------------------------'
Inserir numero da opcao desejada: """
        clientsocket.send(tabela.encode('ascii'))
        opc1 = clientsocket.recv(1024)
        opc = int(opc1.decode('ascii'))
        print("O cliente escolheu a opção ", opc)
        print(novocarro)

        if opc == 1:
            clientsocket.send("Quantos Km voce quer andar?".encode('ascii'))
            quilometro = clientsocket.recv(1024)
            clientsocket.send(novocarro.andar(quilometro.decode('ascii')).encode('ascii'))

        elif opc == 2:
            clientsocket.send("Quantos litros voce deseja abastecer? ".encode('ascii'))
            abastece = clientsocket.recv(1024)
            clientsocket.send(novocarro.abastecer(abastece.decode('ascii')).encode('ascii'))

        elif opc == 3:
            clientsocket.send(novocarro.obtergasolina().encode('ascii'))

        elif opc == 4:
            clientsocket.send(novocarro.__str__().encode('ascii'))

        elif opc == 5:
            clientsocket.send("saindo do programa :)".encode("ascii"))
            clientsocket.close()

        else:
            clientsocket.send("erro, selecione uma das opcoes indicando seu numero".encode('ascii'))
