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
Quantidade de Combustível = %.2f
Km andados = %.2f
        """ % (self.kmporlitro, self.qtdcombustivel, self.km_andados)

    def obtergasolina(self):
        return f"Seu tanque possui {self.qtdcombustivel} litros de combustível"

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
        return f"Você abasteceu {litro} litros"


# criação do socket
serverCarro = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 4321
serverCarro.bind((host, port))
serverCarro.listen()


while True:
    print("server carro está ouvindo")
    clientsocket, addr = serverCarro.accept()
    print("Got a connection from %s\n %s" % (str(addr), str(clientsocket)))

    # introdução
    intro = """
SIMULADOR DE CONSUMO DE COMBUSTÍVEL
seja bem vindo(a)! 

instruções:
- Insira o número correspondente a opção desejada na tabela
- Sempre insira APENAS números se for requisitado alguma resposta
- Sempre aperte ENTER para continuar e espere um pouco

Mas primeiro precisamos saber quantos Km por Litro seu carro consome: 
"""

    # instanciação do objeto
    clientsocket.send(intro.encode())
    consumo = clientsocket.recv(1024)
    novocarro = Carro(consumo.decode())

    # opções de manuseio do objeto
    opc = 0
    while opc != 5:
        tabela = """
-----------------------------------,
Opções:                            |
-----------------------------------|
1 - Andar                          |
2 - Abastecer                      |
3 - Ver quantidade de combustível  |
4 - Ver dados do seu carro         |
5 - Sair                           |
-----------------------------------'
Inserir número da opção desejada: """
        clientsocket.send(tabela.encode())
        opc1 = clientsocket.recv(1024)
        opc = int(opc1.decode())
        print("O cliente escolheu a opção ", opc)

        if opc == 1:
            clientsocket.send("Quantos Km você quer andar?".encode())
            quilometro = clientsocket.recv(1024)
            clientsocket.send(novocarro.andar(quilometro.decode()).encode())

        elif opc == 2:
            clientsocket.send("Quantos litros você deseja abastecer? ".encode())
            abastece = clientsocket.recv(1024)
            clientsocket.send(novocarro.abastecer(abastece.decode()).encode())

        elif opc == 3:
            clientsocket.send(novocarro.obtergasolina().encode())

        elif opc == 4:
            clientsocket.send(novocarro.__str__().encode())

        elif opc == 5:
            clientsocket.send("saindo do programa :)".encode())
            clientsocket.close()

        else:
            clientsocket.send("erro, click enter para tentar novamente".encode())
