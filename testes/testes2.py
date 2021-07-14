from socket import *
import pickle
from threading import *

player = socket(AF_INET, SOCK_STREAM)
player.connect(("127.0.0.1", 7777))


def mutado():
    print("ESPERE A VEZ DO OUTRO JOGADOR E NÃO DIGITE NADA")
    while True:
        if not not input():
            print("não digite nada opoha >:(")
        print("entrando loop")

        msg = pickle.loads(player.recv(4096))
        print(msg)
        if msg[0] == 2:
            player.send(pickle.dumps(input()))
            break


request = [None]
while request[0] != 0:
    print("vc voltou pro laço")
    request = pickle.loads(player.recv(4096))
    print(request)
    if request[0] == 3:
        t2 = Thread(target=mutado)
        t2.start()
        t2.join()
        print("vc saiu do join")
