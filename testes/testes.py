from threading import *
from socket import *
import pickle
import time

Uno = socket(AF_INET, SOCK_STREAM)
Uno.bind(("127.0.0.1", 7777))
Uno.listen()


def mutar(sock):
    sock.send(pickle.dumps([3]))
    time.sleep(0.2)
    sock.send(pickle.dumps([1, "oi"]))
    time.sleep(0.2)
    sock.send(pickle.dumps([1, "MUDOU A COR"]))
    time.sleep(0.2)
    sock.send(pickle.dumps([1, "É A VEZ DO JOGADOR 1"]))
    time.sleep(0.2)
    sock.send(pickle.dumps([2]))
    print(pickle.loads(sock.recv(4096)))
    sock.send(pickle.dumps([1, "ooiiiii"]))
    sock.send(pickle.dumps([2]))
    print(pickle.loads(sock.recv(4096)))
    sock.send(pickle.dumps([2]))
    print(pickle.loads(sock.recv(4096)))


while True:
    clientesocket, adrr = Uno.accept()
    print("Conectado a jogador ", adrr)
    t = Thread(target=mutar, args=(clientesocket,))
    t.start()
