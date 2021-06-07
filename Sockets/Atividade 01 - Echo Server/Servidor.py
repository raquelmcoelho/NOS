# NO LADO DO SERVIDOR MEXEREMOS COM O FILE, PARA TORNAR O ACESSO AOS DADOS ALGO RESTRITO AO SERVIDOR
from FileMethods import *
from socket import *
from Classes import *
import pickle
import threading

# criando, binding e listening o servidor
servidor = socket(AF_INET, SOCK_STREAM)
servidor.bind(("127.0.0.1", 9999))
print("servidor binded")
servidor.listen()


def usar(clientsocket):
    data = ""
    while data != "sair":
        client = ""
        data = clientsocket.recv(4096).decode()
        print("MÉTODO ESCOLHIDO: ", data)

        if data == "acessaruserinfo":
            clientid = clientsocket.recv(4096).decode()
            infor = acessaruserinfo(clientid)
            clientsocket.send(pickle.dumps(infor))

        elif data == "pegarclient":
            # construir e enviar cópia do cliente para manuseio a partir da infor recebida
            infor = pickle.loads(clientsocket.recv(4096))
            print("informação recebida:", infor)
            client = Cofre(infor[2]["nome"], infor[2]["cofre"])
            # copiando dados
            for i in range(len(infor[1])):
                if i <= 2:
                    client.adddados(infor[1][i], 1)
                else:
                    client.adddados(infor[1][i], 0)
            # copiando cofre
            for i1 in zip(infor[2].keys(), infor[2].values()):
                client.adicionarsenha(i1[0], i1[1])

            clientsocket.send(pickle.dumps(client))
            print("cliente enviado:", client)

        elif data == "replace":
            client = pickle.loads(clientsocket.recv(4096))
            print("cliente recebido\n", client)
            replace(client.save())
            print("como o file está agora", ler())
            clientsocket.send("seu cliente foi substituido".encode())

        elif data == "deleteuser":
            client = pickle.loads(clientsocket.recv(4096))
            print("cliente recebido\n", client)
            deleteuser(client.save())
            print("como o file está agora", ler())
            clientsocket.send("seu cliente foi deletado".encode())

    clientsocket.close()


# loop infinito onde o primeiro send do cliente chama a "função" do servidor
while True:
    print("Aguardando conexão...")
    csocket, adrr = servidor.accept()
    print("conectado a um cliente ☺")
    t = threading.Thread(target=usar, args=(csocket, ))
    t.start()
