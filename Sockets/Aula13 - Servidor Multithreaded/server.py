"""
1. Criar um echo server Multi-Threaded que realize o cálculo do IMC do usuário
e o cliente equivalente.
"""
from socket import *
import threading


def handle_client(clientsocket, addr):
    print("Got a connection from %s" % str(addr))
    # pegando peso
    clientsocket.send("Qual seu peso?".encode())
    peso = float(clientsocket.recv(4096).decode())
    # pegando altura
    clientsocket.send("Qual sua altura?".encode())
    altura = float(clientsocket.recv(4096).decode())
    # calculando imc
    imc = peso / (altura * altura)
    # mandando imc
    clientsocket.send(str(imc).encode())
    clientsocket.close()


ss = socket(AF_INET, SOCK_STREAM)
host = '127.0.0.1'
port = 9998
ss.bind((host, port))
ss.listen()
print("Server active on port %s.\n\r" % port)

while True:
    csocket, ad = ss.accept()
    t = threading.Thread(target=handle_client, args=(csocket, ad))
    t.start()
