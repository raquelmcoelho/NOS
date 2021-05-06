# NO LADO DO SERVIDOR MEXEREMOS COM O FILE, PARA TORNAR O ACESSO AOS DADOS ALGO RESTRITO AO SERVIDOR
from FileMethods import *
from socket import *
from Classes import *
import pickle


# criando, binding e listening o servidor
servidor = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 9999
servidor.bind((host, port))
print("servidor binded")

while True:
    servidor.listen(5)
    print("Aguardando conexão...")
    clientsocket, adrr = servidor.accept()
    print("conectado a %s" % (str(clientsocket) + str(adrr)))

    client = ""
    data = ""
    while data != "sair":
        # sempre que o cliente quiser manusear o cliente ele manda o nome do manuseio/método
        recebido = clientsocket.recv(4096)
        data = recebido.decode()
        print("MÉTODO ESCOLHIDO: ", data)

        if data == "salvarnovocliente":
            bclient = clientsocket.recv(4096)
            client = pickle.loads(bclient)
            print("cliente recebido:", client)
            atualizar(client.save())
            print("como o file json está agora:\n", ler())
            clientsocket.send('Seu cliente foi salvo'.encode())

        elif data == "adddados":
            # adicionar dados recebidos a um cliente recebido
            bdados = clientsocket.recv(4096)
            dados = pickle.loads(bdados)
            print("dados recebidos", type(dados), "\n", dados)
            bclient = clientsocket.recv(4096)
            client = pickle.loads(bclient)
            print("cliente recebido para salvar dados:", client)
            for i1 in range(len(dados)):
                if i1 <= 2:
                    # adicionando só numeros
                    client.adddados(dados[i1], 1)
                else:
                    # adicionando strings
                    client.adddados(dados[i1], 0)
            replace(client.save())
            print("o file ficou assim depois de adicionar os dados:zn", ler())
            clientsocket.send('Seus dados foram salvos'.encode())

        elif data == "pegarclient":
            # construir e enviar cópia do cliente para manuseio a partir da infor recebida
            binfor = clientsocket.recv(4096)
            infor = pickle.loads(binfor)
            print("informação recebida:", infor)
            client = Cofre(infor[2]["nome"], infor[2]["cofre"])
            # copiando dados dados
            for i in range(len(infor[1])):
                if i <= 2:
                    client.adddados(infor[1][i], 1)
                else:
                    client.adddados(infor[1][i], 0)
            # copiando cofre
            for i1 in zip(infor[2].keys(), infor[2].values()):
                client.adicionarsenha(i1[0], i1[1])

            bclient = pickle.dumps(client)
            clientsocket.send(bclient)
            print("cliente enviado:", client)

        elif data == "replace":
            bclient = clientsocket.recv(4096)
            client = pickle.loads(bclient)
            print("cliente recebido\n", client)
            replace(client.save())
            print("como o file está agora", ler())
            clientsocket.send("seu cliente foi substituido".encode())

        elif data == "deleteuser":
            bclient = clientsocket.recv(4096)
            client = pickle.loads(bclient)
            print("cliente recebido\n", client)
            deleteuser(client.save())
            print("como o file está agora", ler())
            clientsocket.send("seu cliente foi deletado".encode())

        elif data == "acessaruserinfo":
            bclientid = clientsocket.recv(4096)
            clientid = bclientid.decode()
            infor = acessaruserinfo(clientid)
            binfor = pickle.dumps(infor)
            clientsocket.send(binfor)

    clientsocket.close()
